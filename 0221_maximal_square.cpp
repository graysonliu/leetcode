/*
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
*/

#include <vector>

using namespace std;

class Solution
{
public:
    int maximalSquare(vector<vector<char>> &matrix)
    {
        // dynamic programming

        // dp(i,j) represents the side length of the maximum square whose bottom right corner is the
        // cell with index (i,j) in the original matrix.

        // dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1

        // https://assets.leetcode.com/static_assets/media/original_images/221_Maximal_Square.PNG?raw=true

        if (matrix.empty())
            return 0;
        int rows = matrix.size(), cols = matrix[0].size();
        int max_len = 0;
        vector<vector<int>> dp(rows + 1, vector<int>(cols + 1, 0));
        // we use an extra row on the top and an extra column on the left to avoid out of index range
        // that is, dp[i][j] is corresponding to matrix[i-1][j-1]

        for (int i = 1; i <= rows; ++i)
        {
            for (int j = 1; j <= cols; ++j)
            {
                if (matrix[i - 1][j - 1] == '1')
                {
                    dp[i][j] = min(dp[i - 1][j], min(dp[i - 1][j - 1], dp[i][j - 1])) + 1;
                    max_len = max(max_len, dp[i][j]);
                }
            }
        }
        return max_len * max_len;
    }
};
