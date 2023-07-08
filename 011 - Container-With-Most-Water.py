"""
Link - https://leetcode.com/problems/container-with-most-water/
"""
from typing import List


# Solution:

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0

        while left < right:
            cur = min(height[left], height[right])
            cur *= (right-left)
            ans = max(cur, ans)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return ans


if __name__ == '__main__':
    solution = Solution()
    heights = list(map(int, input('Enter the Heights: ').split(',')))
    answer = solution.maxArea(height=heights)
    print(answer)
