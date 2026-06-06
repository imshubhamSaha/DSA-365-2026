# 2574. Left and Right Sum Differences

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        run_sum = nums[0]

        for i in range(1, n) :
            answer[i] = run_sum
            run_sum += nums[i]

        run_sum = nums[n-1]

        for i in range(n-2, -1, -1) :
            answer[i] = abs(answer[i] - run_sum)
            run_sum += nums[i]
        
        return answer
