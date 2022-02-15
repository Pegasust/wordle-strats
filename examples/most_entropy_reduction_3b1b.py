"""
Studies what 3 blue 1 brown means by most-entropy strategy.
By selecting words that reduces entropy the most, we eliminate
the most expected potential candidates.

Entropy is defined as E[surprise]  # where entropy is measure of uncertainty

This strategy is a correct algorithm because it seeks to eliminate
non-selected words to eventually reach the answer.
"""

from wordlist import La  # words that would be chosen

