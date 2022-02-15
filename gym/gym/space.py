from abc import ABC, abstractmethod
from .TODOException import TODOException
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
        self.bounds = bounds
        self.default_value = default_value if default_value else [None for _ in range(len(bounds))]
        self.var = self.generate_var()
    def generate_var(self):
        return self.default_value.copy()
    def get_bounds(self):
        return self.bounds 
    def within_bounds(self):
        return [v in b for v, b in zip(self.var, self.bounds)].count(False) == 0
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
