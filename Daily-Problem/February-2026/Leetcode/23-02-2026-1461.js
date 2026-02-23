// 1461. Check If a String Contains All Binary Codes of Size K

/**
 * @param {string} s
 * @param {number} k
 * @return {boolean}
 */
var hasAllCodes = function (s, k) {
  const n = s.length;
  const unique_binary = new Set();

  for (let i = 0; i <= n - k; i++) {
    unique_binary.add(s.slice(i, i + k));
  }

  return unique_binary.size === Math.pow(2, k);
};
