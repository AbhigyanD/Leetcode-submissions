class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_a = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack [-1][1] > h:
                index, height = stack.pop()

                max_a = max(max_a, height*(i-index))
                start = index
            stack.append((start,h))

        for i, h in stack:
            max_a = max(max_a, h*(len(heights)-i))
        return max_a