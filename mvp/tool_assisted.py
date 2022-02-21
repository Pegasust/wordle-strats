from wordlist import La

UNGUESSED = 0       # Black
NOT_IN = 1          # Grey
WRONG_ORDER = 2     # Yellow
CORRECT = 3         # Green

def _potential_words(last_potential_words, guess, outcome):
    def retain_word(word, guess, outcome):
        # order
        word_char_cnt = dict()
        must_be_0 = {c for c, o in zip(guess, outcome) if o == NOT_IN}
        if any([(o == CORRECT and g != w) or (o == WRONG_ORDER and g == w) for w,g,o in zip(word, guess, outcome)]):
            return False
        # yellow credits
        for w, g, o in zip(word, guess, outcome):
            word_char_cnt[w] = word_char_cnt.get(w, 0) + (1 if o != CORRECT else 0)
            word_char_cnt[g] = word_char_cnt.get(g, 0) - (1 if o == WRONG_ORDER else 0)
        retain = all([v >= 0 for v in word_char_cnt.values()]) and all([v == 0 for c, v in word_char_cnt.items() if c in must_be_0])
        return retain
    return [word for word in last_potential_words if retain_word(word, guess, outcome)]

def potential_words_zip(outputs, wordlist=None):
    if not wordlist:
        wordlist = La.copy()
    for guess, outcome in outputs:
        wordlist = _potential_words(wordlist, guess, [int(o) for o in outcome])
    return wordlist

def potential_words(guesses, outputs, wordlist=None):
     return potential_words_zip(zip(guesses, outputs))

def all_potential(wordlist=None):
    if not wordlist:
        return {chr(c): {i for i in range(5)} for c in range(ord('a'), ord('z')+1)}
    potential = dict()
    for word in wordlist:
        for i, char in enumerate(word):
            if char not in potential:
                potential[char] = set()
            potential[char].add(i)
    return potential

def derive_potential(output_zips, potential=None, wordlist=None):
    if not potential:
        potential = all_potential(wordlist)
    for guess, output in output_zips:
        for g, o in zip(guess, output):
            if o == NOT_IN:
                potential[g][0].clear()
            elif o == CORRECT:
                potential[g][1].add()
            

# def score_one_step_zip(outputs):
#     knowledge = 
    
#     return {word: score(word, wordlist) for word in wordlist}


if __name__ == "__main__":
    print(potential_words(["salet"], [[1,3,1,1,3]]))
    print(potential_words(["salet", "again"], 
            [[NOT_IN, CORRECT, NOT_IN, NOT_IN, CORRECT], [WRONG_ORDER, NOT_IN, NOT_IN, CORRECT, NOT_IN]]
        ))    
    print(potential_words(["salet", "again", "habit"], 
            [[NOT_IN, CORRECT, NOT_IN, NOT_IN, CORRECT], 
            [WRONG_ORDER, NOT_IN, NOT_IN, CORRECT, NOT_IN],
            [NOT_IN, CORRECT, NOT_IN, CORRECT, CORRECT]]
        ))
    print(potential_words(["salet"], ["13113"]))
    print(potential_words(["salet", "again"], ["13113", "21131"]))
    print(potential_words(["salet", "again", "habit"], ["13113", "21131", "13133"]))

    print(potential_words(["salet"], ["11132"]))