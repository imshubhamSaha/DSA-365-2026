# Perimeter of Shapes in Binary Matrix
class Solution:
    def findPerimeter(self, mat: list[list[int]]) -> int:
        hth=len(mat)
        wth=len(mat[0])
        seen=set()
        def fill(x,y):
            nonlocal mat,hth,wth,seen
            if not(0<=x<wth and 0<=y<hth) or (x,y,) in seen or mat[y][x]==0:
                return 0
            ret=1 if x-1<0 or mat[y][x-1]==0 else 0
            ret+=1 if x+1>=wth or mat[y][x+1]==0 else 0
            ret+=1 if y-1<0 or mat[y-1][x]==0 else 0
            ret+=1 if y+1>=hth or mat[y+1][x]==0 else 0
            seen.add((x,y,))
            return ret+fill(x+1,y)+fill(x-1,y)+fill(x,y+1)+fill(x,y-1)
        ret=0
        for y in range(hth):
            for x in range(wth):
                ret+=fill(x,y)
        return ret
