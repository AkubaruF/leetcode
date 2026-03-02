class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0

        isNegative = x < 0

        x = abs(x)
        while x != 0:
            result = (result * 10) + x % 10
            x = x // 10
        
        if result < -2**31 or result > 2**31 - 1:
            return 0

        if isNegative:
            return result * -1
        return result
