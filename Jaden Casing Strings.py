Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def toJadenCase(string):
    return ' '.join([ele.capitalize() for ele in string.split()])
