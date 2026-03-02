class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        length = len(nums) - 1

        while i <= length:
            middle = (i + length) // 2

            if nums[middle] < target:
                i = middle + 1
            elif nums[middle] > target:
                length = middle - 1
            elif nums[middle] == target:
                return middle
                
        return i