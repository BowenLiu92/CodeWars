def is_isogram(string):
    return all([string.lower().count(letter) <=1 for letter in string.lower()])