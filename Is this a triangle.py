def is_triangle(a, b, c):
    l = [a, b, c]
    if all(e > 0 for e in l):
        maxVal = max(l)
        l.remove(maxVal)
        if sum(l) > maxVal:
            return True
        else:
            pass
    return False
