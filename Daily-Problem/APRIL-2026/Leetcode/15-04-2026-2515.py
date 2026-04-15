# 2515. Shortest Distance to Target String in a Circular Array

class Solution:
    def closestTarget(self, words, target, startIndex) :
        n = len(words)
        if words[startIndex] == target :
            return 0
        min_dist = 10001
        for i in range(n) :
            if (words[i] == target) :
                min_dist = min(min_dist, abs(startIndex - i), n - abs(i - startIndex))

        return min_dist if min_dist != 10001 else -1