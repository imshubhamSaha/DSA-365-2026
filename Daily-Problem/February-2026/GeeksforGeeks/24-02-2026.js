// Longest Span in two Binary Arrays

/**
 * @param {number[]} a1
 * @param {number[]} a2
 * @returns {number}
 */
class Solution {
  equalSumSpan(a1, a2) {
    const n = a1.length;
    const diff = new Array(n).fill(0);
    diff[0] = a1[0] - a2[0];
    for (let i = 1; i < n; i++) diff[i] = diff[i - 1] + (a1[i] - a2[i]);

    const first_occurrence = new Map();
    let max_len = 0;

    for (let i = 0; i < n; i++) {
      if (diff[i] == 0) max_len = Math.max(max_len, i + 1);

      if (first_occurrence.has(diff[i])) {
        const span_len = i - first_occurrence.get(diff[i]);
        max_len = Math.max(max_len, span_len);
      } else first_occurrence.set(diff[i], i);
    }
    return max_len;
  }
}
