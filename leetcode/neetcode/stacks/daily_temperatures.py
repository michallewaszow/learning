from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] # pair: [temp, index]
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_i = stack.pop()
                output[stack_i] = (i - stack_i)
            stack.append([temp, i])
        return output
    
sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))