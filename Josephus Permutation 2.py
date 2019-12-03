def josephus(items,k):
    res = []
    n = len(items)
    if not n: return []
    i = (k - 1)%n
    res.append(items[i])
    return res + josephus(items[i+1:] + items[:i], k)
