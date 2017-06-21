def reverse_complement(seq,material='DNA'):
    """Returns the reverse complement of a base."""

    #initialize the reverse complement
    rev_seq=''
    for base in reversed(seq):
    #for base in seq(::-1):
        rev_seq += complement_base(base, material=material)

    return rev_seq

def complement_base(base, material='DNA'):
    """Returns the Watson-Crick complement of a base."""

    base=base.lower()

    if base == 'a':
        if material=='DNA':
            return 'T'
        elif material=='RNA':
            return 'U'
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'
