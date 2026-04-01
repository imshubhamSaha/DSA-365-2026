// 2751. Robot Collisions

/**
 * @param {number[]} positions
 * @param {number[]} healths
 * @param {string} directions
 * @param {number[]} position_list
 * @return {number[]}
 */
var removeRobot = function(positions, healths, directions, position_list) {
    const stack = [];

    for (const pos of position_list) {
        if (directions[pos] === "R") 
            stack.push(pos);
        else {
            while (stack.length && healths[pos] > 0) {
                const peek = stack.at(-1);

                if (healths[peek] > healths[pos]) {
                    healths[pos] = 0;
                    healths[peek] -= 1;
                }
                else if (healths[pos] > healths[peek]) {
                    healths[pos] -= 1;
                    healths[stack.pop()] = 0;
                }else {
                    healths[stack.pop()] = 0;
                    healths[pos] = 0;
                }
            }
        }    
    }

    let idx = 0;

    for(let i = 0; i < healths.length; i++) {
        if (healths[i] > 0) {
            healths[idx] = healths[i];
            idx++;
        }    
    }
    
    return idx;
}

/**
 * @param {number[]} positions
 * @param {number[]} healths
 * @param {string} directions
 * @return {number[]}
 */
var survivedRobotsHealths = function(positions, healths, directions) {
    const n = positions.length;
    const position_list = Array.from({length : n}, (_, idx) => idx);
    position_list.sort((a,b) => positions[a] - positions[b]);

    const survived_healths_idx = removeRobot(positions, healths, directions, position_list)
    healths.splice(survived_healths_idx)
    return healths;
};
