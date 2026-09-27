# Longest Colored Path
class Solution:
    def longestPath(self, s, edges):
        n = len(s)
        g = [[] for _ in range(n)]
        
        for u, v in edges:
            u -= 1
            v -= 1
            g[u].append(v)
            g[v].append(u)

        par = [-1] * n
        order = [0]
        for u in order:
            for v in g[u]:
                if v != par[u]:
                    par[v] = u
                    order.append(v)

        down = [1] * n

        ans = 1
        
        for u in order[::-1]:
            a = b = 0

            for v in g[u]:

                if par[v] == u and s[v] == s[u]:
                    x = down[v]

                    if x > a:
                        b, a = a, x
                    elif x > b:
                        b = x

            down[u] = a + 1
            ans = max(ans, a + b + 1)

        up = [1] * n

        for u in order:
            a = b = 0
            who = -1
            
            for v in g[u]:
                if par[v] == u and s[v] == s[u]:

                    x = down[v]
                
                    if x > a:
                        b, a, who = a, x, v
                    elif x > b:
                        b = x



            for v in g[u]:
                if par[v] == u and s[v] == s[u]:
                    other = b if v == who else a
                    up[v] = 1 + max(up[u], other + 1)



        arm = [max(down[i], up[i]) for i in range(n)]



        for u, v in edges:
            u -= 1
            v -= 1
            
            if s[u] != s[v]:
                ans = max(ans, arm[u] + arm[v])



        return ans

