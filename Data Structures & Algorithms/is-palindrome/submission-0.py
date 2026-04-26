class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n-1

        s = s.upper()

        while left < right:
            if not self.isAlphanumeric(s[left]):
                left += 1
                continue
            if not self.isAlphanumeric(s[right]):
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    def isAlphanumeric(self, s: str) -> bool:
        if ord(s) >= ord("A") and ord(s) <= ord("Z"):
            return True
        if ord(s) >= ord("0") and ord(s) <= ord("9"):
            return True
        return False

