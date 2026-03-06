// 1784. Check if Binary String Has at Most One Segment of Ones

/**
 * @param {string} s
 * @return {boolean}
 */
var checkOnesSegment = function (s) {
  let seenZero = false;

  for (let c of s) {
    if (c === "0") {
      seenZero = true;
    } else if (seenZero) {
      return false;
    }
  }

  return true;
};
