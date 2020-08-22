/*
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
*/

#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    vector<int> majorityElement(vector<int> &nums)
    {
        vector<int> res;

        // my solution: not in O(1) space

//        int n = nums.size();
//        unordered_map<int, int> count;
//        for (int &i:nums)
//        {
//            count[i]++;
//            if (count[i] > n / 3 && (res.empty() || i != res[0]))
//                res.push_back(i);
//            if (res.size() == 2)
//                return res;
//        }

        // O(1) space solution: Boyer-Moore Voting Algorithm
        // we will have at most two majority elements that appear more than ⌊ n/3 ⌋ times
        // actually, we will have at most k-1 majority elements that appear more than ⌊ n/k ⌋ times
        // this algorithm is to find out two most frequent elements, but they might not be the majority elements
        // https://leetcode.com/problems/majority-element-ii/solution/
        int count1 = 0, count2 = 0;
        int candidate1 = 0, candidate2 = 0;
        for (int &num:nums)
        {
            if (candidate1 == num)
                count1++;
            else if (candidate2 == num)
                count2++;
            else if (count1 == 0)
            {
                candidate1 = num;
                count1++;
            }
            else if (count2 == 0)
            {
                candidate2 = num;
                count2++;
            }
            else
            {
                count1--;
                count2--;
            }
        }

        // verify whether candidates are actually majority elements
        int real_count1 = 0, real_count2 = 0;
        for (int &num:nums)
        {
            if (num == candidate1)
                real_count1++;
            else if (num == candidate2)
                real_count2++;
        }
        if (real_count1 > nums.size() / 3)
            res.push_back(candidate1);
        if (real_count2 > nums.size() / 3)
            res.push_back(candidate2);


        return res;
    }
};

int main()
{
    Solution().majorityElement(*new vector<int>{1, 2, 2, 3, 2, 1, 1, 3});
    return 0;
}
