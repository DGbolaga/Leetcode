class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # I am thinkin of a fast and slow pointer can of stuff.
        # I know that will not be O(log (m+n))
        # but that will give us a good way to start. we can use binary search to achieve the O(log (m+n)) afterwards.

        # or rather we can just simulate the middle point logic with 2 queues.

        #0 -> 1 2 3 5 6
        #0 -> 2 3 4 7
        
        # if even: 2 mid
        # if odd: 1.

        arr = [deque(nums1), deque(nums2)]
        n, m = len(nums1), len(nums2)
        cnt = 0
        # get to middle element
        while cnt < (n + m - 1) // 2 :
            var = []
            if arr[0]:
                var.append((0, arr[0].popleft()))
                if not arr[1] and arr[0]:
                    var.append((0, arr[0].popleft()))

            if arr[1]:
                var.append((1, arr[1].popleft()))
                if len(var) == 1 and arr[1]:
                    var.append((1, arr[1].popleft()))

            var.sort(key=lambda x: x[1])

            get_max = var[-1]
            arr[get_max[0]].appendleft(get_max[1])
            cnt += 1

        var = []
        if arr[0]:
            var.append((0, arr[0].popleft()))
            if not arr[1] and arr[0]:
                var.append((0, arr[0].popleft()))

        if arr[1]:
            var.append((1, arr[1].popleft()))
            if len(var) == 1 and arr[1]:
                var.append((1, arr[1].popleft()))

        var.sort(key=lambda x: x[1])
        if (n + m) % 2 == 1:
            get_min = var[0]
            return float(get_min[1])
        else:
            if arr[0]:
                var.append((0, arr[0].popleft()))
            if arr[1]:
                var.append((1, arr[1].popleft()))
            
            var.sort(key=lambda x: x[1])

            return (var[0][1] + var[1][1]) / 2
             

            


            
        


                

            