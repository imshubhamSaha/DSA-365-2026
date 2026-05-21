//3043. Find the Length of the Longest Common Prefix
/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number}
 */
var longestCommonPrefix = function(arr1, arr2) {
    const n = arr1.length;
    const m = arr2.length;
    const possible_prefix = new Set();
    for (const num of arr1) {
        temp = num
        while (temp  > 0){
            possible_prefix.add(temp);
            temp =Math.floor( temp / 10);
        }
    }
        
    let lcp = 0;
        

    for (const num of arr2) {
        let len = (num + "").length;
        let temp = num 
        if (possible_prefix.has(temp)) {
            lcp = Math.max(lcp , len);
            continue;
        }
                
        while (temp) {
            temp = Math.floor(temp/10);
            len -= 1;
            if (possible_prefix.has(temp)) {
                lcp = Math.max(lcp , len);
            }
        }
    }

    return lcp;
};
