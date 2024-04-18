class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        could be achieved with sorted array but it's quicker
        to check if current number is "start of the sequence", 
        for 1, 2, 3, 4, 100, 200 only 1, 100 and 200 are "start of sequence"
        '''
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                length = 0
                while (num + length) in nums:
                    length += 1
                longest = max(length, longest)
        return longest

s = Solution()
print(s.longestConsecutive([1, 5, 100, 6, 49, 7, 101, 102, 103]))