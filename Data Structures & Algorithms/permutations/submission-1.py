class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr_start,visited,path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for choice in range(0,len(nums)):
                if visited[choice]:
                    continue
                
                visited[choice] = True
                path.append(nums[choice])
                backtrack(choice,visited,path)
                path.pop()
                visited[choice] = False
        
        backtrack(0,[False]*len(nums),[])

        return res
