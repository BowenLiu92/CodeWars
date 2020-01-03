def is_pangram(s):
    s_a = [cha.lower() for cha in s if cha.isalpha()]
    s_n = set(ord(e) for e in s_a)
    return len(s_n) == 26