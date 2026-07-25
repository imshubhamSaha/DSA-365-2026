# 3536. Maximum Product of Two Digits
class Solution:
    def maxProduct(self, n: int) -> int:
        if n <= 10 :
            return 0
        
        num = n
        first_digit = 0
        second_digit = -1

        while num :
            digit = num % 10
            if digit >= first_digit :
                second_digit = first_digit
                first_digit = digit
            elif digit > second_digit :
                second_digit = digit

            num //= 10

        return (first_digit * second_digit)
