class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2: return 1
        if n == 3: return 2

        return self.recursive(n)
    
    def recursive(self, n):
        if n <= 4:
            return n
        return 3 * self.recursive(n - 3)