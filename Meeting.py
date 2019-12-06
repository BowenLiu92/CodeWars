def meeting(s):
    in_res = [names.split(':') for names in s.upper().split(';')]
    to_so = sorted([(l[1], l[0]) for l in in_res])
    res_l = [', '.join(x) for x in to_so]
    return '(' + ')('.join(res_l) + ')'