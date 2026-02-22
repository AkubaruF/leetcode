class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1
            
        for i, j in enumerate(haystack):
            if needle == haystack[i: i + len(needle)]:
                return i
        return -1