import itertools


def n_letter_missing(s:str, n=1):
    length = len(s)
    missing_positions = [[i for i in range(length)] for j in range(n)]
    
    miss_combinations = list(itertools.product(*missing_positions))

    for i in range(len(miss_combinations)-1, -1, -1):
        combination = miss_combinations[i]
        if len(combination) != len(set(combination)):
            del miss_combinations[i]

    print(miss_combinations)

    typos = []
    for combination in miss_combinations:
        typo = s
        for position in combination:
            typo = remove_ith_char(typo, position) 
        typos.append(typo)

    return typos

def remove_ith_char(s:str, idx):
    return s[:idx] + s[idx+1:]