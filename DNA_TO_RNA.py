def to_rna(dna):
    res = ''

    for i, item in enumerate(dna):
        if item == 'G':
            res = res + 'C'
        elif item == 'C':
            res = res + 'G'
        elif item == 'T':
            res = res + 'A'
        elif item == 'A':
            res = res + 'U'
    return res

print(to_rna('ACGTGGTCTTAA'))



