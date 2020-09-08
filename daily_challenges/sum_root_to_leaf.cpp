// Runtime: O(n); beats 98.4%
// Space: O(1); beats 49.2%
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int sumRootToLeaf(TreeNode* root) {
        get_sums(root,0);        
        return sum;
    }
​
private:
    int sum = 0;
    void get_sums(TreeNode* node, int curr) {
        if(node == nullptr){return;}
        curr <<=1;
        curr += node->val;
        if(node->left == nullptr && node->right == nullptr){this->sum += curr; return;}
        get_sums(node->left, curr); get_sums(node->right, curr);
        curr >>=1;
    }
};