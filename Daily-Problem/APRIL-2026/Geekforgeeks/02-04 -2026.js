//Painting the Fence


/**
 * @param {number} n
 * @param {number} k
 * @returns {number}
 */
class Solution {
    countWays(n, k) {
        // code here
        if ( n === 1) 
            return k;
        let w1 = k;
        let w2 = k * k;
        
        for (let i = 3; i <= n; i++) {
            let w3 = (k - 1) *( w2 + w1);
            w1 =w2;
            w2 = w3;
        }
        
        return w2;
    }
}
