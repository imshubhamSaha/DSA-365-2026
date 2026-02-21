// Find H-Index

/**
 * @param {number[]} citations
 * @returns {number}
 */

class Solution {
  hIndex(citations) {
    // code here
    const n = citations.length;
    const bucket = new Array(n + 1).fill(0);

    for (let i = 0; i < n; i++) {
      if (citations[i] >= n) bucket[n]++;
      else bucket[citations[i]]++;
    }

    let maxCitation = 0;

    for (let i = n; i >= 0; i--) {
      maxCitation += bucket[i];

      if (maxCitation >= i) return i;
    }

    return 0;
  }
}
