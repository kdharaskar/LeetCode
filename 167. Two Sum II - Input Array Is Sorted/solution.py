class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r  = 0, len(numbers) - 1
        while l < r:
            addition = numbers[l] + numbers[r]
            if addition < target:
                l += 1
            elif addition > target:
                r -= 1
            else:
                return [l + 1, r + 1]