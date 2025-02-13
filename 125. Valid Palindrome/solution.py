class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.is_valid(s[l]):
                l += 1
            while l < r and not self.is_valid(s[r]):
                r -= 1
            if l < r and s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                break
        return l >= r
    
    def is_valid(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))