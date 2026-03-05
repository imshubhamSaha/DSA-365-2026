// 1758. Minimum Changes To Make Alternating Binary String

/**
 * @param {string} s
 * @return {number}
 */
var minOperations = function(s) {
    const n = s.length;

    let ones_case = 0;
    let zeros_case = 0;

    for (let i = 0; i < n; i++) {
        if ((i % 2) === 0)
            if (s[i] === "0")
                ones_case += 1;
            else zeros_case += 1;
        else {
            if (s[i] === "0")
                zeros_case += 1;
            else ones_case += 1;
        }
    }

    return Math.min(ones_case, zeros_case);
};
