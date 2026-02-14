class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lowest = min(strs, key=len)
        for i in range(len(lowest)):
            for j in strs:
                if j[i] != lowest[i]:
                    return lowest[:i]
        return lowest
