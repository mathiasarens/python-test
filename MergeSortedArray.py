class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        while i<m+n and j<n:
            if nums1[i] >= nums2[j] and nums1[i] >= nums1[0]:
                for k in range(m+n-1, i, -1):
                    nums1[k] = nums1[k-1]
                nums1[i] = nums2[j]  
                i+=1
                j+=1
            elif nums1[i] < nums2[j] and m+n-i > n-j:
                i+=1
            else:
                nums1[i] = nums2[j]  
                i+=1
                j+=1
            

solution = Solution()
# arr1 = [1,2,3,0,0,0]
# arr2 = [2,5,6]
# solution.merge(arr1,3,arr2,3)
# arr1 = [4,5,6,0,0,0]
# arr2 = [1,2,3]
# solution.merge(arr1,3,arr2,3)
arr1 = [0,0,0,0,0,0]
arr2 = [1,2,3]
solution.merge(arr1,3,arr2,3)
print(arr1)