// Longest Subarray with Majority Greater than K

class Solution {
  longestSubarray(arr, k) {
    const n = arr.length;
    let longest_subarray = 0;

    const mpp = new Map();
    let greater_sum = 0;

    for (let i = 0; i < n; i++) {
      if (arr[i] > k) greater_sum += 1;
      else greater_sum -= 1;

      if (greater_sum > 0) longest_subarray = i + 1;

      const req = greater_sum - 1;

      if (mpp.has(req))
        longest_subarray = Math.max(longest_subarray, i - mpp.get(req));

      if (!mpp.has(greater_sum)) mpp.set(greater_sum, i);
    }
    return longest_subarray;
  }
}
