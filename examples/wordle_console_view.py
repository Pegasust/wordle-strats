from gym import View
from dataclasses import dataclass, field
from colorama import Fore, Style, Back

@dataclass
class WordleConsoleView(ConsoleView):
    guesses: list = field(default_factory=lambda:[])
    color_match: list = field(default_factory=lambda:[])
    rewards: list = field(default_factory=lambda:[])
    conf: None

    def _render(self, possible, acceptable):
        print("-"*80)
        print(f"{Style.BRIGHT}Guesses{Style.RESET_ALL}")
        print("-"*5)
        for guess, color, reward in zip(self.guesses, self.color_match, self.rewards):
            color_style = [Style.RESET_ALL, Fore.YELLOW, Fore.GREEN]
            print("".join([f"{color_style[col]}{c}" for c, col in zip(guess,color)]),end="\t")
            print(f"{reward}")
        print("-"*5)
        print(f"{Style.BRIGHT}Accept\tPossible{Style.RESET_ALL}")
        for pos, acc in zip(possible[:10], acceptable[:10]):
            print(f"{pos}\t{acc}")
    def on_new_info(self, info):
        self.guesses.append(info["guess"])
        self.color_match.append(info["color_match"])
        self.rewards.append(info["reward"])
        self._render(info["possible"], info["acceptable"])
    def on_action(self, _):
        pass
    def on_new_env(self, env, env_config=None):
        self.conf = env_config
        info = env.get_info()
        self._render(info["possible"], info["acceptable"])
