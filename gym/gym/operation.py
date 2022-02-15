# import environment, strategy, view
from .environment import Environment
from .strategy import Strategy
from .view import View
## TODO
from abc import ABC, abstractmethod
from dataclasses import dataclass
@dataclass
class Operation(ABC):
    env: Environment
    strategy: Strategy
    view: View
    @abstractmethod
    def operate(self):
        pass # can be defaulted to perform, train, or can be a singleton for perform and train.
    @abstractmethod
    def perform(self):
        pass
    @abstractmethod
    def train(self):
        pass