/*
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example:

Input: 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
*/

#include <complex>
#include <unordered_set>

class Solution
{
public:
    bool isHappy(int n)
    {
        if (n <= 0)
            return false;
        std::unordered_set<int> m;
        while (n != 1)
        {
            m.insert(n);
            int s = 0;
            while (n != 0)
            {
                s += pow(n % 10, 2);
                n = n / 10;
            }
            if (m.find(s) != m.end())
                return false;
            n = s;
        }
        return true;
    }

    // an O(1) space solution: to detect the repeat process, instead of using a set,
    // we can use dual pointers method (a slow one and a fast one), just like detecting the cycle in a linked list
};

int main()
{
    Solution().isHappy(2);
    return 1;
}