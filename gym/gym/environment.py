"""
    This file provide the interface (for dependency injection)
    for an environment to train and backtest.
"""
from abc import ABC, abstractmethod
from typing import Iterable
from .TODOException import TODOException

class Environment:
    pass
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
        if not action_space.within_bounds():
            raise ValueError("given action not in action space")
    
    @abstractmethod
    def get_info(self):
        raise TODOException("get_info")
    
    def copy(self):
        raise ValueError("Environment cannot be copied")
    
    def unchoose(self):
        raise ValueError("Environment does not support unchoose")

class EnvironmentFactory(ABC):
    def __init__(self, ctor):
        self._env_ctor = ctor

    @abstractmethod
    def config_bounds(self):
        raise AttributeError("Environment config bounds unknown")

    def generate_from_config(self, config):
        return self._env_ctor(config)

    def environments(self):
        # (This pattern is called generator using coroutines)
        for conf in self.config_bounds():
            yield self.generate_from_config(conf)

@dataclass
class EnvironmentAbstractFactory:
    _ctor: dict = field(default_factory=lambda:dict())
    def register_factory(self, factory_id, factory_ctor):
        self._ctor[factory_id] = factory_ctor
        
    def create_factory(self, factory_id, *args, **kwargs):
        return self._ctor[factory_id](*args, **kwargs)
    