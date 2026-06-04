# 3751. Total Waviness of Numbers in Range I
class Solution:
    def checkWaviness(self, num,last_num) : 
        if ((num % 10) > (num // 10) % 10 and (num % 10) > last_num) :
            return True
        if ((num % 10) < (num // 10) % 10 and (num % 10) < last_num) :
            return True
        
        return False

    def totalWaviness(self, num1: int, num2: int) -> int:
        if num2 < 101 :
            return 0
        waviness = 0

        for i in range(max(num1, 101) , num2 + 1) :
            last_num = i % 10
            i = i // 10

            while (i // 10) > 0 : 
                if (self.checkWaviness(i,last_num)) :
                    waviness += 1
                last_num = i % 10
                i //= 10

        return waviness
