from abc import ABC, abstractmethod

class View(ABC):
    @abstractmethod
    def on_new_info(self, env_info):
        pass
    @abstractmethod
    def on_action(self, action_space):
        pass
    @abstractmethod
    def on_new_env(self, env, env_config):
        pass

class ConsoleView(View):
    def on_new_info(self, env_info):
        print(f"New info: {env_info}")
    def on_action(self, action_space):
        print(f"Performing action: {action_space}")
    def on_new_env(self, env, env_config=None):
        print(f"New environment: {env}")
        if env_config:
            print(f"env_config: {env_config}")