from collections import defaultdict
from collections import Counter


def reverseShuffleMergeIncorret(s):
    A = []
    letter_count_in_s = count_letters(s)
    letter_count_for_A = dict(
        map(lambda kv: (kv[0], kv[1]//2), letter_count_in_s.items()))
    letter_matrix = create_letter_matrix(s)

    i = len(s)-1
    while i > 0 and sum(letter_count_for_A.values()) > 0:
        if letter_count_for_A[s[i]] == letter_count_in_s[s[i]]:
            # critical
            A.append(s[i])
            letter_count_for_A[s[i]] -= 1
        elif is_smallest_character(letter_count_for_A, letter_matrix, s, i):
            # it's safe to take the smallest character
            A.append(s[i])
            letter_count_for_A[s[i]] -= 1
        elif next_critical_character(letter_count_for_A, letter_count_in_s, s, i) > s[i]:
            A.append(s[i])
            letter_count_for_A[s[i]] -= 1
        letter_count_in_s[s[i]] -= 1
        i -= 1
    return ''.join(A)

def next_critical_character(letter_count_for_A, letter_count_in_s, s, index_at_s):
    _letter_count_in_s = dict(letter_count_in_s)
    i = index_at_s-1
    while i >= 0:
        if letter_count_for_A[s[i]] == _letter_count_in_s[s[i]]:
            return s[i]
        _letter_count_in_s[s[i]]-=1
        i-=1
    return 'a'

def is_smallest_character(letter_rest, letter_matrix, s, i):
    no_other_character_inbetween = True
    for c in range(ord('a'), ord(s[i])):
        if letter_rest.get(chr(c), 0) > 0: # and other_chars_of_letter_rest_to_the_left(letter_rest, letter_matrix, chr(c), s, i):
            no_other_character_inbetween = False
    return no_other_character_inbetween and letter_rest.get(s[i], 0) > 0


def other_chars_of_letter_rest_to_the_left(letter_rest, letter_matrix, additional_except_char, s, i):
    for j in range(i-1, -1, -1):
        if s[j] == additional_except_char:
            for k, v in letter_rest.items():
                if k == s[i] and letter_matrix[j][ord(s[i])-ord('a')] < v-1:
                    return False
                elif k != s[i] and letter_matrix[j][ord(k)-ord('a')] < v:
                    return False
            return True
    return False


def create_letter_matrix(s):
    result = [[0 for i in range(26)] for i in range(len(s))]
    for i in range(len(s)):
        if i > 0:
            for j in range(26):
                result[i][j] = result[i-1][j]
        char_value = ord(s[i])-ord('a')
        result[i][char_value] += 1
    return result


def count_letters(s):
    letter_count = {}
    for c in s:
        letter_count[c] = letter_count.get(c, 0) + 1
    return letter_count


def dict_for_left_pos_in_string(s):
    letter_pos = {}
    for i in range(len(s)):
        if letter_pos.get(s[i], -1) < 0:
            letter_pos[s[i]] = i
    return letter_pos

print(reverseShuffleMerge("eggegg") == "egg")
print(reverseShuffleMerge("abcdefgabcdefg") == "agfedcb")
print(reverseShuffleMerge("abeeba") == "abe")
print(reverseShuffleMerge("aaabeeba") == "abea")
print(reverseShuffleMerge("jjcddjggcdjd") == "cgddjj")
print(reverseShuffleMerge("aahaxxxhxhxxah") == "ahhxxxa")
print(reverseShuffleMerge("bdabaceadaedaaaeaecdeadababdbeaeeacacaba") == "aaaaaabaaceededecbdb")


# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    A = []
    letter_freq = Counter(s)
    remaining_chars = dict(letter_freq)
    used_chars= defaultdict(int)

    def can_use(char):
        return letter_freq[char] // 2 - used_chars[char] > 0
    
    def can_pop(char):
        chars_needed = letter_freq[char] // 2
        return remaining_chars[char] + used_chars[char] -1 >= chars_needed

    for char in reversed(s):
        if can_use(char):
            while A and A[-1] > char and can_pop(A[-1]):
                removed_char = A.pop()
                used_chars[removed_char]-=1
                
            used_chars[char]+=1
            A.append(char)
        remaining_chars[char]-=1
    
    return ''.join(A)
        




# incorrect: aaaaaabaacceeddedebb
#            bdabaceadaedaaaeaecdeadababdbeaeeacacaba
# correct:   aaaaaabaaceededecbdb



# Complete fail
# def reverseShuffleMerge(s):
#     A = []
#     letter_count_in_s = count_letters(s)
#     letter_count_for_A = dict(
#         map(lambda kv: (kv[0], kv[1]//2), letter_count_in_s.items()))
#     letter_matrix = create_letter_matrix(s)

#     i = len(s)-1
#     while i > 0 and sum(letter_count_for_A.values()) > 0:
#         if letter_count_for_A[s[i]] == letter_count_in_s[s[i]]:
#             # critical
#             A.append(s[i])
#             letter_count_for_A[s[i]] -= 1
#         elif is_smallest_character(letter_count_for_A, letter_matrix, s, i):
#             # it's safe to take the smallest character
#             A.append(s[i])
#             letter_count_for_A[s[i]] -= 1
#         elif next_critical_character(letter_count_for_A, letter_count_in_s, s, i) > s[i]:
#             A.append(s[i])
#             letter_count_for_A[s[i]] -= 1
#         letter_count_in_s[s[i]] -= 1
#         i -= 1
#     return ''.join(A)

# def next_critical_character(letter_count_for_A, letter_count_in_s, s, index_at_s):
#     _letter_count_in_s = dict(letter_count_in_s)
#     i = index_at_s-1
#     while i >= 0:
#         if letter_count_for_A[s[i]] == _letter_count_in_s[s[i]]:
#             return s[i]
#         _letter_count_in_s[s[i]]-=1
#         i-=1
#     return 'a'

# def is_smallest_character(letter_rest, letter_matrix, s, i):
#     no_other_character_inbetween = True
#     for c in range(ord('a'), ord(s[i])):
#         if letter_rest.get(chr(c), 0) > 0: # and other_chars_of_letter_rest_to_the_left(letter_rest, letter_matrix, chr(c), s, i):
#             no_other_character_inbetween = False
#     return no_other_character_inbetween and letter_rest.get(s[i], 0) > 0


# def other_chars_of_letter_rest_to_the_left(letter_rest, letter_matrix, additional_except_char, s, i):
#     for j in range(i-1, -1, -1):
#         if s[j] == additional_except_char:
#             for k, v in letter_rest.items():
#                 if k == s[i] and letter_matrix[j][ord(s[i])-ord('a')] < v-1:
#                     return False
#                 elif k != s[i] and letter_matrix[j][ord(k)-ord('a')] < v:
#                     return False
#             return True
#     return False


# def create_letter_matrix(s):
#     result = [[0 for i in range(26)] for i in range(len(s))]
#     for i in range(len(s)):
#         if i > 0:
#             for j in range(26):
#                 result[i][j] = result[i-1][j]
#         char_value = ord(s[i])-ord('a')
#         result[i][char_value] += 1
#     return result


# def count_letters(s):
#     letter_count = {}
#     for c in s:
#         letter_count[c] = letter_count.get(c, 0) + 1
#     return letter_count


# def dict_for_left_pos_in_string(s):
#     letter_pos = {}
#     for i in range(len(s)):
#         if letter_pos.get(s[i], -1) < 0:
#             letter_pos[s[i]] = i
#     return letter_pos

# Correct copied from leaderboard
# def reverseShuffleMerge(s):
#     char_freq = Counter(s)
#     used_chars = defaultdict(int)
#     remain_chars = dict(char_freq)
#     res = []
    
#     def can_use(char):
#         return (char_freq[char] // 2 - used_chars[char]) > 0
    
#     def can_pop(char):
#         needed_chars = char_freq[char] // 2
#         return used_chars[char] + remain_chars[char] - 1 >= needed_chars
    
#     for char in reversed(s):
#         if can_use(char):
#             while res and res[-1] > char and can_pop(res[-1]):
#                 removed_char = res.pop()
#                 used_chars[removed_char] -= 1
            
#             used_chars[char] += 1
#             res.append(char)
        
#         remain_chars[char] -= 1
    
#     return "".join(res)