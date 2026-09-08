# Word in Grid - All Occurrences
class Solution:
    def searchWord(self, mat, word):
        n=len(mat)
        m=len(mat[0])
        ans=[]
        dirs={0:[0,1],1:[0,-1],2:[1,0],3:[-1,0],4:[-1,1],5:[-1,-1],6:[1,-1],7:[1,1]}
        def find(i,j,dir,k):
            if k>=len(word):
                return True

            if i<0 or i>=n or j<0 or j>=m or mat[i][j]!=word[k]:
                return False

            x=i+dirs[dir][0]
            y=j+dirs[dir][1]
            return find(x,y,dir,k+1)


        for i in range(n):
            for j in range(m):
                if mat[i][j]==word[0]:
                    for dir in range(8):
                        if find(i,j,dir,0):
                            ans.append([i,j])
                            break
        return ans
        
