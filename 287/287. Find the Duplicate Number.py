class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        def sol(nums):
            l, h = 1, len(nums) - 1
            while l < h:
                m = (l + h) // 2
                c = sum(1 for x in nums if x <= m)
                if c > m:
                    h = m
                else:
                    l = m + 1
            return l
        return sol(nums)
        