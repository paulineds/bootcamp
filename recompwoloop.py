def reverse_complement(seq,material='DNA'):
    """Returns the reverse complement of a base."""

    rev_seq = seq[::-1]
    #for base in reversed(seq):

    rev_seq = rev_seq.replace('T', 'a')
    rev_seq = rev_seq.replace('C', 'g')
    rev_seq = rev_seq.replace('G', 'c')
    rev_seq = rev_seq.replace('A', 't')

    rev_seq = rev_seq.upper()

    return rev_seq
