class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        digits = set([str(i) for i in range(10)])

        def is_integer(s,sign=False):
            # handle optional sign if sign=True
            if sign and s and s[0] in ['+','-']:
                s = s[1:]
            # there should be only digits
            if not s: return False
            for x in s:
                if x not in digits:
                    return False
            return True

        def is_decimal(s):
            if s and s[0] in ['-','+']: s=s[1:] # optional sign
            n = len(s)
            if n==0: return False
            elif is_integer(s): return True # s in an integer
            elif s[n-1]=="." and is_integer(s[:n-1]): return True # digits followed by dot
            elif s[0]=="." and is_integer(s[1:]): return True # dot followed by digits
            for i in range(n):  # digits followed by dots followed by digts
                if s[i]=="." and is_integer(s[:i]) and is_integer(s[i+1:]):
                    return True
            return False
        
        if is_decimal(s): return True # decimal
        for i in range(len(s)):
            if s[i] in ['e','E']: # decimal followed by exponent
                if is_decimal(s[:i]) and is_integer(s[i+1:],sign=True): return True
                else: return False

        return False

  # Time complexity O(n) , space complexity O(1)
