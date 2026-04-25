#Opposite Sign Pair Reduction
class Solution:
    def reducePairs(self, arr):
        # code here
        stack = []

        for current in arr:
            while stack:
                top = stack[-1]

                if (top > 0 > current) or (top < 0 < current):

                    if abs(top) > abs(current):
                        current = None
                        break

                    elif abs(top) < abs(current):
                        stack.pop()
                        continue

                    else:
                        stack.pop()
                        current = None
                        break

                else:
                    break

            if current is not None:
                stack.append(current)

        return stack
            
