#3761. Minimum Absolute Distance Between Mirror Pairs
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        mirror_img = {}
        min_dist = n + 1
        for i in range(n) :
            num = nums[i]
            if num in mirror_img :
                min_dist = min(min_dist, (i - mirror_img[num]))
            rev_num = 0

            while num :
                rev_num = rev_num * 10 + (num % 10)
                num //= 10
            mirror_img[rev_num] = i

        return min_dist if min_dist != (n + 1) else -1
