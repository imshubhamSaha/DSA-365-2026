// Sort by Set Bit Count


class Solution {
    initialiseSetBit() {
        const setBit = new Array(256).fill(0);
        for (let i = 1; i < 256; i++) 
            setBit[i] = (i & 1) + setBit[parseInt(i/2)];
        
        return setBit;
    }
    sortBySetBitCount(arr) {
        const setBit = this.initialiseSetBit();
        arr.sort((a,b) => {
            return (setBit[b & 0xff] +
            setBit[(b >> 8) & 0xff] +
            setBit[(b >> 16) & 0xff] +
            setBit[b >> 24]) - (setBit[a & 0xff] +
            setBit[(a >> 8) & 0xff] +
            setBit[(a >> 16) & 0xff] +
            setBit[a >> 24]);
        })
        
        return arr;
        
    }
};
