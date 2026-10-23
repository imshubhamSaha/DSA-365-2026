# Count Pairs Violating BST Property
''' BST Node Structure
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def pairsViolatingBST(self, root):
        s = [root]
        arr = []
        while s:
            if isinstance(s[-1], int):
                arr.append(s.pop())
            else:
                node = s.pop()
                if node.right:
                    s.append(node.right)
                s.append(node.data)
                if node.left:
                    s.append(node.left)
        inversions_count = 0

        def mergesort(arr: list[int]) -> list[int]:
            nonlocal inversions_count
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            brr = mergesort(arr[:mid])
            crr = mergesort(arr[mid:])
            i = j = 0
            bl, cl = len(brr), len(crr)
            arr.clear()
            while i < bl and j < cl:
                if brr[i] <= crr[j]:
                    arr.append(brr[i])
                    i += 1
                else:
                    arr.append(crr[j])
                    j += 1
                    inversions_count += bl - i
            if i < bl:
                arr.extend(brr[i:])
            elif j < cl:
                arr.extend(crr[j:])
            return arr

        mergesort(arr)
        return inversions_count
