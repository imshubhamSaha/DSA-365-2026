# Seating Arrangement

class Solution:
    def canSeatAllPeople(self, k, seats):
        if len(seats)==1 and k==1 and seats[0]==0:
            return True
        i = 0
        while i<(len(seats)-1):
            if seats[i]==0 and seats[i+1]==0:
                k-=1
                i+=1
            elif seats[i]==1 and seats[i+1]==1:
                return False
            i+=1
        if k<=0:
            return True
        return False
        
