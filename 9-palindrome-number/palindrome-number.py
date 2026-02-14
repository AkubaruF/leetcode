class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        string = str(x)
        for i in range(len(string)):
            if string[i] == string[len(string) - i - 1]:
                continue
            else:
                return False
        return True
        