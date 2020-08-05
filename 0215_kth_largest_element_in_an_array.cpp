/*
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
*/

#include <vector>
#include <iostream>

using namespace std;

class Solution
{
public:
    int partition(vector<int> &nums, int start, int end)
    {
        int pivot = nums[end];
        int i = start;
        for (int j = start; j < end; ++j)
        {
            if (nums[j] < pivot)
                swap(nums[j], nums[i++]);
        }
        swap(nums[i], nums[end]); // swap with the pivot
        return i;
    }

    int findKthLargest(vector<int> &nums, int k)
    {
        // partition like quicksort
        int n = nums.size();
        int start = 0, end = n - 1;
        while (true)
        {
            int p = partition(nums, start, end); // nums[p] is (p+1)th smallest

            // kth largest is (n-k+1)th smallest
            if (p == n - k)
                return nums[p];

            // nums[p] is larger than the target, therefore the target is on the left of p
            if (p > n - k)
                end = p - 1;
            else if (p < n - k) //the target is on the right of p
                start = p + 1;
        }
    }
};

int main()
{
    cout << Solution().findKthLargest(*new vector<int>{3, 1, 2, 4}, 2);
    return 0;
}
