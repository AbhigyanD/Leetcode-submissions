class Solution:
    def findMin(self, nums: List[int]) -> int:
        a = 0
        b = len(nums)-1
        while a < b:
            m = a + (b-a) // 2
            if nums[m] < nums[b]:
                b = m
            else:
                a = m + 1
        return nums[a]