"""
This example provides an environment for Wordle game

Action-space: [word for word in wordlist if not_selected(word)]
Observable-space: [word for word in wordlist if is_possible(word)]
Seed-space: index of chosen word (answer)

step:
    - validation: action is within bounds
    - record guessed
    - compare against answer, give wordle_diff as reward
    - done if guessed == answer
    - info: nothing right now

"""

from gym import Environment, UnlabelledSpace
from random import choice


from wordlist import La
class WordleEnv(Environment):
    def __init__(self, seed=None):
        self.wordlist = La
        self.guessed = []
        if not seed:
            seed = choice(self.environment_config_space())
        self.answer = self.wordlist[seed]
    def environment_config_space(self):
        return range(len(self.wordlist))
    