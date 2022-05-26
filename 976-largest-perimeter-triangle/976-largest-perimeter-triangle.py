class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        peri = 0
        nums.sort(reverse=True)
        for i in range(0, len(nums)-2):
            if nums[i]<(nums[i+1]+nums[i+2]) and nums[i+1]<(nums[i]+nums[i+2]) and nums[i+2]<(nums[i+1]+nums[i]):
                peri = nums[i] + nums[i+1] + nums[i+2]
                break
        
        return peri