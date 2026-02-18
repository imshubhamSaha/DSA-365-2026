//  Count Inversions


/**
 * @param {number[]} arr
 * @returns {number}
 */

class Solution {
    cnt = 0;
    
    merge(arr , low, high, mid) {
        const n = mid - low + 1;
        const m = high - mid;
        const arr1 = new Array(n).fill(0);
        const arr2 = new Array(m).fill(0);
        
        for (let i = 0; i < n; i++) arr1[i] = arr[i + low];
        
        for (let i = 0; i < m; i++) arr2[i] = arr[i + mid + 1];
        
        let i = 0, j = 0, k = low;
        
        while (i < n && j < m) {
            if (arr1[i] <= arr2[j]) arr[k++] = arr1[i++];
            else {
                arr[k++] = arr2[j++];
                this.cnt += n - i;
            }
        }
        
        while (i < n) arr[k++] = arr1[i++];
        while (j < m) arr[k++] = arr2[j++];
    }
    
    mergeSort(arr, low, high) {
        if (low >= high) return 0;
        
        const mid = low + Math.floor((high - low)/2);
        this.mergeSort(arr,low,mid);
        this.mergeSort(arr,mid+1,high);
        this.merge(arr,low,high,mid);
        
        return this.cnt;
    }
    // Function to count inversions in the array.
    inversionCount(arr) {
        const n = arr.length;
        
        return this.mergeSort(arr,0,n-1);
    }
}
