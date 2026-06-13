# 3838. Weighted Word Mapping

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        n =  len(words)
        mpp = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'] 
        res = []

        for word in words:
            total_weight  = 0
            for ch in word :
                total_weight += weights[(ord(ch) - ord('a'))]

            res.append(mpp[total_weight % 26])

        return ''.join(res)
