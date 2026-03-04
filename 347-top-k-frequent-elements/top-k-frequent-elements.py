class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        unique = {}
        for i in nums:
            if i in unique.keys():
                unique[i] = unique.get(i) + 1
            else:
                unique[i] = 1

        result = []
        for i in enumerate(range(k)):
            key = max(unique, key=unique.get)
            unique.pop(key)
            result.append(key)
        
        return result