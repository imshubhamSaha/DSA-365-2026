// 3296. Minimum Number of Seconds to Make Mountain Height Zero
/**
 * @param {number} mountainHeight
 * @param {number[]} workerTimes
 * @return {number}
 */
var minNumberOfSeconds = function(mountainHeight, workerTimes) {
    let low = 1n, high = 10000000000000000n;
    let res = high;
    
    const isPossible = (mid) => {
        let totalH = 0n;
        for (let n of workerTimes) {
            let nBig = BigInt(n);
            let val = (2n * mid) / nBig;
            // Quadratic root for x^2 + x - val = 0
            let x = Math.floor((-1 + Math.sqrt(1 + 4 * Number(val))) / 2);
            totalH += BigInt(x);
            if (totalH >= BigInt(mountainHeight)) return true;
        }
        return totalH >= BigInt(mountainHeight);
    };

    while (low <= high) {
        let mid = low + (high - low) / 2n;
        if (isPossible(mid)) {
            res = mid;
            high = mid - 1n;
        } else {
            low = mid + 1n;
        }
    }
    return Number(res);
};
