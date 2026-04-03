// Gray Code

/**
 * @param {number} n
 * @returns {number[]}
 */
class Solution {
    graycode(n) {
        // code here
        let prev=["0", "1"];
        if(n === 1) 
            return prev;
         
        for(let i=2; i<=n; i++){
            const next = [];
            const pn =prev.length;
            
            for(let j = 0; j < pn; j++){
              next.push("0" + prev[j]);    
            }        
            for(let j = pn-1; j >= 0; j--){
              next.push("1" + prev[j]);    
            }
            
            prev = next;
                  
          }
          
          return prev;
    }
}
