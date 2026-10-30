class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:

        arr.sort()
        d = arr[1] - arr[0]
        for i in range(1, len(arr) -1):
            if arr[i] + d != arr[i+1]:
                return False
        return True 