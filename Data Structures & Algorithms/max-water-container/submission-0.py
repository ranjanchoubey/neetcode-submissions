class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        max_area = 0

        # Two pointers
        left = 0
        right = n-1

        while(left < right):
            water = min(heights[left],heights[right])* (right-left)
            max_area = max(max_area,water)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
        