class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = (high - low)//2
        if high%2 != 0 and low%2 != 0:
            count += 1
        elif high%2 == 0 and low%2 == 0:
            count = (high - low)//2
        else:
            count += 1
        return count
    
        