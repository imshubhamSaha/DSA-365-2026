//657. Robot Return to Origin
/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    const n = moves.length;
    let left_right_move = 0;
    let up_down_move = 0;

    for (const move of moves) {
        if (move === "U" || move === "D") {
            if (move === "U") 
                up_down_move += 1;
            else 
                up_down_move -= 1;
        }else {
            if (move === "L") {
                left_right_move += 1;
            }else 
                left_right_move -= 1;
        }
    }

    return left_right_move === 0 && up_down_move === 0;
};
