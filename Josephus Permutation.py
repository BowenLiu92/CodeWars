Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def josephus(items,k):
    res = []
    i = 0
    while items:
        i = (i+k-1)%len(items)
        res.append(items.pop(i))
    return res
