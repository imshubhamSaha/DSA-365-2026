// 1382. Balance a Binary Search Tree


/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {ArrayList} nodeArray
 */ 
var inOrderTraversal = function(root, nodesArray) {
    if(!root) return;
    inOrderTraversal(root.left, nodesArray);
    nodesArray.push(root);
    inOrderTraversal(root.right, nodesArray);
}

/**
 * @param {ArrayList} nodesArray
 * @param {Integer} start
 * @param {Integer} end
 * @return {TreeNode}
 */
var createBalancedTree = function(nodesArray, start, end) {
    if(end < start) return null;
    const mid = Math.floor((end-start)/2) + start;
    const root = nodesArray[mid];
    root.left = createBalancedTree(nodesArray, start, mid -1);
    root.right = createBalancedTree(nodesArray, mid+1, end);
    return root;
}

/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var balanceBST = function(root) {
    const nodesArray = [];
    inOrderTraversal(root, nodesArray);
    return createBalancedTree(nodesArray, 0 , nodesArray.length-1);
};
