class Solution(object):
    @staticmethod
    def calculate_product_iteratively(nums):
        prev_val = None
        products = []
        for num in nums:
            if prev_val is None:
                product = num
                products.append(num)
            else:
                product = num * prev_val
                products.append(product)
            prev_val = product
        return products
    
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # best solution
        ''' 
                         input 1, 2, 3, 4
        prefix(prefix*nums[i]) 1, 1, 2, 6
        
        postfix (going in reverse)
                            input 1,  2,  3, 4
                           prefix 1,  1,  2, 6
        postfix(postfix*nums[i]) 24, 24, 12, 4
        output(postfix*prefix)   24, 12,  8, 6
        ''' 
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

        # original solution
        from_left = Solution.calculate_product_iteratively(nums)
        from_right = list(reversed(Solution.calculate_product_iteratively(reversed(nums))))
        product_except_self = []
        for i in range(0, len(nums)):
            if i == 0:
                product_except_self.append(from_right[i+1])
            elif i == len(nums) - 1:
                product_except_self.append(from_left[i-1])
            else:
                product_except_self.append(from_left[i-1] * from_right[i+1])
        return product_except_self
