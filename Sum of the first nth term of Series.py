def series_sum(n):
    res, i = 0, 1
    while i <= n:
        res += 1/(3*i - 2)
        i += 1
    return '{:0.2f}'.format(n)