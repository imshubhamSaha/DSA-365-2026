// 536. Minimum Swaps to Arrange a Binary Grid

/**
 * @param {number[][]} grid
 * @return {number}
 */
var minSwaps = function(grid) {
    let n = grid.length;
    let trailingZeros = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        let zeros = 0;
        for (let j = n - 1; j >= 0; j--) {
            if (grid[i][j] === 0) zeros++;
            else break;
        }
        trailingZeros[i] = zeros;
    }
    let swaps = 0;
    for (let i = 0; i < n; i++) {
        let needed = n - i - 1;
        let found = -1;
        for (let j = i; j < n; j++) {
            if (trailingZeros[j] >= needed) {
                found = j;
                break;
            }
        }
        if (found === -1) return -1;
        while (found > i) {
            [trailingZeros[found], trailingZeros[found - 1]] = [trailingZeros[found - 1], trailingZeros[found]];
            found--;
            swaps++;
        }
    }
    return swaps;
};
