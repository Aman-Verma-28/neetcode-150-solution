from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        bucket = [[] for i in range(len(nums) + 1)]
        # print(bucket)
        for key, val in counter.items():
            bucket[val].append(key)

        index = len(nums)
        ans = []
        while index >= 0:
            if bucket[index]:
                ans.extend(bucket[index])
            if len(ans) >= k:
                break
            index -= 1

        return ans


solution = Solution()
nums = list(map(int, input('Enter the Numbers: ').split(',')))
k = int(input('Enter the value of k: '))
answer = solution.topKFrequent(nums=nums, k=k)
print(answer)
