class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        #there is a great insight in this problem.
        #which is if there are even negative numbers. The maximum is the absolute sum of all the values.
        #if there are odd negative numbers. the maximum is the absolute sum of all the values minus the minimun absolute value.

        minV = float("inf")
        sumV = 0
        n = len(matrix)
        nCount = 0
        contains0 = False
        for i in range(n):
            for j in range(n):
                num = matrix[i][j]
                if num < 0:
                    nCount += 1
                minV = min(minV, abs(num))
                if num==0: 
                    contains0 = True
                sumV += abs(num)

        if contains0 or nCount % 2  == 0:
            return sumV
        else:
            return sumV - 2*minV
                
                
                
