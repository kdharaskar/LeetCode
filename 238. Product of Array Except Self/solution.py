class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        for i, num in enumerate(nums):
            res.append(product)
            product *= num
        product = 1
        for i in reversed(range(len(res))):
            res[i] *= product
            product *= nums[i]
        return res
