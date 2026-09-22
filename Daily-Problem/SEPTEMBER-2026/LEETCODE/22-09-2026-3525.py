# 3525. Find X Value of Array II
class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1

        cnt = [[0] * k for _ in range(2 * size)]
        prod = [1 % k] * (2 * size)

        def set_leaf(pos, val):
            i = pos + size
            v = val % k
            cnt[i] = [0] * k
            cnt[i][v] = 1
            prod[i] = v

        def pull(i):
            l, r = 2 * i, 2 * i + 1
            lp = prod[l]
            prod[i] = lp * prod[r] % k
            c = cnt[l][:]
            rc = cnt[r]
            for v in range(k):
                c[v * lp % k] += rc[v]
            cnt[i] = c

        for i in range(n):
            set_leaf(i, nums[i])
        for i in range(size - 1, 0, -1):
            pull(i)

        def update(pos, val):
            set_leaf(pos, val)
            i = (pos + size) >> 1
            while i:
                pull(i)
                i >>= 1

        def query(l, r):
            segs_l, segs_r = [], []
            lo, hi = l + size, r + size + 1
            while lo < hi:
                if lo & 1:
                    segs_l.append(lo); lo += 1
                if hi & 1:
                    hi -= 1; segs_r.append(hi)
                lo >>= 1; hi >>= 1
            segs = segs_l + segs_r[::-1]
            if not segs:
                return [0] * k
            rc = cnt[segs[0]][:]
            rp = prod[segs[0]]
            for s in segs[1:]:
                nc = rc[:]
                sc = cnt[s]
                for v in range(k):
                    nc[v * rp % k] += sc[v]
                rc = nc
                rp = rp * prod[s] % k
            return rc

        result = []
        for idx, val, start, x in queries:
            nums[idx] = val
            update(idx, val)
            c = query(start, n - 1)
            result.append(c[x])
        return result
