#My solution, using itertools groupby
from itertools import groupby
def letter_count(s):
    d = {}
    for k, g in groupby(sorted(s)):
        d[k] = len(list(g))
    return d

#Another very good solution, not mine, using `Counter`
#Actually this one is much easier.
from collections import Counter
def letter_count(s):
    return Counter(s)