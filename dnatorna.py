"""
Convert DNA to RNA
"""

def rna(seq):
    """Convert DNA into RNA"""

    #Determine if seq is uppercase
    seq_upper=seq.isupper()

    #convert to lowercase
    seq = seq.lower()

    # swap t for u

    seq= seq.replace('t','u')

    #return upper or lower depending on input

    if seq_upper:
        return seq.upper()
    else:
        return seq

def reverse_rna_complement(seq):
    """
    Convert a DNA sequence into its reverse complement as RNA.
    """

    # Determine if original was uppercase
    seq_upper = seq.isupper()

    # Reverse sequence
    seq = seq[::-1]

    # Convert to upper
    seq = seq.upper()

    # Compute complement
    seq = seq.replace('A', 'u')
    seq = seq.replace('T', 'a')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'g')

    # Return result
    if seq_upper:
        return seq.upper()
    else:
        return seq
