//3740. Minimum Distance Between Three Equal Elements I
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumDistance = function(nums) {
    const n = nums.length;
    const idxMapping = new Map();
    let minDist = Number.MAX_SAFE_INTEGER;

    for (let i = 0; i <n; i++) {
        const num = nums[i];

        if (!idxMapping.has(num))
            idxMapping.set(num, [i,-1,-1]);
        else {
            const [fp,sp,tp] = idxMapping.get(num);
            if (sp === -1) 
                idxMapping.set(num, [fp,i,tp]);
            else if (tp != -1) {
                idxMapping.set(num, [sp,tp,i]);
                minDist = Math.min(minDist , (Math.abs(sp-tp) + Math.abs(tp-i) + Math.abs(i - sp)));
            }else {
                idxMapping.set(num, [fp,sp,i]);
                minDist = Math.min(minDist , (Math.abs(sp-fp) + Math.abs(sp-i) + Math.abs(i - fp)));
            }
        }
    }

    return minDist === Number.MAX_SAFE_INTEGER ? -1 : minDist;
};
