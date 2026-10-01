# Minimum Time to Finish Project
from collections import defaultdict
class Solution:
    def minTime(self, duration, dependencies):
        # code here
        if len(dependencies)==0:
            return max(duration)
        adj=defaultdict(set)
        ino=defaultdict(int)
        for sta,sto in dependencies:
            adj[sta].add(sto)
            ino[sto]+=1
        tim=defaultdict(int)
        q=[ix for ix in range(len(duration)) if ino[ix]==0]
        while q:
            nq=[]
            for cur in q:
                for nxt in adj[cur]:
                    tim[nxt]=max(tim[nxt],tim[cur]+duration[cur])
                    ino[nxt]-=1
                    if ino[nxt]==0:
                        nq.append(nxt)
            q=nq
        if max(ino.values())>0:
            return -1
        return max([tim[ix]+duration[ix] for ix in range(len(duration))])
