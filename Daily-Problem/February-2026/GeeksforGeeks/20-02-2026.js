// Form the Largest Number

/**
 * @param {number[]} arr
 * @returns {String}
 */

class Solution {
  findLargest(arr) {
    const largest = arr.map((element) => element.toString());

    largest.sort((a, b) => {
      if (a + b > b + a) return -1;
      if (a + b < b + a) return 1;
      return 0;
    });

    return largest[0] === "0" ? "0" : largest.join("");
  }
}
