Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def score_hand(cards):
    d, res, countA = {}, 0, 0
    for num in range(2, 11):
        d[str(num)] = num
    for face in 'JQK':
        d[face] = 10
    d['A'] = 11
    for card in cards:
        if card == 'A':
            countA += 1
        res += d[card]
    while res > 21 and countA:
        res -= 10
        countA -= 1
    return res
