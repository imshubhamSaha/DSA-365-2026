# Longest Subsequence with Adjacent Diff as 1
from collections import defaultdict
class Solution:
    def longestSubseq(self, arr):
        cnt = defaultdict(int)
        for num in arr:
            val = 0
            if num - 1 in cnt:
                val = cnt[num-1]
            if num + 1 in cnt:
                val = max(val, cnt[num + 1])
            val += 1
            cnt[num] = val

        return max(cnt.values())
        
