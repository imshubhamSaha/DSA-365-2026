// K Sum Paths

/**
 * @param {Node} root
 * @param {number} k
 * @return {number}
 */

/*
class Node{
    constructor(data){
        this.data = data;
        this.left = null;
        this.right = null;
    }
}
*/

class Solution {
    solve(root, k, ans, mp, sum) {
        if (!root) return;
        
        sum += root.data;
        ans.count += (mp.get(sum - k) || 0);
        if (sum === k) ans.count++;
        
        mp.set(sum, (mp.get(sum) || 0) + 1);
        
        this.solve(root.left, k, ans, mp, sum);
        this.solve(root.right, k, ans, mp, sum);
        
        mp.set(sum, mp.get(sum) - 1);
    }
    countAllPaths(root, k) {
        const ans = { count: 0 };
        const mp = new Map();
        this.solve(root, k, ans, mp, 0);
        return ans.count;
        
    }
}
