from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        for val in nums[:-1]:
            ans.append(ans[-1] * val)
        prev = nums[-1]
        for index in range(len(nums) - 2, -1, -1):
            ans[index] = prev * ans[index]
            prev *= nums[index]
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = list(map(int, input('Enter the Numbers: ').split(',')))
    answer = solution.productExceptSelf(nums=nums)
    print(answer)
    