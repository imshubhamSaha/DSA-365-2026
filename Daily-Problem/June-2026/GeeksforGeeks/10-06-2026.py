# Check Repeated Substring with K Replacements

class Solution:
    def kSubstr(self, s: str, k: int) -> bool:
        n = len(s)
        hashMap = {}
        for i in range(0 , n , k):
            sub = s[i:i+k]
            hashMap[sub] = hashMap.get(sub , 0) + 1
        if len(hashMap) == 1:
            return True
        if len(hashMap) == 2:
            for sub in hashMap:
                if hashMap[sub] == 1:
                    return True
        return False
        
        
