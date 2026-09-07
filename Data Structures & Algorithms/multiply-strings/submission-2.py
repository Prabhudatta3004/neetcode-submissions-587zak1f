class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        res = [0] * (len(num1) + len(num2)) ## stores the result array

        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):

                digit1 = int(num1[i])
                digit2 = int(num2[j])
                product = digit1 * digit2
                
                ## remainder and carry index
                p2 = i+j+1 ## remainder
                p1 = i+j
                total_sum = product +  res[p2]

                res[p2] = total_sum % 10
                res[p1] += total_sum // 10

        start = 0
        while start < len(res) and res[start] == 0:
            start +=1
        
        res_str = "".join(map(str, res[start:]))
        return res_str

