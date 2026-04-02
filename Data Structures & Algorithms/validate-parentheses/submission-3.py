class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)
            else:
                if stack:
                    if c == ']':
                        if stack[-1] == '[':
                            stack.pop()
                        else:
                            return False
                    elif c == '}':
                        if stack[-1] == '{':
                            stack.pop()
                        else:
                            return False
                    elif c == ')':
                        if stack[-1] == '(':
                            stack.pop()
                        else:
                            return False
                else:
                    return False
        if len(stack) == 0:
            return True
        return False