class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        # this question should be a hard tagged.
        # looks like partition dp.

        total = sum(nums)
        # mp = Counter(nums) # at most 16 values. freq of at most 4.

        if total % k != 0: return False

        
        # after some wrestling, the best way forward is to explore all posibility with backtracking. good bruteforce. ngl, this problem was difficult.

        # I know we want to sort the nums.

        nums.sort(reverse=True)
        target = total // k
        n = len(nums)
        used = [False for _ in range(n)]

        def backtrack(i, numPartitions, partitionSum):
            # base case.
            if numPartitions == 0: # valid
                return True
            if partitionSum == target:
                return backtrack(0, numPartitions-1, 0) # new one.

            # explore all options.
            for j in range(i, n):
                if used[j] == True or partitionSum + nums[j] > target:
                    continue

                used[j] = True
                if backtrack(j+1, numPartitions, partitionSum + nums[j]):
                    return True
                used[j] = False

                if partitionSum == 0:
                    return False
            
            return False
        
        return backtrack(0, k, 0)
            