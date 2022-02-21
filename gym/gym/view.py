class View:
    # @abstractmethod
    def on_new_info(self, env_info):
        pass
    # @abstractmethod
    def on_action(self, action_space):
        pass
    # @abstractmethod
    def on_new_env(self, env, env_config):
        pass
    # @abstractmethod
    def on_await_env_start(self, env_config, env_process_generator):
        pass
    # @abstractmethod
    def on_env_done(self):
        pass
    # @abstractmethod
    def on_spawn(self):
        pass
    # @abstractmethod
    def on_destroy(self):
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