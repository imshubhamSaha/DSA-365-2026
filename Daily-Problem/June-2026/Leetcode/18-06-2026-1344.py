#1344. Angle Between Hands of a Clock
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_hand_angle = 6.0 * minutes
        hour_hand_angle = (30 * (hour % 12)) + (0.5 * minutes)
        angle_diff = abs(min_hand_angle - hour_hand_angle)
        return min(angle_diff, 360.0 - angle_diff)
