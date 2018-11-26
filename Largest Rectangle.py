# Complete the largestRectangle function below.
def largestRectangle(h):
    stack = []
    max_r = 0
    for i in range(len(h)):
        if stack and h[i] < stack[0][0]:
            last_pos = 0
            while stack and stack[0][0] >= h[i]:
                stack_item = stack.pop(0)
                last_pos=stack_item[1]
                max_r = max(max_r, stack_item[0] * (i - stack_item[1]))
            stack.insert(0, (h[i], last_pos))   
        elif not stack or h[i] > stack[0][0]:
            stack.insert(0, (h[i],i))
            
    while stack:
        stack_item = stack.pop(0)
        max_r = max(max_r, stack_item[0] * (len(h) - stack_item[1]))
    return max_r

print(largestRectangle([1,2,3,4,5])==9)
print(largestRectangle([1,3,5,9,11])==18)
print(largestRectangle([11,11,10,10,10])==50)
print(largestRectangle([5,4,3,2,1])==9)
print(largestRectangle([1,5,1,1])==5)
print(largestRectangle([1,5,1,1,1,1])==6)
print(largestRectangle([1,1,1,1,2,3,4,5])==9)
print(largestRectangle([1,1,1,1,1,1,2,3,4,5])==10)
print(largestRectangle([1,15,1,1,1,1,2,3,4,5])==15)
print(largestRectangle([])==0)
print(largestRectangle([4])==4)
print(largestRectangle([5,3,9,8,3])==16)
print(largestRectangle([5,3,7,7,3])==15)