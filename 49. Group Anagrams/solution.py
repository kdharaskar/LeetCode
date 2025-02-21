class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            l = [0] * 26
            for char in s:
                l[ord(char) - ord('a')] += 1
            anagram = tuple(l)
            anagrams.setdefault(anagram, []).append(s)
        return list(anagrams.values())