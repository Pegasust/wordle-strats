"""
This example provides an environment for Wordle game

Action-space: [word for word in wordlist if not_selected(word)]
Observable-space: [[word for word in wordlist if is_possible(word)], [0, 1, 2, 0, 1]]
Seed-space: index of chosen word (answer)

step:
    - validation: action is within bounds
    - record guessed
    - compare against answer, give wordle_diff as reward
    - done if guessed == answer
    - info: nothing right now

"""
from gym import Environment, UnlabelledSpace
from random import choice, randint
from dataclasses import dataclass, field
from wordlist import La

def _match_color(guess: str, word: str, retval:list=None):
    if not retval:
        retval = [[randint(0, 2), "dum"] for _ in range(5)]
        retval.append("do not modify")
    remaining_count = dict()
    # green pass
    for i in range(len(guess)):
        if guess[i] == word[i]:
            retval[i] = 2
            continue
        remaining_count[word[i]] = remaining_count.get(word[i], 0) + 1
    # yellow pass
    for i in range(len(guess)):
        if retval[i] == 2:
            continue
        if remaining_count.get(guess[i], 0) > 0:
            remaining_count[guess[i]] -= 1
            retval[i] = 1
        else:
            retval[i] = 0
    return retval[:5]

def generate_wordlist():
    return [word for word in La]

def no_match(guess, guess_result, wordlist):
    def matches(guess, guess_result, word):
        word_rem = dict()
        guess_yellow = dict()
        # green check
        for g, res, w in zip(guess, guess_result, word):
            if res == 2 and g != w:
                return False
            word_rem[w] = word_rem.get(w, 0) + 1
            guess_yellow[g] = guess_yellow.get(g, 0) + 1
        # yellow check
        for g in guess_yellow.keys():
            if word_rem.get(g, 0) < guess_yellow[g]:
                return False
        return True
    return {word for word in wordlist if not matches(guess, guess_result, word)}
            
@dataclass
class WordleEnv(Environment):
    seed: None
    wordlist: list = field(default_factory=generate_wordlist)
    guessed: list = field(default_factory=lambda:[])
    # seed: int = field(default_factory=lambda: choice(self.environment_config_space()))
    def __post__init__(self):
        self.seed = self.seed if self.seed else choice(self.environment_config_space())
        self.answer = self.wordlist[self.seed]
        self._acceptable = set(self.wordlist)
        self._possible = set(self.wordlist)
        self._observable = UnlabelledSpace([range(0,3) for _ in range(5)].append(La))
        self._info = {
            "possible": self._possible,
            "acceptable": self._acceptable
        }

    def get_answer(self):
        return self.answer

    def environment_config_space(self):
        return range(len(self.wordlist))
    
    def generate_from_config(self, config):
        return self.__init__(config)
    
    def action_space(self):
        return UnlabelledSpace(self.acceptable_words())

    def observable_space(self):
        return self._observable.copy()
    
    def acceptable_words(self):
        return self._acceptable

    def possible_words(self):
        return self._possible
    
    def get_info(self):
        return self._info

    def on_guess(self, guess):
        self.guessed.append(guess)
        self._acceptable -= {guess}
        obs = self.observable_space()
        color_match = _match_color(guess, self.answer, obs.var)
        # remove possible from given color_match
        impossible_words = no_match(guess, color_match, self._possible)
        self._possible -= impossible_words
        reward_space = UnlabelledSpace([range(1, len(La)+1)],
            [len(impossible_words)])
        obs.var[6] = self._possible
        self._info = {
            "color_match": color_match,
            "guess": guess,
            "reward": reward_space,
            "possible": self._possible,
            "acceptable": self._acceptable
        }
        return (obs, reward_space, guess == self.answer, self._info) 

    def step(self, action_space):
        super().step(action_space)
        guess = action_space[0][0]
        return self.on_guess(guess)

if __name__ == "__main__":
    print(generate_wordlist())