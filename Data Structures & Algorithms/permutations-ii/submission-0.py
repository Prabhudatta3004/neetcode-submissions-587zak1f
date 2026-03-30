class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(path,visited):
            if len(path) == len(nums):
                res.append(list(path))
                return
            for i in range(0,len(nums)):
                if i>0 and nums[i-1] == nums[i] and not visited[i-1]:
                    continue
                if visited[i]:
                    continue
                path.append(nums[i])
                visited[i] = True
                backtrack(path,visited)
                path.pop()
                visited[i] = False
        backtrack([],[False]*len(nums))

        return res