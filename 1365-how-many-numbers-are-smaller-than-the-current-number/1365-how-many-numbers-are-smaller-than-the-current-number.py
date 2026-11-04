class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sort_nums = sorted(nums)
        d = {}
        res = []
        for i, j in enumerate(sort_nums):
            if j not in d:
                d[j] = i
        for j in nums:
            res.append(d[j])
        return res