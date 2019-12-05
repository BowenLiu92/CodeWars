def DNA_strand(dna):
    d = {'A': 'T', 'T':'A', 'C':'G', 'G':'C'}
    return ''.join([d[key] for key in dna])