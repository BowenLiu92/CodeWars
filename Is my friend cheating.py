Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def removNb(n):
    pic, nsum = list(range(round(n/2), n+1)), n*(n+1)/2
    res = []
    for a in pic:
        b =  (nsum - a)/(a + 1)
        if b.is_integer() and b <= n:
            res.append((a, b))
    return sorted(res)
