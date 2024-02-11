class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        def findCombinationSum(candidates, target, index, cur, ans):
            if index == len(candidates) - 1:
                if target == candidates[index]:
                    ans.append(cur+[candidates[index]])
                return 

            if index >= len(candidates):
                return

            # not_pick

            val = candidates[index]
            if val > target:
                return
            if val == target:
                ans.append(cur+[val])
                return
            ind = index

            while ind < len(candidates) and candidates[ind] == val:
                ind += 1
            
            findCombinationSum(candidates, target, ind, cur, ans)

            findCombinationSum(candidates, target-val, index+1, cur+[val], ans)

        ans = []
        findCombinationSum(candidates, target, 0, [], ans)
        return ans