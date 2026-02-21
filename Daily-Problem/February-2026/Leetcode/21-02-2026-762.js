// 762. Prime Number of Set Bits in Binary Representation

/**
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var countPrimeSetBits = function (left, right) {
  function isPrime(x) {
    if (x < 2) return false;
    for (let d = 2; d * d <= x; d++) {
      if (x % d === 0) return false;
    }
    return true;
  }

  let res = 0;
  for (let i = left; i <= right; i++) {
    let x = i,
      bits = 0;
    while (x !== 0) {
      x &= x - 1;
      bits++;
    }
    if (isPrime(bits)) res++;
  }
  return res;
};
