//Anagram Palindrome

/**
 * @param {string} s
 * @returns {boolean}
 */
class Solution {
    canFormPalindrome(s) {
        // code here
        const n = s.length;
        let diff = 0;
        const freq = new Array(26).fill(0);
        
        for (const char of s) {
            const idx = char.charCodeAt(0) - 'a'.charCodeAt(0);
            if (!freq[idx]) {
                freq[idx] += 1;
                diff += 1;
            }
            else {
                freq[idx] -= 1;
                diff -= 1;
            }
        }
        return (diff == 0 || diff == 1) ? true : false;
    }
}
