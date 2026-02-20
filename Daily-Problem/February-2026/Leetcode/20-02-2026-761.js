// 761. Special Binary String

/**
 * @param {string} s
 * @return {string}
 */
var makeLargestSpecial = function (s) {
  let res = [];
  let cnt = 0,
    idx = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "1") cnt++;
    else cnt--;

    if (cnt === 0) {
      const inner = makeLargestSpecial(s.slice(idx + 1, i));
      res.push("1" + inner + "0");
      idx = i + 1;
    }
  }

  res.sort().reverse();
  return res.join("");
};
