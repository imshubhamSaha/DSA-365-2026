# 2904. Shortest and Lexicographically Smallest Beautiful String
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ones_position = []

        for i in range(n) :
            if s[i] == '1' :
                ones_position.append(i)

        m = len(ones_position)

        if m < k :
            return ''

        smallest_substring = ''

        for i in range(m - k + 1) :
            left_pos = ones_position[i]
            right_pos = ones_position[i + k - 1]

            curr_substring = s[left_pos : right_pos + 1]

            if (smallest_substring == '') or (len(curr_substring) < len(smallest_substring)) or ((len(curr_substring) == len(smallest_substring)) and (curr_substring < smallest_substring)) :
                smallest_substring = curr_substring

        return smallest_substring
