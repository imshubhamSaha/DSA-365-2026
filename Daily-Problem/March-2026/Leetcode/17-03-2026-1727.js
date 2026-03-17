// 1727. Largest Submatrix With Rearrangements

/**
 * @param {number[][]} matrix
 * @return {number}
 */
var largestSubmatrix = function(matrix) {
    let n = matrix.length, m = matrix[0].length, maxArea = 0;
    for (let i = 1; i < n; i++)
        for (let j = 0; j < m; j++)
            if (matrix[i][j]) matrix[i][j] += matrix[i - 1][j];

    for (let row of matrix) {
        row.sort((a, b) => b - a);
        for (let j = 0; j < m; j++)
            maxArea = Math.max(maxArea, row[j] * (j + 1));
    }
    return maxArea;
};
