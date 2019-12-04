Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def is_triangle(a, b, c):
    l = [a, b, c]
    if all(e > 0 for e in l):
        maxVal = max(l)
        l.remove(maxVal)
        if sum(l) > maxVal:
            return True
        else:
            pass
    return False
