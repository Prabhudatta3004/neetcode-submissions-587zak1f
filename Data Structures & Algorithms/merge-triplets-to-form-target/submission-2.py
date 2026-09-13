class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        target_a,target_b,target_c = target

        a_flag = b_flag = c_flag = False

        for a,b,c in triplets:
            if a>target_a or b>target_b or c>target_c:
                continue
            
            if a == target_a:
                a_flag = True
            if b == target_b:
                b_flag = True
            if c == target_c:
                c_flag = True
        
        return a_flag and b_flag and c_flag