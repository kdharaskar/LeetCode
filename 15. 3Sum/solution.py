class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()
        for index, num in enumerate(nums):
            l, r = index + 1, len(nums) - 1
            target = 0 - num
            while l < r:
                if l == index:
                    l += 1
                if r == index:
                    r -= 1
                s = nums[l] + nums[r]
                if target == s:
                    if (nums[l], nums[r], num) not in output:
                        output.add((nums[l], nums[r], num))
                    l += 1
                    r -= 1
                elif target > s:
                    l += 1
                else:
                    r -= 1
                if l == index:
                    l += 1
                if r == index:
                    r -= 1
        
        return [list(t) for t in output]