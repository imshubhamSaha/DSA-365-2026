//2069. Walking Robot Simulation II
/**
 * @param {number} width
 * @param {number} height
 */
var Robot = function(width, height) {
    this.w = width;
    this.h = height;
    this.x = 0; 
    this.y = 0; 
    this.dir = 0;
    this.d = ["East", "North", "West", "South"];
};

/** 
 * @param {number} num
 * @return {void}
 */
Robot.prototype.step = function(num) {
    const cycle = 2 * (this.w + this.h) - 4;
        num %= cycle;

        if (num === 0) {
            if (this.x === 0 && this.y === 0) this.dir = 3;
            return;
        }

        while (num > 0) {
            if (this.dir === 0) {
                let move = Math.min(num, this.w - 1 - this.x);
                this.x += move; num -= move;
                if (move === 0) this.dir = 1;
            } else if (this.dir === 1) {
                let move = Math.min(num, this.h - 1 - this.y);
                this.y += move; num -= move;
                if (move === 0) this.dir = 2;
            } else if (this.dir === 2) {
                let move = Math.min(num, this.x);
                this.x -= move; num -= move;
                if (move === 0) this.dir = 3;
            } else {
                let move = Math.min(num, this.y);
                this.y -= move; num -= move;
                if (move === 0) this.dir = 0;
            }
        }
};

/**
 * @return {number[]}
 */
Robot.prototype.getPos = function() {
    return [this.x, this.y];
};

/**
 * @return {string}
 */
Robot.prototype.getDir = function() {
    return this.d[this.dir];
};

/** 
 * Your Robot object will be instantiated and called as such:
 * var obj = new Robot(width, height)
 * obj.step(num)
 * var param_2 = obj.getPos()
 * var param_3 = obj.getDir()
 */
