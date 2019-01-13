# https://www.hackerrank.com/contests/saggezza-coding-test/challenges/the-birthday-bar
def birthday(s, d, m):
    ans = 0
    for i in range(len(s)):
        rest_d = d
        rest_m = m
        j = i
        while j < len(s) and rest_d > 0 and rest_m > 0:
            rest_d -= s[j]
            rest_m -= 1
            j += 1
        if rest_d == 0 and rest_m == 0:
            ans += 1
    return ans


print(birthday([1, 2, 1, 3, 2], 3, 2) == 2)
print(birthday([1, 1, 1, 1, 1, 1], 3, 2) == 0)
print(birthday([1, 1, 1, 1, 1, 1], 3, 3) == 4)
print(birthday([4], 4, 1) == 1)
