// 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

/**
 * @param {string} n
 * @return {number}
 */
var minPartitions = function(n) {
    for (let i = 9; i > 0; i--) {
        if (n.includes(i.toString())) return i;
    }
    return 0;
};
