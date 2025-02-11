class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sl, tl = [0] * 26, [0] * 26
        for char in s:
            sl[ord(char) - ord('a')] += 1
        for char in t:
            tl[ord(char) - ord('a')] += 1
        return sl == tl