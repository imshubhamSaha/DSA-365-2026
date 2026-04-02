// Print Diagonally


/**
 * @param {number} n
 * @param {number[][]} mat
 * @returns {number[]}
 */

class Solution {
    diagView(mat) {
        //  code here
        const n = mat.length;
        const diagonal_element = [];
        for(let j = 0 ; j < n ; j++){
            let row = 0;
            let col = j;
            while(row < n && col >= 0){
                diagonal_element.push(mat[row][col]);
                row++;
                col--;
            }
        }
        for(let i = 1 ; i < n ; i++){
            let row = i;
            let col = n-1;
            while(row < n && col >= 0){
                diagonal_element.push(mat[row][col]);
                row++;
                col--;
            }
        }
    
        
                
        return diagonal_element;
    }
}
