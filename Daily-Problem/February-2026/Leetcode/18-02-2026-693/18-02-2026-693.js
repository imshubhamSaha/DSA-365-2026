//693. Binary Number with Alternating Bits

/**
 * @param {number} n
 * @return {boolean}
 */
var hasAlternatingBits = function(n) {
    let prev = n & 1;
    n >>= 1;

    while (n > 0) {
        let cur = n & 1;
        if (cur === prev) 
            return false;
        prev = cur;
        n >>= 1;
    }
    return true;
};
