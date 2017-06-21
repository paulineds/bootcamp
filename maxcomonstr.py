def longuest_common_str(seq1, seq2):
    """return the longest common substring """

    max_lenght_str = min(len(seq1), len(seq2))

    if len(seq1) == max_lenght_str:
        trial = seq1
        searching_seq = seq2
    else:
        trial = seq2
        searching_seq = seq1

    for i in range(len(trial),0,-1):
        nb_substr=len(trial)-i+1
        for j in range(0,nb_substr):
            sub_trial=trial[j:j+i]
            if sub_trial in searching_seq:
                return sub_trial
    return 0
