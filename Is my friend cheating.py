def removNb(n):
    pic, nsum = list(range(round(n/2), n+1)), n*(n+1)/2
    res = []
    for a in pic:
        b =  (nsum - a)/(a + 1)
        if b.is_integer() and b <= n:
            res.append((a, b))
    return sorted(res)
