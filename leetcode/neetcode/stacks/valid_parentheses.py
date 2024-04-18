class Solution:
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    def isValid(self, s: str) -> bool:
        #my solution
        stack = []
                #cleaner solution
        for char in s:
            if char in Solution.brackets:                    
                if stack and stack[-1] == Solution.brackets[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
    
        result = False
        last_bracket = None
        for char in s:
            if char in Solution.brackets:
                if len(stack) == 0:
                    return result
                last_bracket = stack.pop()
                valid_bracket = Solution.brackets[char]
                if last_bracket != valid_bracket:
                    return result
            else:
                stack.append(char)
        if len(stack) == 0:
            result = True
        return result
    
sol = Solution()
print(sol.isValid("()[]{}"))