Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def stock_list(listOfArt, listOfCat):
    l_sim = [(e[0], int(e.split(' ')[1])) for e in listOfArt]
    d, res_l = {}, []
    d = d.fromkeys(listOfCat, 0)
    for e in l_sim:
        if e[0] in d.keys():
            d[e[0]] += e[1]
    #if there is nothing then returns empty
    if not any(d.values()):
        return ''
    else:
        pass
    l = ['(' + letter + ' : '+ str(d[letter]) + ')' for letter in listOfCat]
    return ' - '.join(l)
