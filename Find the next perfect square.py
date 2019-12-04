Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def find_next_square(sq):
    sq_rt = float(sq**0.5)
    if sq_rt.is_integer():
        return (sq_rt + 1)**2
    return -1
