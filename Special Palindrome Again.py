# Complete the substrCount function below.
def substrCount(s):
    count = 0
    for i in range(len(s)):
        count += palindromes(s, i, i)
        count += palindromes(s, i, i+1)
    return count

def palindromes(s, pos, pos_next):
    count = 0
    while pos >= 0 and pos_next < len(s) and s[pos] == s[pos_next] and ((count > 1 and s[pos] == s[pos+1]) or count < 1 or (count == 1 and s[pos] == s[pos+2])):
        count += 1
        pos -= 1
        pos_next+=1
    return count

# print(substrCount("m")==1)
# print(substrCount("mnonopoo")==12)
# print(substrCount("asasd")==7)
# print(substrCount("abcbaba")==10)
# print(substrCount("aaaa")==10)
# print(substrCount("aba")==4)
# print(substrCount("abba")==5)
# print(substrCount("aabbaa")==9)

if __name__ == '__main__':
    fptr = open('Special Palindrome Again-TestCase2.txt', 'r')
    n = int(fptr.readline())
    s = fptr.readline()
    result = substrCount(s)
    print(result == 1272919)
    print(result)
    fptr.close()


