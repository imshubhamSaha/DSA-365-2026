//Consecutive 1's not allowed


/**
 * @param {number} n
 * @returns {number}
 */
class Solution {
    countStrings(n) {
        
        let prev = 1;
        let cur = 1;
        let next = 0;
        let i = 1;
        while(i <= n) {
            next = (prev + cur);
            cur = prev;
            prev = next;
            i +=1;
        }
        
        return next;
    }
}
