// 67. Add Binary

/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    const m = a.length;
    const n = b.length;

    const binary_sum = [];
    let idx1 = m - 1;
    let idx2 = n - 1;
    let carry = 0;

    while (idx1 >= 0 || idx2 >= 0 || carry) {
        const num1 = idx1 >= 0 ? a[idx1].charCodeAt(0) - "0".charCodeAt(0) : 0;
        const num2 = idx2 >= 0 ? b[idx2].charCodeAt(0) - "0".charCodeAt(0) : 0;
        const s = num1 ^ num2 ^ carry;
        binary_sum.push(s);
        carry = (num1 & num2) | (num1 & carry) | (num2 & carry);
        idx1 -= 1;
        idx2 -= 1;
    }

    return binary_sum.reverse().join("");
};
