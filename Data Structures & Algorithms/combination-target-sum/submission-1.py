class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(curr_start,path,total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            
            for choices in range(curr_start,len(nums)):
                path.append(nums[choices])
                dfs(choices,path,total+nums[choices])
                path.pop()
        dfs(0,[],0)

        return res


