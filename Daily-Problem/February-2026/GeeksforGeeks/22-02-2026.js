// Count Subarrays with given XOR

/**
 * @param {number[]} arr
 * @param {number} k
 * @returns {number}
 */

class Solution {
  subarrayXor(arr, k) {
    const n = arr.length;

    let cnt = 0;
    let xor = 0;
    const mp = new Map();
    mp.set(0, 1);

    for (let i = 0; i < n; i++) {
      xor = xor ^ arr[i];

      if (mp.has(xor ^ k)) cnt += mp.get(xor ^ k);

      mp.set(xor, (mp.get(xor) || 0) + 1);
    }

    return cnt;
  }
}
