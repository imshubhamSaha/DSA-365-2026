# Largest with Same Parity Adjacent Swaps
class Solution:
    def lexicographicallyLargest(self, arr: list[int]) -> list[int]:
        # code here
        n = len(arr)
        parity = arr[0] & 1
        start = 0
        for i in range(1, n):
            if parity != arr[i] & 1:
                arr[start:i] = sorted(arr[start:i], reverse=True)
                parity = 1 - parity
                start = i
        arr[start:n] = sorted(arr[start:n], reverse=True)
        return arr
