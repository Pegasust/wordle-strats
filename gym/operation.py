import environment, strategy, view
## TODO
from abc import ABC, abstractmethod
from dataclasses import dataclass
@dataclass
class Operation(ABC):
    env: environment.Environment
    strategy: strategy.Strategy
    view: view.View
    @abstractmethod
    def operate(self):
        pass # can be defaulted to perform, train, or can be a singleton for perform and train.
    @abstractmethod
    def perform(self):
        pass
    @abstractmethod
    def train(self):
        pass