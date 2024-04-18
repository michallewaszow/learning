from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # O(n) time
        current_sum = 0
        prefix_sums_count = {0: 1}
        res = 0

        for n in nums:
            current_sum += n
            diff = current_sum - k
            
            res += prefix_sums_count.get(diff, 0)
            prefix_sums_count[current_sum] = 1 + prefix_sums_count.get(current_sum, 0)
            
        return res
    
        #brute force (wrong)
        prefix = 0
        prefixes = [prefix]
        subarrays_count = 0
        for main in range(len(nums)):
            prefix += nums[main]
            prefixes.append(prefix)
            for comparing in range(len(prefixes) - 2, -1, -1):
                if prefix - prefixes[comparing] == k:
                    subarrays_count += 1
        return subarrays_count
    
sol = Solution()
print(sol.subarraySum([1,1,1], 2))
