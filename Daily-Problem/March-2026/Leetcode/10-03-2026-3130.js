// 3130. Find All Possible Stable Binary Arrays II

const mod = 1000000007n;

    function comp(i) {
        let ways = Array(i + 1).fill(0n);
        let prev = Array(i + 1).fill(0n);
        prev[0] = 1n;

        for (let k = 1; k <= i; k++) {
            let curr = Array(i + 1).fill(0n);
            let pref = 0n;
            for (let j = 1; j <= i; j++) {
                pref = (pref + prev[j - 1]) % mod;
                if (j - limit - 1 >= 0) {
                    pref = (pref - prev[j - limit - 1] + mod) % mod;
                }
                curr[j] = pref;
            }
            ways[k] = curr[i];
            prev = curr;
        }
        return ways;
    }

    let Zero = comp(zero);
    let One = comp(one);
    let ans = 0n;

    for (let a = 1; a <= zero; a++) {
        if (a <= one) {
            ans = (ans + (Zero[a] * One[a]) % mod) % mod;
        }
        if (a - 1 >= 1 && a - 1 <= one) {
            ans = (ans + (Zero[a] * One[a - 1]) % mod) % mod;
        }
    }

    for (let a = 1; a <= zero; a++) {
        if (a <= one) {
            ans = (ans + (Zero[a] * One[a]) % mod) % mod;
        }
        if (a + 1 <= one) {
            ans = (ans + (Zero[a] * One[a + 1]) % mod) % mod;
        }
    }

    return Number(ans % mod);
