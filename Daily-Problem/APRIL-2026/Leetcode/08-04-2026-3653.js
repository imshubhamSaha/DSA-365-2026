// 3653. XOR After Range Multiplication Queries I

/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number}
 */
var xorAfterQueries = function(nums, queries) {
    const MOD = 1000000007;
    let xor = nums.reduce((x, curr) => x ^ curr, 0);

    for (let [left, right, counter, factor] of queries) {
        while (left <= right) {
            xor ^= nums[left];
            nums[left] = (nums[left] * factor) % MOD;
            xor ^= nums[left];
            left += counter;
        }
    }

    return xor;
};
