from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sum_val = 0
        for n in self.nums[left:right+1]:
            sum_val += n
        return sum_val
    
    # more efficient solution with prefix sums (cumulative sums for precalculation)
    # 1 2 3  4  5  6 <- nums
    # 1 3 6 10 15 21 <- prefixes 
    # sum of [1:3] = prefix[3] - prefix[1-1](sum of all previous nums)

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sums = []
        curr_sum = 0
        for n in nums:
            curr_sum += n
            self.prefix_sums.append(curr_sum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sums[right]
        return self.prefix_sums[right] - self.prefix_sums[left-1]
        # return self.prefix_sums[right] - self.prefix_sums[left-1] if left != 0 else self.prefix_sums[right
        #right = self.prefix_sums[right]
        #left = self.prefix_sums[left - 1] if left > 0 else 0

# Your NumArray object will be instantiated and called as such:
obj = NumArray([1, 2, 3, 4, 5, 6])
param_1 = obj.sumRange(1,3)
print(param_1)
param_2 = obj.sumRange(0,3)
print(param_2)