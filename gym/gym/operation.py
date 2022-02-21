"""
The glue between environment, strategy, and view
"""


# import environment, strategy, view
from .environment import Environment
from .strategy import Strategy
from .view import View
## TODO
from abc import ABC, abstractmethod
from dataclasses import dataclass


class Operation(ABC):
    @abstractmethod
    def operate(self):
        pass # can be defaulted to perform, train, or can be a singleton for perform and train.
    @abstractmethod
    def perform(self):
        pass
    @abstractmethod
    def train(self):
        pass

@dataclass
class ConcreteOperation(Operation):
    stacks: None # Iterable[Environment, Optional<EnvConfig>, Strategy, Iter[View], Optional<Obj>]
    def operate(self):
        for env, env_config, strategy, view_iter, _ in self.stacks:
            # TODO: params (4th field) is currently ignored
            
