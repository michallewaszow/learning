from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        unique = defaultdict(list)

           
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            unique[tuple(count)].append(word)
        return list(unique.values())

        for word in strs:
            sorted_w = ''.join(sorted(word))
            unique[sorted_w].append(word)
        return list(unique.values())
    
solution = Solution()
actual = solution.groupAnagrams(['eat', 'tae', 'bla', 'alb', 'dec'])
print(actual)