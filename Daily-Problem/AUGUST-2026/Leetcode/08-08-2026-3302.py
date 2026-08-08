#3302. Find the Lexicographically Smallest Valid Sequence
class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n1, n2 = len(word1), len(word2)
        pref = [0] * n1

        # right to left
        j = n2 - 1
        for i in range(n1 - 1, -1, -1):
            if i < n1 - 1:
                pref[i] = pref[i + 1]
            if j >= 0 and word1[i] == word2[j]:
                pref[i] += 1
                j -= 1

        # left to right
        res = [-1] * n2
        match = 0
        i, j = 0, 0
        while i < n1 and j < n2:
            if word1[i] == word2[j]:
                res[j] = i
                j += 1
                match += 1
            elif i < n1 - 1 and pref[i + 1] >= n2 - match - 1:
                res[j] = i
                j += 1
                i += 1
                while j < n2 and i < n1:
                    if word1[i] == word2[j]:
                        res[j] = i
                        j += 1
                    i += 1
                return res

            i += 1

        if match == n2:
            return res
        return []p
