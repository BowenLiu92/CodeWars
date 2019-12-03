Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def ETA(path):
    d = {'-':1, '/':2, '|':0.5}
    res = 0
    for i in path:
        res += d[i]
    return res
