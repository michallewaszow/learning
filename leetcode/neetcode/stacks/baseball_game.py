from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        total_sum = 0 
        value = 0
        for operation in operations:
            if operation == 'C':
                value = -record.pop()
            elif operation == 'D':
                value = record[-1] * 2
                record.append(value)
            elif operation == '+':
                value = record[-1] + record[-2]
                record.append(value)
            else:
                value = int(operation)
                record.append(value)
            total_sum += value
        return total_sum

sol = Solution()
print(sol.calPoints(["5","2","C","D","+"]))