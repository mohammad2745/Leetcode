class Solution:
    def findMin(self, nums: List[int]) -> int:
        length=len(nums)
        begin=0
        end=length-1
        while nums[begin]>nums[end]:
            mid=begin+(end-begin)//2
            if nums[mid]>nums[begin]: 
                begin=mid+1
            elif nums[mid]<nums[begin]: 
                end=mid
            else : 
                return nums[end]
        
        return nums[begin]