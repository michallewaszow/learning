from typing import List

class Solution:
    """
    Design:
        (string length + # + actual_string) + (string length + # + actual_string) + ...
    """

    def encode(self, strs: List[str]) -> str:
        output = ''
        if len(strs) > 0:
            for s in strs:
                output += f"{len(s)}#{s}"
            return output
        else:
            return None

    def cleaner_decode(self, s: str) -> List[str]:
        if s is None:
            return []
        i, output = 0, []
        while i < len(s):
            start = i
            while s[i] != "#":
                i += 1
            length = int(s[start:i])
            output.append(s[i+1:i+1+length])
            i = i + 1 + length
        return output

    def decode(self, s: str) -> List[str]:
        if s is None:
            return []
        word_len = ''
        output = []
        i = 0
        while i < len(s):
            char = s[i]
            if char == '#':
                start = i+1
                end = start+int(word_len)
                output.append(s[start:end])
                i = end
                word_len = ''
            else:
                word_len = word_len + char
                i += 1
        return output
            
            
        
    
sol = Solution()
encoded = sol.encode(['mordo', 'jak', 'tam'])
print(encoded)
print(sol.cleaner_decode(encoded))
