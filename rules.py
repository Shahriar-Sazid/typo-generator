from itertools import combinations, permutations, product
import re


def remove_ith_char(s: str, idx):
    return s[:idx] + s[idx + 1:]

def replace_str_index(s,index, victim_length = 1, replacement=''):
    if index >= len(s) or index < 0:
        return s
    
    return f"{s[:index]}{replacement}{s[index+victim_length:]}"

def skip_letter(s: str, n=1):
    length = len(s)

    miss_combinations = list(combinations([i for i in range(length)], n))

    typos = []
    for combination in miss_combinations:
        typo = s
        for i in range(len(combination) - 1, -1, -1):
            typo = remove_ith_char(typo, combination[i])
        typos.append(typo)

    return typos


def reverse_letter(s: str):
    typos = []

    for i in range(len(s) - 1, 0, -1):
        typo = list(s)
        typo[i - 1], typo[i] = typo[i], typo[i - 1]
        typos.append(''.join(typo))

    return typos


def double_letter(s: str):
    typos = []

    for i in range(len(s)):
        typo = list(s)
        typo.insert(i, typo[i])
        typos.append(''.join(typo))

    return typos


def keyboard_adjacent_letter(s: str):
    pass


def vowel_replace(s: str):
    pass


def homophones_replace(s: str):
    typos = []
    homophones_dict = (
        ('j', 'z', 'g'),
        ('a', 'o'),
        ('i', 'e'),
        ('c', 's', 'k'),
        ('q', 'k'),
        ('u', 'o', 'oo'),
        ('f', 'p', 'ph'),
        ('s', 'sh'),
    )

    for homophone in homophones_dict:
        index_dict = {}
        for char in homophone:
            idx_list = [m.start() for m in re.finditer(char,s)]
            for idx in idx_list:
                index_dict[idx] = {
                    'index': idx,
                    'length': len(char)
                }
                
        
        indices = list(index_dict.values())
        combined = [homophone for i in range(len(indices))]
        combinations = list(product(*combined))

        for combination in combinations:
            typo = s        
            for i in range(len(indices)-1, -1, -1):
                typo = replace_str_index(typo, indices[i]['index'], indices[i]['length'], combination[i])
                
            typos.append(typo)

    return list(set(typos))



