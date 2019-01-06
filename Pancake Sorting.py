class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = []
        sorted = False
        while not sorted:
            flip = False
            for i in range(len(A)-1, 0, -1):
                if A[i-1] > A[i]:
                    maximum = A[i-1]
                    maximum_pos = i-1
                    for j in range(i-1, -1, -1):
                        if A[j] > maximum:
                            maximum = A[j]
                            maximum_pos = j
                    if maximum_pos == 0:
                        k = len(A)-1
                        while  k > 0:
                            if A[k] < A[0]:
                                break
                            k-=1
                        A = self.flip(A, k)
                        ans.append(k+1)
                    elif maximum_pos >= len(A)//2 and A[0] > A[i]:
                        A = self.flip(A, i)
                        ans.append(i+1)
                    else:
                        A = self.flip(A, maximum_pos)
                        ans.append(maximum_pos+1)
                    flip = True
                    break
            if not flip:
                sorted = True
        return ans

    def flip(self, A, i):
        return list(reversed(A[:i+1]))+A[i+1:]


solution = Solution()
print(solution.pancakeSort([3,2,4,1])==[4,2,4,3])
print(solution.pancakeSort([1,2,3])==[])
print(solution.pancakeSort([1])==[])
print(solution.pancakeSort([2,1])==[2])
print(solution.pancakeSort([3,2,1])==[3])
print(solution.pancakeSort([1,3,2])==[2,3,2])
print(solution.pancakeSort([1, 2, 4, 3])== [3,4,3,2])

132
312
213
123

132
231
321
123

# 3241
# 1423
# 4123
# 3214


# 3241
# 4231
# 1324
# 3124
# 2134
# 1234


# 1243
# 3421
# 4321
# 1234

# 1243
# 4213
# 3124
# 2134
# 1234

# 54321

# 23451
# 15432
# 51432
# 23415
# 43215
# 12345

# 23451
# 54321
# 12345

# 32541
# 52341
# 14325
# 41325
# 23145
# 32145
# 12345

# 32541
# 14523
# 54123
# 32145
# 12345

# 41532
# 51432
# 23415
# 43215
# 12345

# 41532
# 23514
# 53214
# 41235
# 32145
# 12345

# 45321
# 54321
# 12345

# 34521
# 54321
# 12345

# 34521
# 12543
# 52143
# 34125
# 43125
# 21345
# 12345

# 43215
# 12345

# 53214
# 41235
# 32145
# 12345

# 35214

# 45213
# 54213
# 31245
# 12345

# 45213
# 31254