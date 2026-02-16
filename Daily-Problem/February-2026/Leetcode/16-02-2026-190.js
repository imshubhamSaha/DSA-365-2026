// 190. Reverse Bits

/**
 * @param {number} n
 * @return {number}
 */
var reverseBits = function(n) {
    const bits = new Array(32).fill(0);
    let i = 0;
    let num = n >>> 0; 

    while (num !== 0 && i < 32) {
        bits[i] = num & 1;
        num = num >>> 1;
        i++;
    }
    let res = bits[31] >>> 0;
    for (let k = 0; k < 31; k++) {
        res = (res + (bits[k] << (31 - k))) >>> 0;
    }
    return res >>> 0;
};
