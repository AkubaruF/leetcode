class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        biggest = 0
        for i in range(len(height)):
            area = min(height[left],height[right]) * (right - left)
            if area > biggest:
                biggest = area
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return biggest