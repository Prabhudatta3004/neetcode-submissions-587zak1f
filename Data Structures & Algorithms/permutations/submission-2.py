class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path,visited):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(0,len(nums)):
                if visited[i]:
                    continue
                path.append(nums[i])
                visited[i] =True
                backtrack(path,visited)
                path.pop()
                visited[i] = False
        backtrack([],[False]*len(nums))
        return res