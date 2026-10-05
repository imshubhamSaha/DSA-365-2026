# Your Social Network

class Solution:
    def socialNetwork(self, arr):
        # code here
        n = len(arr)+1
        network = []
        
        for i in range(2, n + 1) :
            recheable_user = i
            user_count = 0
            
            while recheable_user != 1 :
                recheable_user = arr[recheable_user - 2] 
                user_count += 1
                network.append([i, recheable_user, user_count])
        network.sort()
        return network
        
