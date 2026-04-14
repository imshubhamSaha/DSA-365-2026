// URLify a given string

/**
 * @param {String} s
 * @returns {String}
 */
class Solution {
  URLify(s) {
    // code here
    return s.replaceAll(" ", "%20");
  }
}
