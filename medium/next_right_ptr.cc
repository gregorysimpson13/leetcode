/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        if (root == nullptr) return root;
        queue<pair<Node*, int>> q;
        q.push({root, 0});
        Node* prev = nullptr;
        int prev_lvl = 0;
        while(!q.empty()) {
            auto &[curr, level] = q.front();
            if(prev != nullptr && prev_lvl == level) {
                prev->next = curr;
            } else {
                if(prev != nullptr) prev->next = nullptr;
            }
            if (curr->left != nullptr) q.push({curr->left, level+1});
            if (curr->right != nullptr) q.push({curr->right, level+1});
            prev = curr; prev_lvl = level;
            q.pop();
        }
        return root;
    }
};