from wordle_env import WordleEnv
from wordle_console_view import WordleConsoleView
from gym import Operation

class WordleOperation(Operation):
    def __init__(self):
        super().__init__(WordleEnv(), __, WordleConsoleView())
        