"""
Controller code using a discrete environment and strategy.
"""
import gym

class FullBacktest(gym.operation.Operation):
    def operate(self):
        for env in self.env.environments():
            self.view.on_new_env(env)
            done = False
            while not done:
                self.view.on_action(self.strategy.get_current_action())
                _, _, done, inf = self.strategy.perform_action()
                self.view.on_new_info(self.strategy.get_last_info())
    def train(self):
        return self.operate()
    def perform(self):
        return self.operate()

            
