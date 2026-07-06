# 1288. Remove Covered Intervals
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        result = 0

        for i in range(n) :
            left , right = intervals[i]
            not_covered = True
            for j in range(n) :
                if i == j :
                    continue
                if left >= intervals[j][0] and right <= intervals[j][1] :
                    not_covered = False
                    break
            if not_covered :
                result += 1
        
        return result

  ------------------------

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()
        result = 0
        i = 0

        while i < n :
            left , right = intervals[i]
            i += 1
            while i < n and intervals[i][0] == left :
                right = max(right, intervals[i][1])
                i += 1
            while i < n and intervals[i][0] <= right and right >= intervals[i][1] :
                right = max(right, intervals[i][1])
                i += 1
            result += 1
        
        return result
