# 3720. Lexicographically Smallest Permutation Greater Than Target
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - ord('a')] += 1

        prefix = []

        for i in range(n):

            x = ord(target[i]) - ord('a')

            if cnt[x] == 0:
                break

            cnt[x] -= 1
            prefix.append(target[i])

        if len(prefix) < n:
            i = len(prefix)
            x = ord(target[i]) - ord('a')

            for c in range(x + 1, 26):
                if cnt[c] == 0:
                    continue

                ans = "".join(prefix) + chr(ord('a') + c)

                cnt[c] -= 1

                for ch in range(26):
                    ans += chr(ord('a') + ch) * cnt[ch]

                return ans

        for i in range(len(prefix) - 1, -1, -1):

            cnt[ord(prefix[i]) - ord('a')] += 1
            prefix.pop()

            x = ord(target[i]) - ord('a')

            for c in range(x + 1, 26):

                if cnt[c] == 0:
                    continue

                ans = "".join(prefix) + chr(ord('a') + c)

                cnt[c] -= 1

                for ch in range(26):
                    ans += chr(ord('a') + ch) * cnt[ch]

                return ans

        return ""
