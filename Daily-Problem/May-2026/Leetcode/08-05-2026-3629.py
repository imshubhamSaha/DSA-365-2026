# 3629. Minimum Jumps to Reach End via Prime Teleportation
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        def compute_spf(n):
            spf = list(range(n+1))

            for i in range(2, int(n ** 0.5) + 1):
                if(spf[i] == i):
                    for j in range(i**2, n+1, i):
                        if(spf[j] == j):
                            spf[j] = i
        
            return spf
        
        def getAllPrimeFactors(x, spf):
            prime = set()
            while(x > 1):
                prime.add(spf[x])
                x //= spf[x]
            
            return prime
        
        smallest_prime_factor = compute_spf(max(nums))

        d = {}
        n = len(nums)

        if(n <= 1):
            return 0

        for i in range(n):
            for prime in getAllPrimeFactors(nums[i], smallest_prime_factor):
                if(prime in d):
                    d[prime].append(i)
                else:
                    d[prime] = [i]
        
        steps = [float("inf")] * (n)
        steps[0] = 0

        q = [[0, 0]]

        while(q):
            ind, step = q.pop(0)

            for i in range(max(ind-1, 0), min(n, ind + 2), 1):
                if(steps[i] > step + 1):
                    steps[i] = step + 1
                    q.append([i, step + 1])
            if(nums[ind] in d):
                for index in d[nums[ind]]:
                    if(steps[index] > step + 1):
                        q.append([index, step + 1])
                        steps[index] = step + 1
                d[nums[ind]].clear() # this is the main optimisation to remove redundant searches.
        
        return steps[-1]
