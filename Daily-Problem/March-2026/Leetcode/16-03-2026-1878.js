// 1878. Get Biggest Three Rhombus Sums in a Grid

/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var getBiggestThree = function(grid) {
    const m = grid.length, n = grid[0].length;
    const sums = new Set();

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            sums.add(grid[i][j]);
            for (let s = 1; i + 2 * s < m && j - s >= 0 && j + s < n; s++) {
                let sum = 0;
                for (let k = 0; k < s; k++) {
                    sum += grid[i + k][j - k];
                    sum += grid[i + s + k][j - s + k];
                    sum += grid[i + 2 * s - k][j + k];
                    sum += grid[i + s - k][j + s - k];
                }
                sums.add(sum);
            }
        }
    }

    return Array.from(sums).sort((a, b) => b - a).slice(0, 3);
};
