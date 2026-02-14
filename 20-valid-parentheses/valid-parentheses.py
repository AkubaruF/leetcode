class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        stack = []
        
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if not stack or brackets[stack[-1]] != i:
                    return False
                stack.pop()

        if len(stack) != 0:
            return False
        return True
            
        