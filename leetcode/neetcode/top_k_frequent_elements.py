from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) <= k:
            return nums
        counted = {}
        for n in nums:
            counted[n] = counted.get(n, 0) + 1

        sorted_freq = [[] for i in range(len(nums)+1)] ## bucket sort algorithm
        for n, c in counted.items():
            sorted_freq[c].append(n)

        top_k = []
        for ordered in sorted_freq[::-1]:
            for o in ordered:
                top_k.append(o)
                if len(top_k) == k:
                    return top_k
            

        top_k = {}
        for num, count in list(counted.items())[k:]:
            for i, topk_n, topk_c in enumerate(top_k):
                if count > topk_c:
                    top_k[i] = (num, count)

        sorted_by_count = sorted([(count, num) for num, count in counted.items()], reverse=True)
        return [num for _, num in sorted_by_count[:k]]

        top_k = {n: c for n, c in list(counted.items())[:k]}
        for num, count in list(counted.items())[k:]:
            for top_k_num, top_k_count in top_k.items():
                if count > top_k_count:
                    top_k.pop(top_k_num)
                    top_k[num] = count
                    break
        return list(top_k.keys())

sol = Solution()
print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(sol.topKFrequent([1], 1))
print(sol.topKFrequent([4,1,-1,2,-1,2,3], 2))
            