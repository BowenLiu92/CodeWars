def ETA(path):
    d = {'-':1, '/':2, '|':0.5}
    res = 0
    for i in path:
        res += d[i]
    return res
