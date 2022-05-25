class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        while n:
            flag = n%10
            p *= flag
            s += flag
            n = n // 10
        return p-s