class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # let's just get the next greater element of all the values in the array.
        n = len(nums2)
        arr = [-1 for _ in range(n)]
        monostack = []
        seen = set(nums1)
        mp = {}

        for i in range(n-1, -1, -1):
            if nums2[i] in seen:
                mp[nums2[i]] = i

            if not monostack:
                monostack.append(nums2[i])
            else:
                while monostack and monostack[-1] < nums2[i]:
                    monostack.pop()

                if monostack:
                    arr[i] = monostack[-1]

                monostack.append(nums2[i])
        
        return [arr[mp[val]] for val in nums1]

