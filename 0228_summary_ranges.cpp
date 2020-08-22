/*
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
*/

#include <string>
#include <vector>

using namespace std;

class Solution
{
public:

    vector<string> summaryRanges(vector<int> &nums)
    {
        vector<string> res;
        int i = 0;
        while (i < nums.size())
        {
            int begin = i, end = i;
            while (end + 1 < nums.size() && nums[end] + 1 == nums[end + 1])
                end++;
            if (begin == end)
                res.push_back(to_string(nums[i]));
            else
                res.push_back(to_string(nums[begin]) + "->" + to_string(nums[end]));
            i = end + 1;
        }
        return res;
    }
};

int main()
{
    vector<string> v_s = Solution().summaryRanges(*new vector<int>{1, 3});
    return 0;
}
