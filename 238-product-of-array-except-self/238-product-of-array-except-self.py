class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        flag = 1
        for i in range(0, len(nums)):
            flag *= nums[i]
            left.append(flag)
            
        flag = 1
        for i in range(len(nums)-1, -1, -1):
            flag *= nums[i]
            right.append(flag)
        
        right.reverse()
            
        for i in range(len(nums)):
            if i==0:
                nums[i] = 1 * right[i+1]
            elif i == len(nums)-1:
                nums[i] = left[i-1] * 1
            else:
                nums[i] = left[i-1] * right[i+1]
        
        return nums
            