// Trapping Rain Water

/**
 * @param {number[]} arr
 * @returns {number}
 */

class Solution {
    maxWater(arr) {
        const n = arr.length;
        let totalWater = 0;
        let left = 0, right = n-1;
        
        let prefixMax = 0, suffixMax = 0;
        
        while (left < right) {
            if (arr[left] <= arr[right]) {
                if (arr[left] > prefixMax) {
                    prefixMax = arr[left];
                }    
                else {
                    totalWater += prefixMax - arr[left];
                }    
                left++;
            }else {
                if (arr[right] > suffixMax) {
                    suffixMax = arr[right];
                }    
                else {
                    totalWater += suffixMax - arr[right];
                }    
                right--;
            }
        }
        
        return totalWater;
    }
}
