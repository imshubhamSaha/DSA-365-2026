#3622. Check Divisibility by Digit Sum and Product

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = n
        digit_sum = 0
        digit_product = 1

        while num :
            digit_sum += num % 10
            digit_product *= num % 10

            num //= 10

        return (n % (digit_sum + digit_product)) == 0
