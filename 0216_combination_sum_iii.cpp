/*
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
*/

#include <vector>

using namespace std;

class Solution
{
public:

    vector<vector<int>> res;

    void backtrack(int candidate_begin, int k, int n, vector<int> &path)
    {
        if (k == 0 && n == 0)
        {
            res.push_back(path);
            return;
        } else if (k <= 0 || n <= 0)
            return;
        for (int i = candidate_begin; i <= 9; ++i)
        {
            path.push_back(i);
            backtrack(i + 1, k - 1, n - i, path);
            path.pop_back();
        }
    }


    vector<vector<int>> combinationSum3(int k, int n)
    {
        // backtracking (dfs)
        // compare to 0039 and 0040
        vector<int> path{};
        backtrack(1, k, n, path);
        return res;

    }
};
