class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        seen = set()
        dup = -1

        for n in nums:
            if n in seen:
                dup = n
            seen.add(n)

        for i in range(1, len(nums) + 1):
            if i not in seen:
                missing = i
                break
        return [dup, missing]