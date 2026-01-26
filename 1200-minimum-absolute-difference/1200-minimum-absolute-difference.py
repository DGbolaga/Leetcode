class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # we want to get the minimum difference between any two 
        # integers in the array.
        # A way that comes to the top of my head is:
        # - sort the array.
        # - find the minimum absolute difference in the sorted array.
        # - loop through the array and save the two values that give the
        # - minimum absolute difference.

        mp = {}
        arr.sort()
        ans = []
        n = len(arr)
        minA = float("inf")
        for i in range(1, n):
            minA = min(minA, arr[i] - arr[i-1])
        
        for i in range(1, n):
            if arr[i] - arr[i-1] == minA:
                ans.append([arr[i-1], arr[i]])
                
        return ans
