class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(path,visited):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for idx in range(len(nums)):
                if visited[idx]:
                    continue
                path.append(nums[idx])
                visited[idx] = True
                dfs(path,visited)
                path.pop()
                visited[idx] = False
        dfs([],[False]*len(nums))
        return res