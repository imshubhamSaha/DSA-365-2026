# 3754. Concatenate Non-Zero Digits and Multiply by Sum I
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num = n
        running_sum = 0
        x = 0
        place = 1
        while num :
            if num % 10 :
                x = (num % 10) * place + x
                place *= 10

            running_sum += num % 10
            num //= 10

        return x * running_sum


---------------
class Solution:
    def calculate(self, num, x, running_sum) :
        if num == 0 :
            return x , running_sum
        x, running_sum = self.calculate(num // 10, x, running_sum)
        digit = num % 10
        running_sum += digit
        if digit :
            x = x * 10 + digit 
        return x, running_sum

    def sumAndMultiply(self, n: int) -> int:
        num = n
        x, running_sum = self.calculate(num, 0, 0) 
        return x * running_sum


