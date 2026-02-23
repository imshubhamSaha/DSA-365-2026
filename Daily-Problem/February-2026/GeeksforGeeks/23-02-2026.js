// Union of Arrays with Duplicates

/**
 * @param {number[]} a
 * @param {number[]} b
 * @returns {number[]}
 */
class Solution {
  findUnion(a, b) {
    const m = a.length;
    const n = b.length;
    a.sort((a, b) => a - b);
    b.sort((a, b) => a - b);
    const union = [];

    let l1 = 0;
    let l2 = 0;

    while (l1 < m && l2 < n) {
      if (a[l1] === b[l2]) {
        if (!union.length || union[union.length - 1] != a[l1])
          union.push(a[l1]);
        l1 += 1;
        l2 += 1;
      } else if (a[l1] < b[l2]) {
        if (!union.length || union[union.length - 1] != a[l1])
          union.push(a[l1]);
        l1 += 1;
      } else {
        if (!union.length || union[union.length - 1] != b[l2])
          union.push(b[l2]);
        l2 += 1;
      }
    }

    while (l1 < m) {
      if (!union.length || union[union.length - 1] != a[l1]) union.push(a[l1]);
      l1 += 1;
    }

    while (l2 < n) {
      if (!union.length || union[union.length - 1] != b[l2]) union.push(b[l2]);
      l2 += 1;
    }

    return union;
  }
}
