class Solution:
    def isPalindrome(self, x: int) -> bool:
        r = str(x)
        return r == r[::-1] 
            