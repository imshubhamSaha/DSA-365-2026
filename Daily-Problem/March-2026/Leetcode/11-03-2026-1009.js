// 1009. Complement of Base 10 Integer

/**
 * @param {number} n
 * @return {number}
 */
var bitwiseComplement = function(n) {
    let temp = n;
    if (n === 0)
        return 1;
    let s = 0;
    let base = 1;
    while (temp) {

        if ((temp & 1) == 0) {
            s += base;
        }
        base *= 2;
        temp >>= 1;
    }

    return s;
};
