from typing import List

class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        #cleaner
        right_sum = 0
        for n in nums:
            right_sum += n # is equivalent of `sum(nums)`

        left_sum = 0
        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1

        #my submission
        from_right_prefix_sums = []
        
        left_prefix = right_prefix = 0
        nums_length = len(nums)

        for i in range(nums_length - 1, -1, -1):
            from_right_prefix_sums.append(right_prefix)
            right_prefix += nums[i]
            
        print(from_right_prefix_sums)

        for i in range(nums_length):
            print(f'is (left_prefix[{i}]){left_prefix} == {from_right_prefix_sums[-i-1]} (right_prefix[{-i-1}])')
            if left_prefix == from_right_prefix_sums[-i-1]:
                return i
            
            left_prefix += nums[i]
            
        return -1
        
sol = Solution()
print(sol.pivotIndex([1,7,3,6,5,6]))
print(sol.pivotIndex([-1,-1,0,1,0,-1]))