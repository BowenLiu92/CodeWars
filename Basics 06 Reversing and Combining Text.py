def reverse_and_combine_text(text):
    t = text.split()
    while len(t) > 1:
        if len(t)%2 == 0:
            t = [a[::-1] + b[::-1] for a, b in zip(t[::2], t[1::2])]
        elif len(t)%2 == 1:
            tail = t[-1][::-1]
            t = [a[::-1] + b[::-1] for a, b in zip(t[::2], t[1::2])]
            t.append(tail)
    return t[0]       