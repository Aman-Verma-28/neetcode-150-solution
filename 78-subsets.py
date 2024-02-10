class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def findSubsets(nums, index, cur, ans):
            if index == len(nums):
                ans.append(cur)
                return
            
            # Not pick
            findSubsets(nums, index+1, cur, ans)
            # Pick
            findSubsets(nums, index+1, cur+[nums[index]], ans)

        ans = []
        findSubsets(nums, 0, [], ans)

        return ans