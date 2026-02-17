//  401. Binary Watch

/**
 * @param {number} turnedOn
 * @return {string[]}
 */
var readBinaryWatch = function(turnedOn) {
    const res = [];
    if (turnedOn > 8) return res;
    for (let i = 0; i < 12; i++) {
        const setBit = i.toString(2).split('1').length - 1;
        if (setBit < turnedOn) {
            const remaining = turnedOn - setBit;
            for (let j = 0; j < 60; j++) {
                if (j.toString(2).split('1').length - 1 === remaining) {
                    res.push(`${i}:${j < 10 ? '0' + j : j}`);
                }
            }
        } else if (setBit === turnedOn) {
            res.push(`${i}:00`);
        }
    }
    return res;
};
