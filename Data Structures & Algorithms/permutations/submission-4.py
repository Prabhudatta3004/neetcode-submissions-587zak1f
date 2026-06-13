class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for idx in range(0,len(nums)):
                if nums[idx] in path:
                    continue
                path.append(nums[idx])
                dfs(path)
                path.pop()
        dfs([])
        return res