// 1545. Find Kth Bit in Nth Binary String
var reverse = function(...args) {
    return args.reverse().map(num => {
        if (num === "1") return "0";
        return "1";
    }).join("");
}
/**
 * @param {number} n
 * @param {number} k
 * @return {character}
 */
var findKthBit = function(n, k) {
    let binaryStr = "0";

    for (let i = 2; i <= n; i++) {
        const newStr = binaryStr + "1" + reverse(...binaryStr);
        binaryStr = newStr;
    }

    return binaryStr[k-1];
};
