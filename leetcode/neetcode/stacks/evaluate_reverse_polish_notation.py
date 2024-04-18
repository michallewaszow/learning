from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                result = operators[t](a, b)
                stack.append(result)
        return stack[0]
    
sol = Solution()
print(sol.evalRPN(["2","1","+","3","*"]))
print(sol.evalRPN(["4","13","5","/","+"]))
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))