class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        parantheses_map = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        for i in s:
            if i in "[{(":
                stack.append(i)

            elif i in ")}]" :
                if not stack:
                    return False
                if parantheses_map[i] != stack.pop():
                    return False
                
        return len(stack) == 0

