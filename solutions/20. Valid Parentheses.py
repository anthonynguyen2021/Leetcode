class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        leftDictionary = {']': '[', ')': '(', '}':'{'}
        for char in s:
            if char not in leftDictionary:  # char is a left bracket
                stack.append(char)
            else:  # we have a right bracket
                if not stack or leftDictionary[char] != stack[-1]:  # invalid case
                    return False
                else:
                    stack.pop()  # remove the top of the stack
        return stack == []
                    
                    
