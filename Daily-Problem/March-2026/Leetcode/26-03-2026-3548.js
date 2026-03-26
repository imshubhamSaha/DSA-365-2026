// 3548. Equal Sum Grid Partition II

/**
 * @param {number[][]} grid
 * @return {boolean}
 */
var canPartitionGrid = function(grid) {
    const m = grid.length;
    const n = grid[0].length;

    let total = 0, maxVal = 0;

    const rowSums = new Array(m).fill(0);
    const colSums = new Array(n).fill(0);


    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const v = grid[i][j];
            total += v;
            rowSums[i] += v;
            colSums[j] += v;
            if (v > maxVal) maxVal = v;
        }
    }

    const globalCnt = new Uint32Array(maxVal + 1);
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            globalCnt[grid[i][j]]++;
        }
    }

    const topCnt = new Uint32Array(maxVal + 1);
    let acc = 0;

    for (let i = 0; i < m - 1; i++) {
        for (let j = 0; j < n; j++) {
            const v = grid[i][j];
            topCnt[v]++;
        }

        acc += rowSums[i];
        const S1 = acc;
        const S2 = total - acc;

        if (S1 === S2) return true;

        const diff = Math.abs(S1 - S2);

        if (S1 > S2) {
            const rows = i + 1;

            if (rows >= 2 && n >= 2) {
                if (topCnt[diff] > 0) return true;
            } else if (rows === 1) {
                if (grid[0][0] === diff || grid[0][n - 1] === diff) return true;
            } else if (n === 1) {
                if (grid[0][0] === diff || grid[i][0] === diff) return true;
            }

        } else {
            const rows = m - (i + 1);

            if (rows >= 2 && n >= 2) {
                if (globalCnt[diff] - topCnt[diff] > 0) return true;
            } else if (rows === 1) {
                const r = i + 1;
                if (grid[r][0] === diff || grid[r][n - 1] === diff) return true;
            } else if (n === 1) {
                const r1 = i + 1, r2 = m - 1;
                if (grid[r1][0] === diff || grid[r2][0] === diff) return true;
            }
        }
    }


    const leftCnt = new Uint32Array(maxVal + 1);
    acc = 0;

    for (let j = 0; j < n - 1; j++) {
        for (let i = 0; i < m; i++) {
            const v = grid[i][j];
            leftCnt[v]++;
        }

        acc += colSums[j];
        const S1 = acc;
        const S2 = total - acc;

        if (S1 === S2) return true;

        const diff = Math.abs(S1 - S2);

        if (S1 > S2) {
            const cols = j + 1;

            if (m >= 2 && cols >= 2) {
                if (leftCnt[diff] > 0) return true;
            } else if (cols === 1) {
                if (grid[0][0] === diff || grid[m - 1][0] === diff) return true;
            } else if (m === 1) {
                if (grid[0][0] === diff || grid[0][j] === diff) return true;
            }

        } else {
            const cols = n - (j + 1);

            if (m >= 2 && cols >= 2) {
                if (globalCnt[diff] - leftCnt[diff] > 0) return true;
            } else if (cols === 1) {
                const c = j + 1;
                if (grid[0][c] === diff || grid[m - 1][c] === diff) return true;
            } else if (m === 1) {
                if (grid[0][j + 1] === diff || grid[0][n - 1] === diff) return true;
            }
        }
    }

    return false;
};
