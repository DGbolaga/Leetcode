import math
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # # the first idea that comes to mind is to arrange the points
        # # based on the y axis (increasing)
        # squares.sort(key=lambda x: x[1]) # sort by y values.
        # total_area = sum(x[-1]**2 for x in squares)
        # print(total_area)

        # return 0
        # we can simulate this movement of dividing areas in half by moving
        # from the lowest to the highest.

        # as we are cutting, if 2 or more points are overlapping, we only need 
        # to know if the current y point divider falls within that points square.
        # If it does, we deduct the values of each movement upwards by (1*abs(y1-yP))
        # from a temporary total_sum. We can keep doing this until the total_sum_area
        # becomes exactly half of it's initial area.

        # I found a fault in my reasoning, which is that our divider is not moving in
        # discrete packs. It is moving continuously and they can be infinite number
        # of points between 1 and 2 on the y-axis.

        # a better approach will be to compute the total area sum and a target, which 
        # is half of the total-area-sum.

        # we can use a binary search algorithm to move between the range of the 
        # minimum y value and the maximum y value + size(length) of all 
        # the square points. With this we can compute area below and area above.
        # once our divider (D) increases the area below will increase. And we want this
        # to hold until the area below == target.

        min_y, max_h, area_sum = float('inf'), float('-inf'), 0
        n = len(squares)
        for i in range(n):
            min_y = min(min_y, squares[i][1])
            max_h = max(max_h, squares[i][1] + squares[i][2])
            area_sum += squares[i][2] ** 2
        
        # print(max_y, min_y, max_l, area_sum)
        target = area_sum / 2

        # get area below value
        def get_area_below(D):
            area = 0
            for x, y, l in squares:
                # if D is above less than y, we can't get 
                # any area from moving into it.
                # if D is exactly above the square (y+l) 
                # we can tage the whole area to be below it.
                # if D is in between y and y+l, 
                # we can take only the Area cut by that increase i.e l * (D - y)
                if D <= y:
                    continue # can't take.
                elif D >= y+l:
                    area += l * l # take the whole square.
                else:
                    area += l * (D-y) # take the part that's exactly within it (below)
            return area

 
        # perfom the binary search
        low, high = min_y, max_h
        for _ in range(60): # 60 iterations will assure 5 dp precison
            mid = (low + high) / 2
            if get_area_below(mid) < target:
                low = mid
            else:
                high = mid
            
        return low



