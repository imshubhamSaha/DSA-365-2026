# Box Stacking
class Solution:
    def maxHeight(self, height: list[int], width: list[int], length: list[int]) -> int:
        # Code here
        n = len(length)
        rot = []

        def get_area(box):
            boxw = box[1]
            boxl = box[2]
            return boxw * boxl

        for i in range(n):
            h, w, l = height[i], width[i], length[i]
            rot.append((h, min(w, l), max(w, l)))
            rot.append((w, min(h, l), max(h, l)))
            rot.append((l, min(h, w), max(h, w)))

        rot.sort(key=get_area, reverse=True)

        numbox = len(rot)
        msh = [box[0] for box in rot]

        for i in range(1, numbox):
            for j in range(0, i):
                if rot[i][1] < rot[j][1] and rot[i][2] < rot[j][2]:
                    if msh[i] < msh[j] + rot[i][0]:
                        msh[i] = msh[j] + rot[i][0]

        return max(msh)
