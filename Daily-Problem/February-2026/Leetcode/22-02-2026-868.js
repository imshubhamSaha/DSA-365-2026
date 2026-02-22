// 868. Binary Gap

let prev = -1;
let res = 0;
let idx = 0;

while (n > 0) {
    if ((n & 1) === 1) {
        if (prev !== -1) 
            res = Math.max(res, idx - prev);
        prev = idx;
    }
    n = n >>> 1; 
    idx++;
}
return res;