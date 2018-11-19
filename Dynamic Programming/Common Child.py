# Complete the commonChild function below.
def commonChild(s1, s2):
    dp = [[0 for i in range(len(s2)+1)] for i in range(len(s1)+1)]
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[len(s1)][len(s2)]

print(commonChild("HARRY","SALLY")==2)
print(commonChild("AA", "BB")==0)
print(commonChild("SHINCHAN", "NOHARAAA")==3)
print(commonChild("ABCDEF", "FBDAMN")==2)
print(commonChild("ABCDEF", "FBDAMN")==2)
print(commonChild("ABCDEFERSGDSFAG", "FBDAMNSDFWERSSF")==8)


# solution
# end characters equal
# L(s1(0,..n-1), s2(0,...,m-1)) = 1+ L(s1(0,..n-2), s2(0,...,m-2))
#
# end characters not equal
# L(s1(0,..n-1), s2(0,...,m-1)) = MAX(L(s1(0,..n-2), s2(0,...,m-1), L(s1(0,..n-1), s2(0,...,m-2))

def commonChildRecursiveSlow(s1, s2):
    return LCSRecursive(s1,s2,len(s1),len(s2),0)

def LCSRecursive(s1, s2, end1, end2, count):
    if end1 > 0 and end2 > 0:
        if s1[end1-1] == s2[end2-1]:
            return LCSRecursive(s1, s2, end1-1,end2-1, count+1)
        else:
            return max(LCSRecursive(s1, s2, end1-1, end2, count), LCSRecursive(s1,s2,end1,end2-1, count))
    else:
        return count

# print(commonChildRecursiveSlow("ABCDEFERSGDSFAG", "FBDAMNSDFWERSSF"))