// 3212. Count Submatrices With Equal Frequency of X and Y

/**
 * @param {character[][]} grid
 * @return {number}
 */
var numberOfSubmatrices = function(grid) {
    let n = grid.length;
    let m = grid[0].length;
    
    let prefixX = Array.from({length: n}, () => Array(m).fill(0));
    let prefixY = Array.from({length: n}, () => Array(m).fill(0));
    
    let count = 0;
    
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            
            let x = (grid[i][j] === 'X') ? 1 : 0;
            let y = (grid[i][j] === 'Y') ? 1 : 0;
            
            prefixX[i][j] = x;
            prefixY[i][j] = y;
            
            if (i > 0) {
                prefixX[i][j] += prefixX[i-1][j];
                prefixY[i][j] += prefixY[i-1][j];
            }
            if (j > 0) {
                prefixX[i][j] += prefixX[i][j-1];
                prefixY[i][j] += prefixY[i][j-1];
            }
            if (i > 0 && j > 0) {
                prefixX[i][j] -= prefixX[i-1][j-1];
                prefixY[i][j] -= prefixY[i-1][j-1];
            }
            
            if (prefixX[i][j] === prefixY[i][j] && prefixX[i][j] > 0) {
                count++;
            }
        }
    }
    
    return count;
};
