#My solution, using Counter from collections
from collections import Counter
def duplicate_count(text):
    return len([k for k, v in Counter(text.lower()).items() if v > 1])

#However, the best practice is still a bit better than my solution
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])