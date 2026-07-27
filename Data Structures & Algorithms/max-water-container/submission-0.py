class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxArea =0
        while left < right:
            min_height = min(heights[left],heights[right])
            width = right -left
            currentArea = min_height * width
            maxArea = max(currentArea,maxArea)
            if heights[left]<heights[right]:
                left+=1
            else:
                right -=1
        return maxArea

        