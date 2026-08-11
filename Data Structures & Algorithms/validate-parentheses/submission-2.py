
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {'(', '[', '{'}
        matching = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in opening:
                stack.append(char)
            elif char in matching:
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()
        return len(stack) == 0