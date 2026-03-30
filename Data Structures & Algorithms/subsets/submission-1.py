class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr_start, path):
            res.append(path[:])

            for options in range(curr_start,len(nums)):
                path.append(nums[options])
                dfs(options+1,path)
                path.pop()
            
        dfs(0,[])
        return res