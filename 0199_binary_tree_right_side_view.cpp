/*
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
*/



// * Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}

    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <vector>
#include <queue>

using namespace std;

class Solution
{
public:
    vector<int> rightSideView(TreeNode *root)
    {
        vector<int> res;
        if (!root)
            return res;
        TreeNode *pre = nullptr;
        queue<TreeNode *> Q;
        Q.push(root);
        while (!Q.empty())
        {
            // each level
            int l = Q.size();
            for (int i = 0; i < l; ++i)
            {
                pre = Q.front();
                if (pre->left)
                    Q.push(pre->left);
                if (pre->right)
                    Q.push(pre->right);
                Q.pop();
            }
            res.push_back(pre->val);
        }
        return res;
    }
    @Override
    int hashCode()
};