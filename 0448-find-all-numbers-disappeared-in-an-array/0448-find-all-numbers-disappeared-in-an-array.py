class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        set_nums = set(nums)
        miss = []
        for i in range(1, len(nums)+1):
            if i not in set_nums:
                miss.append(i)
        return miss
            
        