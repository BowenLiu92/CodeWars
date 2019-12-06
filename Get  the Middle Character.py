def get_middle(s):
    return s[({True: (len(s)//2 - 1), False: (len(s)//2)}[len(s)%2 == 0]):
            ({True: (len(s)//2 + 1), False: (len(s)//2) + 1}[len(s)%2 == 0])]