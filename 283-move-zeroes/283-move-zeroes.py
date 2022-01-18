class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        i=0
        while i<len(nums):
            if nums[i]==0:
                count+=1 
                nums.pop(i)
            else:
                i+=1 

        x=[0]*count
        nums[:]=nums+x
        return nums
        