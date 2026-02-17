class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1

        counter = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[counter] = nums[i]
                counter += 1
        return counter