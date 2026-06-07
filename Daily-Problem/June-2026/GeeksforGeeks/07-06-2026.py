#Finding Profession

class Solution:
    def profession(self, level, pos):
        # code here
        cnt = bin(pos - 1).count('1')

        if cnt % 2 == 0:
            return "Engineer"
        else:
            return "Doctor"

