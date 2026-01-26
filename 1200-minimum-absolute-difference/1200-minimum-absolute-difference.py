class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # we want to get the minimum difference between any two 
        # integers in the array.
        # A way that comes to the top of my head is:
        # - sort the array.
        # - find the minimum absolute difference in the sorted array.
        # - loop through the array and save the two values that give the
        # - minimum absolute difference.

        

      
        # arr.sort()
        # ans = []
        # n = len(arr)
        # minA = float("inf")
        # for i in range(1, n):
        #     minA = min(minA, arr[i] - arr[i-1])
        
        # for i in range(1, n):
        #     if arr[i] - arr[i-1] == minA:
        #         ans.append([arr[i-1], arr[i]])

        # return ans

        # A better approach will be to traverse the array once,
        # and update the resulting array, if it's less than the 
        # current minimum and update the minimum. 
        # If it's equals, we want to append it to our result.

        arr.sort()
        res = []
        n = len(arr)
        minA = float("inf")
        for i in range(1, n):
            diff = arr[i] - arr[i-1]
            if diff < minA:
                minA = diff
                res = [[arr[i-1], arr[i]]]
            elif diff == minA:
                res.append([arr[i-1], arr[i]])

        return res
