#3612. Process String with Special Operations I

class Solution:
    # reverse function
    def reverse(self, char_arr ) :
        left = 0
        right = len(char_arr) - 1

        while left < right :
            char_arr[left] , char_arr[right] = char_arr[right], char_arr[left]
            left += 1
            right -= 1

        return char_arr
    
    #duplicate function
    def duplicateString(self, string_arr) :
        n = len(string_arr) 
        new_arr = [''] * (2 * n)

        for i in range(n) :
            new_arr[i] = string_arr[i]
            new_arr[n + i] = string_arr[i]

        return new_arr

    # main function
    def processStr(self, s: str) -> str:
        """
        * -> remove lastchar
        # -> dup the res and append it in res
        % -> rev the curr result
        """
        n = len(s)
        result = []

        for i in range(n) :
            char = s[i]
            if char == '*' :
                if len(result) :
                    result.pop()
                
            elif char == '#':
                result = self.duplicateString(result)
            elif char == '%' :
                result = self.reverse(result)
            else :
                result.append(char)

        return "".join(result)
