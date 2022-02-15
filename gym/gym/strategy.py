from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from .environment import Space
from .TODOException import TODOException

@dataclass
class Strategy:
    _knows_config: bool = True
    _name: str = "Unnamed Strategy"

    _last_obs: Space = field(default_factory=lambda:None)
    _last_reward: Space = field(default_factory=lambda:None)
    _env_done: bool = False
    _config: None

    _action: Space = field(default_factory=lambda:None)

    ### Strategy tags ###
    def knows_config(self):
        return self._knows_config
    def strategy_name(self):
        return self._name
    ### ------------- ###

    ### Operation API ###
    def load_env_config(self, config):
        if not self.knows_config():
            raise Warning("Strategy is not supposed to know config")
        self._config = config
    def load_step(self, obs, reward, done):
        self._last_obs      = obs
        self._last_reward   = reward
        self._env_done      = done
    def signal_action(self, new_action):
        self._action = self.strategy_compute_action(new_action)
    ### ------------- ###

    ### Strategy I/O ###
    def last_obs(self):
        return self._last_obs
    def last_reward(self):
        return self._last_reward
    def done(self):
        return self._env_done
    def config(self):
        if not self.knows_config():
            raise Warning("Strategy is not supposed to know config")
        return self._config
    ### ------------ ###

    ### Strategy dev ###
    @abstractmethod
    def strategy_compute_action(self, new_action_space: Space):
        """Computes the next action to take 

        Args:
            new_action_space (Space): The next action space, overwrite this value

        Raises:
            TODOException: [description]

        Returns:
            Space: Copied or overwritten action space
        """
        raise TODOException("strategy_compute_action")
    ### ------------ ###
    