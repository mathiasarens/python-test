# https://www.hackerrank.com/contests/saggezza-coding-test/challenges/two-characters
from collections import Counter
def alternate(s):
    letter_dict = Counter(s)
    maximum = 0
    letter_dict_items = list(letter_dict.items())
    for i in range(len(letter_dict_items)):
        for j in range(i+1, len(letter_dict_items)):
            last_character = None
            ok = True
            for k in range(len(s)):
                if s[k] == letter_dict_items[i][0] or s[k] == letter_dict_items[j][0]:
                    if last_character == s[k]:
                        ok = False
                        break
                    last_character = s[k]
            if ok:
                maximum = max(maximum, letter_dict[letter_dict_items[i][0]] + letter_dict[letter_dict_items[j][0]])
    return maximum

print(alternate("beabeefeab")==5)
print(alternate("a")==0)
print(alternate("ab")==2)
print(alternate("bab")==3)
print(alternate("baab")==0)
print(alternate("baba")==4)
print(alternate("babb")==0)
print(alternate("babc")==3)
print(alternate("bacb")==3)
print(alternate("cbab")==3)
print(alternate("bcab")==3)
