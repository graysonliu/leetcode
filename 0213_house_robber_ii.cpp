/*
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
*/

#include <vector>

using namespace std;

class Solution
{
public:
    int rob(vector<int> &nums)
    {
        // similar to 0198, but we get a circle instead of a list
        // dynamic programming
        // rob(i) = max(rob(i-1), rob(i-2)+nums[i])
        // we consider two situations
        // one is that the first house is robbed, the other one is the first house isn't robbed

        if (nums.empty())
            return 0;

        // the first house is robbed, then we could not rob the last house
        int pre_pre_1 = 0, pre_1 = nums[0];
        for (int i = 1; i < nums.size() - 1; ++i) // start from the second house
        {
            int temp = pre_1;
            pre_1 = max(pre_1, pre_pre_1 + nums[i]);
            pre_pre_1 = temp;
        }

        // the first house is not robbed, then we could rob the last house
        int pre_pre_2 = 0, pre_2 = 0;
        for (int i = 1; i < nums.size(); ++i)
        {
            int temp = pre_2;
            pre_2 = max(pre_2, pre_pre_2 + nums[i]);
            pre_pre_2 = temp;
        }

        return max(pre_1, pre_2);
    }
};
