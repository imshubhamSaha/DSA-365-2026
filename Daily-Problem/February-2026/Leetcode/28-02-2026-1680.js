// 1680. Concatenation of Consecutive Binary Numbers
/**
 * @param {number} n
 * @return {number}
 */
var concatenatedBinary = function(n) {
    let shifter = 1;
    let val = 1;
    let answer = 0n;
    const mod = 1000000007n;
    
    for (let a = 1; a <= n; a++) {
        if (val * 2 === a) {
            shifter++;
            val = a;
        }
        answer = ((answer << BigInt(shifter)) | BigInt(a)) % mod;
    }
    
    return Number(answer);
};
