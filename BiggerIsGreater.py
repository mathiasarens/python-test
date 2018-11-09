import sys
def biggerIsGreater(w):
    for i in range(len(w)-1, 0, -1):
        if w[i-1]<w[i]:
            # w[i-1] is pivot element
            # swap it with smallest and most right element that is bigger than the pivot element
            smallest_element_in_suffix_bigger_than_pivot = chr(ord('z')+1)
            smallest_element_in_suffix_bigger_than_pivot_index = -1
            for j in range(len(w)-1, i-1,-1):
                if w[j] > w[i-1] and w[j] < smallest_element_in_suffix_bigger_than_pivot:
                    smallest_element_in_suffix_bigger_than_pivot = w[j]
                    smallest_element_in_suffix_bigger_than_pivot_index = j
            # swap pivot element with smallest element in suffix
            suffix = list(w[i:len(w)])
            suffix[smallest_element_in_suffix_bigger_than_pivot_index-i] = w[i-1]
            result=list(w[0:i-1])
            result.append(smallest_element_in_suffix_bigger_than_pivot)
            result.append(''.join(reversed(suffix)))
            return ''.join(result)
    return "no answer"


def check_correct_answer(input, expected):
    result = biggerIsGreater(input)
    if result == expected:
        print(result)
    else:
        print("wrong answer")

check_correct_answer("ab", "ba")
check_correct_answer("bb", "no answer")
check_correct_answer("aba", "baa")
check_correct_answer("hefg", "hegf")
check_correct_answer("dhck", "dhkc")
check_correct_answer("dkhc", "hcdk")
check_correct_answer("lmno", "lmon")
check_correct_answer("dcba", "no answer")
check_correct_answer("dcbb", "no answer")
check_correct_answer("abdc", "acbd")
check_correct_answer("abcd", "abdc")
check_correct_answer("fedcbabcd", "fedcbabdc")
check_correct_answer("zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgmw", "zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgwm")
check_correct_answer("zyyxwwtrrnmlggfeb", "no answer")
check_correct_answer("tccjaoahruyblpejzgkfnpmqoajnvqnvqmcdwpioxkrllofvixidannpvzxtpnzdtyxfkcloanztgkvgsngqxahnzmtrh", "tccjaoahruyblpejzgkfnpmqoajnvqnvqmcdwpioxkrllofvixidannpvzxtpnzdtyxfkcloanztgkvgsngqxahnzrhmt")