class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = False
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                found = True
                break
            elif  nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return mid if found else -1