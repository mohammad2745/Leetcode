class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ = 0
        runningSum = []
        for i in range(0, len(nums)):
            summ += nums[i]
            runningSum.append(summ)
        return runningSum