class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(start,path):
            res.append(path[:])
            for idx in range(start,len(nums)):
                if idx>start and nums[idx] == nums[idx-1]:
                    continue
                path.append(nums[idx])
                dfs(idx+1,path)
                path.pop()
        dfs(0,[])
        return res