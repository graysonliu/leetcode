/*
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
*/

#include <vector>
#include <climits>
#include <iostream>

using namespace std;

class Solution
{
public:
    int minSubArrayLen(int s, vector<int> &nums)
    {
        // dynamic programming
        // we need to find contiguous subarray that ends with each nums[i] and satisfies sum>=s
        int min_len = INT_MAX, sum = 0;
        int start = 0;
        for (int i = 0; i < nums.size(); ++i)
        {
            if (nums[i] >= s)
                return 1;
            sum += nums[i];
            if (sum >= s)
            {
                for (; sum >= s; start++)
                    sum -= nums[start];
                start--;
                sum += nums[start];
                min_len = min(i - start + 1, min_len);
            }
        }
        return min_len == INT_MAX ? 0 : min_len;
    }
};

int main()
{
    cout << Solution().minSubArrayLen(7, *new vector<int>{2, 3, 1, 2, 4, 3}) << endl;
    return 0;
}
