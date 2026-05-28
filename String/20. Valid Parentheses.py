class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if s[i] in [')','}',']']:
                if stack and stack[-1]+s[i] in ['()','{}','[]']:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(s[i])

        if len(stack)==0:
            return True 
        return False

        
