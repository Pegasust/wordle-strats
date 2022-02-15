import cProfile

def match_color_simple(guess, word):
    # TODO

def match_color_dict(guess, word):
    retval = [0] * len(guess)
    remaining_count = dict()
    for i in range(len(guess)):
        if guess[i] == word[i]:
            retval[i] = 2
        remaining_count[word[i]] = remaining_count.get(word[i], 0) + 1
    for i in range(len(guess)):
        if retval[i] == 2:
            continue
        if remaining_count.get(guess[i], 0) > 0:
            remaining_count[guess[i]] -= 1
            retval[i] = 1
    return retval
