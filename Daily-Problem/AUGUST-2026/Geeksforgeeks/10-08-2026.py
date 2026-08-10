# High Effort vs Low Effort
class Solution:
    def maxTask(self, h: list[int], l: list[int]) -> int:
        n = len(h)
       
        prev_day_task = 0
        past_days_task = 0
       
        for i in range(n) :
            temp = prev_day_task
            prev_day_task = max(l[i] + prev_day_task, h[i] + past_days_task)
            past_days_task = temp
           
        return prev_day_task
