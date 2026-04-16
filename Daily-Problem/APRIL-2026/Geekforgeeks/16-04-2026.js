// Implement Atoi

class Solution {
  skippingZeroSpace(s) {
    const n = s.length;
    let left = 0;
    let right = n - 1;
    let sign = true;

    while (
      left <= right &&
      (s[left] === " " || s[left] === "-" || s[left] === "+" || s[left] === "0")
    ) {
      if (s[left] === "-") sign = false;
      left += 1;
    }
    if (left > right) return [left, right, sign];

    while (right >= left && s[right] === " ") right -= 1;

    return [left, right, sign];
  }
  myAtoi(s) {
    // code here
    const max_number = 2147483647;
    const min_number = -2147483648;

    if (!s) return 0;
    const n = s.length;
    let [left, right, sign] = this.skippingZeroSpace(s);

    if (left > right) return 0;

    let number = 0;
    while (left <= right) {
      if (
        !(
          s[left].charCodeAt(0) >= "0".charCodeAt(0) &&
          s[left].charCodeAt(0) <= "9".charCodeAt(0)
        )
      )
        break;

      number = number * 10 + (s[left] - 0);
      left += 1;
      if (sign && number >= max_number) return max_number;
      if (!sign && -1 * number <= min_number) return min_number;
    }

    return sign ? number : -1 * number;
  }
}
