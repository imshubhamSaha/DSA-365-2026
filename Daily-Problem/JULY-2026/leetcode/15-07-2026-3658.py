# 3658. GCD of Odd and Even Sums

class Solution:
    def gcd_rec (self, a, b) :
        if a == 0 or b == 0 :
            return max(a,b)
        if a < b :
            return self.gcd_rec(a, b % a)
        return self.gcd_rec(a%b, b)

    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_sum = 1
        even_sum = 2

        for i in range(1, n) :
            odd_sum += (i + 1) * 2 - 1
            even_sum += (i + 1) * 2

        print(odd_sum, even_sum)
        return self.gcd_rec(odd_sum, even_sum)
------------


class Solution:
    def gcd_rec (self, a, b) :
        if a == 0 or b == 0 :
            return max(a,b)
        if a < b :
            return self.gcd_rec(a, b % a)
        return self.gcd_rec(a%b, b)

    def gcdOfOddEvenSums(self, n: int) -> int:
        even_sum = (n * (n + 1))
        odd_sum = ((2* n) * ((2 * n) + 1)) // 2 - even_sum

        return self.gcd_rec(odd_sum, even_sum)
