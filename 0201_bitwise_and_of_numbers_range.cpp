/*
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
*/

class Solution
{
public:
    int rangeBitwiseAnd(int m, int n)
    {
        // for any two consecutive numbers, one is odd and another one is even
        // the last bit of these two numbers are 1 and 0 individually
        // so, the last bit of the AND result should be 0

        int step = 0;
        while (m != n) // if m==n, then we get the same leading part that m and n share
        {
            m = m >> 1;
            n = n >> 1;
            step++;
        }
        return m << step;
    }
};
