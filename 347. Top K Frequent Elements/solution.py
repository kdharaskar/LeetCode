class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = Counter(nums)
        for i in range(k):
            key = max(freq, key=freq.get)
            res.append(key)
            del(freq[key])
        return res