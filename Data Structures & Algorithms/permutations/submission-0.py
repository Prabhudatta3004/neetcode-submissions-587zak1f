class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, visited,path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(0,len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                path.append(nums[i])
                dfs(i,visited,path)
                path.pop()
                visited[i] = False
        dfs(0,[False]*len(nums),[])
        return res