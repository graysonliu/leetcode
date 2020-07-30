/*
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]
]
Output: 3
*/

#include <vector>
#include <queue>

using namespace std;

class Solution
{
public:
    void dfs(int x, int y, vector<vector<char>> &grid)
    {
        if (x < 0 || y < 0 || x >= grid.size() || y >= grid[0].size() || grid[x][y] != '1')
            return;
        grid[x][y] = '2';
        dfs(x - 1, y, grid);
        dfs(x + 1, y, grid);
        dfs(x, y - 1, grid);
        dfs(x, y + 1, grid);
    }

    int numIslands(vector<vector<char>> &grid)
    {
        int res = 0;
        if (grid.empty() || grid[0].empty())
            return res;
        for (int i = 0; i < grid.size(); ++i)
            for (int j = 0; j < grid[0].size(); ++j)
                if (grid[i][j] == '1')
                {
                    res++;
                    dfs(i, j, grid);
                }
        return res;
    }
};
