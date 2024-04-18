class Solution(object):
    def count_letters(self, word):
        letters_count = {}
        for char in word:
            if char in letters_count:
                letters_count[char] += 1
            else:
                letters_count[char] = 1
        return letters_count

    def is_in_target(self, c, letters_map):
        if c in letters_map:
            print(f'{c} in map')
            return True
        else:
            print(f'{c} NOT in map')
            return False

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        original_letters_count = self.count_letters(s)
        print(original_letters_count)
        target_letters_count = self.count_letters(t)
        print(target_letters_count)

        if len(s) != len(t):
            return False

        for c in original_letters_count:
            if self.is_in_target(c, target_letters_count):
                if original_letters_count[c] == target_letters_count[c]:
                    pass
                else:
                    return False
            else:
                return False
        return True

solution = Solution()

solution.isAnagram('a', 'ab')