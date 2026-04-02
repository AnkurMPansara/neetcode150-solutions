class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefix_product = []
        for num in nums:
            prefix_product.append(product)
            product *= num
        product = 1
        postfix_proudct = []
        for num in nums[::-1]:
            postfix_proudct.append(product)
            product *= num
        postfix_proudct = postfix_proudct[::-1]
        ans = []
        for i in range(len(nums)):
            ans.append(prefix_product[i]*postfix_proudct[i])
        return ans
        