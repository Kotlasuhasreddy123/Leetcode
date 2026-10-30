class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = (n*(n+1)//2)
        sum_1 = 0
        for i in range(1,n+1):
            sum_1 += i
            if total_sum - sum_1 + i == sum_1:
                return i
        return -1
