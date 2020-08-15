/*
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
*/

#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    int calculate_bucket(int num, long capacity)
    {
        // capacity>=1, if capacity==1, we could have divide by zero error
        // when capacity==1, the bucket is just the number itself
        if (capacity == 1)
            return num;
        int b = num < 0 ? (num + 1) / capacity - 1 : num / capacity;
        return b;
    }

    bool containsNearbyAlmostDuplicate(vector<int> &nums, int k, int t)
    {
        // bucket sort
        unordered_map<int, int> buckets;
        // we keep at most k buckets, when a new bucket comes in, we should drop the oldest bucket
        // each bucket represents a range of length t+1
        // ..., [-t-1, -1], [0, t], [t+1, 2t+1], ...
        // if two numbers are in the same bucket, they satisfy abs(nums[i]-nums[j])<=t
        // if two numbers are in adjacent buckets, they might also satisfy the condition
        for (int i = 0; i < nums.size(); ++i)
        {
            if (t < 0) // absolute difference cannot be less than 0
                return false;

            long capacity = t + 1L; //the capacity of each bucket
            int b = calculate_bucket(nums[i], capacity); // the bucket for current number

            if (buckets.count(b) == 1) // fall in the same bucket
                return true;
            // check adjacent buckets
            if (buckets.count(b - 1) == 1 && abs(long(nums[i]) - buckets[b - 1]) <= t)
                return true;
            if (buckets.count(b + 1) == 1 && abs(long(nums[i]) - buckets[b + 1]) <= t)
                return true;

            buckets[b] = nums[i];

            // remove bucket whose index has a difference more than k compared to current index
            // we don't have to worry that a bucket has been updated during the iteration so that we might remove the wrong bucket
            // because if a bucket needs to be updated, that means we find two numbers falling into a same bucket with their
            // difference of indices at most k, in that case, the function will be terminated and return true.
            if (i >= k)
            {
                // nums[i - k] is the number to be removed, calculate its bucket
                b = calculate_bucket(nums[i - k], capacity);
                buckets.erase(b);
            }
        }
        return false;
    }
};


int main()
{
    Solution().containsNearbyAlmostDuplicate(*new vector<int>{1, 5, 9, 1, 5, 9}, 2, 3);
    return 0;
};
