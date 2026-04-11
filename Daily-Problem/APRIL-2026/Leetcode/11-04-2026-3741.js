//3741. Minimum Distance Between Three Equal Elements II
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumDistance = function(nums) {
    const n = nums.length;
    let min_dist = n + 1;

    const nextIndex = new Array(n).fill(-1);
    const occurence = new Map();

    for (let i = n - 1; i >= 0; i--) {
        if (occurence.has(nums[i])) 
            nextIndex[i] = occurence.get(nums[i]);
        occurence.set(nums[i], i);
    }

    for (let i = 0; i < n; i++) {
        const sp = nextIndex[i];
        if (sp === -1) 
            continue;
        const tp = nextIndex[sp];

        if (tp != -1) 
            min_dist = Math.min(min_dist, (tp - i));
    }

    return (min_dist === (n + 1)) ? -1 : 2 * min_dist;
};
