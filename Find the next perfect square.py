def find_next_square(sq):
    sq_rt = float(sq**0.5)
    if sq_rt.is_integer():
        return (sq_rt + 1)**2
    return -1
