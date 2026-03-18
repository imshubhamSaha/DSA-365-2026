// 3070. Count Submatrices with Top-Left Element and Sum Less Than k

/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number}
 */
var countSubmatrices = function(grid, k) {
    let column_totals = [...grid[0]];
    let ROWS = grid.length;
    let COLS = grid[0].length;

    let res = 0;
    let running_total = 0;

    for (let total of column_totals) {
        running_total += total;
        if (running_total <= k) {
            res += 1;
        } else {
            break;
        }
    }

    for (let row_index = 1; row_index < ROWS; row_index++) {
        column_totals[0] += grid[row_index][0];
        if (column_totals[0] <= k) {
            res += 1;
        } else {
            break;
        }

        running_total = column_totals[0];

        for (let column_index = 1; column_index < COLS; column_index++) {
            let cell_value = grid[row_index][column_index];
            column_totals[column_index] += cell_value;
            running_total += column_totals[column_index];

            if (running_total <= k) {
                res += 1;
            } else {
                break;
            }
        }
    }

    return res;
};
