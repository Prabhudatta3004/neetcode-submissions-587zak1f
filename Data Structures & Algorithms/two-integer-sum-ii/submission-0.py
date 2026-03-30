class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ## Since the array is sorted
        ## if the sum of i and j is less than the target then
        ## we increment i 
        ## if sum is greater than target we decrement j
        ## if we get the value we return i and j


        i = 0
        j = len(numbers)-1

        while i<j and j>i:
            if (numbers[i] + numbers[j]) > target:
                j -=1
            if (numbers[i] + numbers[j]) < target:
                i +=1
            if (numbers[i] + numbers[j]) == target:
                return [i+1,j+1]