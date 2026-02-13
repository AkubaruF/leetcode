class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}
        for i in nums:
            pair = target - i
            if pair in result:
                return [result[pair], nums.index(i, nums.index(pair) + 1)]
            result[i] = nums.index(i)