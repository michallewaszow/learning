from timeit import timeit

class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # from LeetCode solutions
        covered_map = {}
        for i, n in enumerate(nums):
            searched = target - n
            found = covered_map.get(searched)
            if found:
                return [i, found]
            covered_map[searched] = i

        for first_index in range(len(nums) - 1, -1, -1):
            last = nums.pop(first_index)
            for second_index, other in enumerate(nums):
                if last + other == target:
                    return [second_index, first_index]
        return []


solution = Solution()
assert solution.twoSum([2, 7, 11, 15], 9) == ([0, 1] or [1, 0])
