// 1356. Sort Integers by The Number of 1 Bits

/**
 * @param {number[]} arr
 * @return {number[]}
 */
var sortByBits = function (arr) {
  const countBits = (n) => {
    let count = 0;
    while (n > 0) {
      count++;
      n &= n - 1;
    }
    return count;
  };

  return arr.sort((a, b) => {
    const bitA = countBits(a);
    const bitB = countBits(b);
    if (bitA !== bitB) return bitA - bitB;
    return a - b;
  });
};
