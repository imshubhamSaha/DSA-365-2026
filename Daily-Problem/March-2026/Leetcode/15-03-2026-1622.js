// 1622. Fancy Sequence


var Fancy = function() {
    this.MOD = 1000000007n;
    this.seq = [];
    this.mul = 1n;
    this.add = 0n;
};
Fancy.prototype.modPow = function(a, b) {
    let res = 1n;
    a = BigInt(a);
    b = BigInt(b);

    while (b > 0n) {
        if (b & 1n) res = (res * a) % this.MOD;
        a = (a * a) % this.MOD;
        b >>= 1n;
    }
    return res;
};
/** 
 * @param {number} val
 * @return {void}
 */
Fancy.prototype.append = function(val) {
    val = BigInt(val);
    let inv = this.modPow(this.mul, this.MOD - 2n);
    let stored = ((val - this.add + this.MOD) % this.MOD * inv) % this.MOD;
    this.seq.push(stored);
};

/** 
 * @param {number} inc
 * @return {void}
 */
Fancy.prototype.addAll = function(inc) {
    this.add = (this.add + BigInt(inc)) % this.MOD;
};

/** 
 * @param {number} m
 * @return {void}
 */
Fancy.prototype.multAll = function(m) {
    m = BigInt(m);
    this.mul = (this.mul * m) % this.MOD;
    this.add = (this.add * m) % this.MOD;
};

/** 
 * @param {number} idx
 * @return {number}
 */
Fancy.prototype.getIndex = function(idx) {
    if (idx >= this.seq.length) return -1;
    let val = (this.seq[idx] * this.mul + this.add) % this.MOD;
    return Number(val);
};

/** 
 * Your Fancy object will be instantiated and called as such:
 * var obj = new Fancy()
 * obj.append(val)
 * obj.addAll(inc)
 * obj.multAll(m)
 * var param_4 = obj.getIndex(idx)
 */
