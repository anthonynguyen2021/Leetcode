class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x > 2 ** 31 - 1:
            return False
        strNum = str(x)
        left = 0
        right = len(strNum)-1
        while left < right:
            if strNum[left] != strNum[right]:
                return False
            left += 1
            right -= 1
        return True 
