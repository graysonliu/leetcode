/*
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
*/

#include "utils.h"

class Solution
{
public:
    int get_height(TreeNode *root)
    {
        int h = 0;
        while (root != nullptr)
        {
            h++;
            root = root->left;
        }
        return h;
    }

    int countNodes(TreeNode *root)
    {
        // insight: every subtree of each node is also a complete binary tree
        // for every complete binary tree, either the left subtree is a perfect full binary tree, or the right
        // subtree is a perfect full binary tree
        if (root == nullptr)
            return 0;
        int l_h = get_height(root->left);
        int r_h = get_height(root->right);
        if (l_h == r_h) // the left subtree is definitely a complete binary tree, it has 2^(l_h)-1 nodes
            return 1 + ((1 << l_h) - 1) + countNodes(root->right); // root + left subtree + right subtree
        else // should be l_h - 1 == r_h, the right subtree is a complete binary tree
            return 1 + countNodes(root->left) + ((1 << r_h) - 1);
    }
};

// time complexity
// h is the height of the tree
// the size of the recursive stack should be O(h), meaning we have O(h) recursions
// in each recursion, we invoke get_height() function, whose time complexity is also O(h)
// thus, the overall time complexity should be O(h^2)