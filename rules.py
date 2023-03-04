from itertools import combinations

def remove_ith_char(s:str, idx):
    return s[:idx] + s[idx+1:]

def skip_letter(s:str, n=1):
    length = len(s)

    miss_combinations = list(combinations([i for i in range(length)], n))

    typos = []
    for combination in miss_combinations:
        typo = s
        for i in range(len(combination)-1, -1, -1):
            typo = remove_ith_char(typo, combination[i]) 
        typos.append(typo)

    return typos

def reverse_letter(s:str):
    typos = []

    for i in range(len(s)-1, 0, -1):
        typo = list(s)
        typo[i-1], typo[i] = typo[i], typo[i-1]
        typos.append(''.join(typo))
    
    return typos

def double_letter(s:str):
    typos = []

    for i in range(len(s)):
        typo = list(s)
        typo.insert(i, typo[i])
        typos.append(''.join(typo))

    
    return typos

def keyboard_adjacent_letter(s:str):
    pass

def vowel_replace(s:str):
    pass

def homophones_replace(s: str):
    homophones_dict = {
        'j': ['z', 'g', ],
        'a': ['o'],
        'i': ['e'],
        'c': ['s', 'k'],
        'q': ['k'],
        'u': ['o'],
        's': ['sh']
    }

    pass

