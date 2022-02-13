"""
Contains some utilities to implement a strategy
"""

import environment
from abc import ABC, abstractmethod
from dataclasses import dataclass
import TODOException

@dataclass
class Strategy(ABC):
    env: environment.Environment = None

    @abstractmethod
    def get_env(self):
        raise TODOException("get_env")
    ### Starting-over ###
    @abstractmethod
    def new_observations(self):
        return self.env.observable_space()
    @abstractmethod
    def new_actions(self):
        return self.env.action_space()
    def load(self, new_env):
        self.env = new_env
    ### -------------- ###

    ### Decisions ###
    def perform_action(self, action=None):
        if not action:
            action = self._action
        self._action = self._pre_step(action)
        outcome = self.get_env().step(action)
        self._prev_step = self._post_step(action, outcome)
    def get_current_action(self):
        return self._action
    def get_last_outcome(self):
        return self._prev_step
    def env_ended(self):
        return self.get_last_outcome()[2] == True
    def get_last_reward(self):
        return self.get_last_outcome()[1]
    def get_last_observations(self):
        return self.get_last_outcome()[0]
    def get_last_info(self):
        return self.get_last_outcome()[3]
    ### --------- ###

    ### Middlewares ###
    def pre_step(self, action):
        pass
    def post_step(self, action, outcome):
        pass
    
    #### Wraps ####
    def _post_step(self, action, outcome):
        self.post_step(action, outcome)
        return outcome
    def _pre_step(self, action):
        self.pre_step(action)
        return action
    ### ----------- ###