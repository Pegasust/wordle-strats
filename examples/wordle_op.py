from wordle_env import WordleEnv
from wordle_console_view import WordleConsoleView
from gym import Operation

class WordleOperation(Operation):
    def operate(self):
        pass
    def perform(self):
        pass
    def train(self):
        pass

if __name__ == "__main__":
    from gym import run
    run(WordleOperation)