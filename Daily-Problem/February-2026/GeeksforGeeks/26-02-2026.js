// Isomorphic Strings

/**
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean}
 */
class Solution {
  areIsomorphic(s1, s2) {
    const m = s1.length;
    const mapping = new Array(26).fill("");
    const rev_mapping = new Array(26).fill("");

    for (let i = 0; i < m; i++) {
      const c1 = s1[i].charCodeAt(0) - "a".charCodeAt(0);
      const c2 = s2[i].charCodeAt(0) - "a".charCodeAt(0);

      if (
        (mapping[c1] !== "" && mapping[c1] !== s2[i]) ||
        (rev_mapping[c2] !== "" && rev_mapping[c2] !== s1[i])
      )
        return false;

      mapping[c1] = s2[i];
      rev_mapping[c2] = s1[i];
    }

    return true;
  }
}
