# Next Smallest Palindrome


class Solution:
    def nextPalindrome(self, num):
        n = len(num)
        ans = [0] * n
        is_greater = False

        i = 0
        j = n - 1

        if (n % 2) == 0:
            while i < j:
                if (num[i] > num[j]) or (num[i] >= num[j] and is_greater):
                    is_greater = True
                else:
                    is_greater = False

                ans[i] = num[i]
                ans[j] = ans[i]
                i += 1
                j -= 1
        else:
            while i <= j:
                if (num[i] > num[j]) or (num[i] >= num[j] and is_greater):
                    is_greater = True
                else:
                    is_greater = False
                ans[i] = num[i]
                ans[j] = ans[i]
                i += 1
                j -= 1

        if not is_greater:
            i -= 1
            j += 1

            if ans[i] == 9:
                ans[i] = 0
                ans[j] = 0
                i -= 1
                j += 1

                while (ans[i] == 9) and i >= 0 and j < n:
                    ans[i] = 0
                    ans[j] = 0
                    i -= 1
                    j += 1

            if i >= 0 and j < n:
                ans[i] = ans[i] + 1
                ans[j] = ans[i]
                is_greater = True

        if not is_greater:
            ans.append(1)
            ans[0] = 1

        return ans
