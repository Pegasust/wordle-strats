"""
    This file provide the interface (for dependency injection)
    for an environment to train and backtest.
"""
from abc import ABC, abstractmethod
import TODOException

class Space(ABC):
    @abstractmethod
    def get_bounds(self):
        """[summary]

        Returns:
            Consistent collection that iterates (and/or enumerates)
            through bounds of each dimension in `self` space
        Raises:
            TODOException: If this function is not overloaded
        """
        raise TODOException("get_bounds")
    @abstractmethod
    def within_bounds(self):
        """[summary]

        Returns:
            bool: Whether the modified space is within the bounds
        Raises:
            TODOException: If this function is not overloaded
        """
        raise TODOException("within_bounds")
    @abstractmethod
    def copy(self):
        pass

class UnlabelledSpace(Space):
    def __init__(self, bounds, default_value=None):
        self.default_value = default_value
        self.bounds = bounds
        self._space = self.generate_var()
    def get_bounds(self):
        return self.bounds 
    def within_bounds(self):
        return [value in bound for value, bound in self._space].count(False) == 0
    def copy(self):
        return UnlabelledSpace(self.bounds, self.default_value)

# class LabelledSpace(Space):
#     def __init__(self, bounds, default_value=None):
#         """
#         Args:
#             bounds (Iterable(Tuple(Any, Domain))): Bounds and labels (zipped vectors or Dict.items())
#             default_value ([type], optional): Default value for each field. Defaults to None.
#         """
#         self._space = {label: (default_value, bound) for label, bound in bounds}

class Environment(ABC):
    @abstractmethod
    def action_space(self):
        """
            Returns a copy collection of possible actions we can take in this step()
        """
        raise TODOException("action_space")
    @abstractmethod
    def observable_space(self):
        """
            Returns a collection of observations made from the last step()
        """
        raise TODOException("observable_space")
    @abstractmethod
    def step(self, action_space):
        """
            Params:
                action: the action in action space we're taking for this step
            Returns:
                (obs_space, reward_space, done_environment, info)
        """
        assert action_space.within_bounds()
        raise ValueError("given action not in action space")
    def environments(self):
        # (This pattern is called generator using coroutines)
        for conf in self.environment_config_space():
            yield generate_from_config(conf)
    def environment_config_space(self):
        raise AttributeError("Environment config space unknown")
    def generate_from_config(self):
        raise TODOException("generate_from_config")
    