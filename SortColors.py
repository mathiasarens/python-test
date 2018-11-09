class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def swap(i,j):
            buffer = nums[j]
            nums[j] = nums[i]
            nums[i] = buffer
        
        if len(nums)<1:
            return
        pos_0=0
        pos_2=len(nums)-1
        i = 0
        j = len(nums)-1
        while i < j:
            while nums[pos_0]==0 and pos_0 < len(nums)-1:
                pos_0+=1
            while nums[pos_2]==2 and pos_2 > 0:
                pos_2-=1
            i = max(pos_0, i)
            j = min(pos_2, j)
            if nums[i] == 2 and i <= j:
                swap(i,pos_2)
                pos_2-=1
            elif nums[i] == 0 and i <= j:
                swap(i,pos_0)
                pos_0+=1
            elif nums[j] == 0 and i <= j:
                swap(pos_0,j)
                pos_0+=1
            else:
                i+=1
                

solution = Solution()

def sort_colors(arr):
    solution.sortColors(arr)
    print(arr)

sort_colors([2,1,2])
sort_colors([])
sort_colors([0])
sort_colors([1])
sort_colors([2])
sort_colors([2,2])
sort_colors([2,1])
sort_colors([2,0])
sort_colors([2,0,1])
sort_colors([1,2,0])
sort_colors([1,0,2])
sort_colors([0,1,2])
sort_colors([0,2,2])
sort_colors([0,1,1,2])
sort_colors([2,2,0,0])
sort_colors([1,1,0,0])
sort_colors([0,2,2,2,0,2,1,1])

