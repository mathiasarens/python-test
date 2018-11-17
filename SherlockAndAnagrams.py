from collections import Counter

def sherlockAndAnagrams(string):
    buckets = {}
    for i in range(len(string)):
        for j in range(1, len(string) - i + 1):
            key = frozenset(Counter(string[i:i+j]).items()) # O(N) time key extract
            buckets[key] = buckets.get(key, 0) + 1
    count = 0
    for key in buckets:
        count += buckets[key] * (buckets[key]-1) // 2
    return count

print(sherlockAndAnagrams("a")==0)
print(sherlockAndAnagrams("ab")==0)
print(sherlockAndAnagrams("abb")==1)
print(sherlockAndAnagrams("abba")==4)
print(sherlockAndAnagrams("abcd")==0)
print(sherlockAndAnagrams("kkkk")==10)
print(sherlockAndAnagrams("ifailuhkqq")==3)
print(sherlockAndAnagrams("cdcd")==5)
print(sherlockAndAnagrams("cd")==0)
print(sherlockAndAnagrams("cdc")==2)
print(sherlockAndAnagrams("cdcd")==5)
print(sherlockAndAnagrams("cdcdc")==12)
print(sherlockAndAnagrams("c")==0)
print(sherlockAndAnagrams("cc")==1)
print(sherlockAndAnagrams("ccc")==4)
print(sherlockAndAnagrams("cccc")==10)
print(sherlockAndAnagrams("ccccc")==20)

####################################################
# Brute force in O(N^3)
#
# def sherlockAndAnagrams(s):
#     substring_dict = {}
#     for substring_length in range(1,len(s)+1):
#         for pos in range(len(s)-substring_length+1):
#             substring = s[pos:pos+substring_length]
#             hash_value = calculateHash(substring)
#             if hash_value in substring_dict:
#                 substring_dict[hash_value]+=1
#             else:
#                 substring_dict[hash_value]=1
#     count = 0
#     for k,v in substring_dict.items():
#         count+=v * (v-1) //2
#     return count

# def calculateHash(substring):
#     hash_value = 0
#     for char in substring:
#         number = ord(char)-ord('a')
#         hash_value+=pow(26, number)
#     return hash_value

###################################################
#
# Brute force O(n^4) too slow
#
# def sherlockAndAnagrams(s):
#     count = 0
#     for substring_length in range(1,len(s)):
#         for pos in range(len(s)-substring_length+1):
#             string_to_find = s[pos:pos+substring_length]
#             for j in range(len(s)-substring_length+1):
#                 if j != pos and isAnagram(string_to_find, s[j:j+substring_length]):
#                     count+=1
#     return count//2

# def isAnagram(str1,str2):
#     char_str1 = defaultdict(int)
#     char_str2 = defaultdict(int)
#     for c in str1:
#         char_str1[c]+=1

#     for c in str2:
#         char_str2[c]+=1
    
#     if len(char_str1) == len(char_str2):
#         for k,v in char_str1.items():
#             if char_str2[k] != v:
#                 return False
#         return True
#     return False        

