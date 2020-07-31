#include <vector>
#include <iostream>
#include <cmath>

/*
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
*/

class Solution
{
public:
    int countPrimes(int n)
    {
        // Sieve of Eratosthenes
        // https://assets.leetcode.com/static_assets/public/images/solutions/Sieve_of_Eratosthenes_animation.gif
        std::vector<bool> is_prime(n, true);
        // all numbers are considered as prime at first, therefore all elements are initialized as true
        int count = 0;

        double sq = sqrt(n);

        for (int i = 2; i < n; ++i)
        {
            if (is_prime[i])
            {
                count += 1;

                // since the inner iteration should satisfy j=i*i<n
                // we don't have to consider the situation of i>=sqrt(n)
                // this is also to avoid overflow since i*i could be very big
                // also, we use i>=sqrt(n) here rather than i*i>=n to make sure overflow does not happen
                if (i >= sq)
                    continue;

                for (int j = i * i; j < n; j += i)
                {
                    // we initialize j as i*i rather than i*2 (i.e. i+i)
                    // since for any i*m, if m<i, we have already checked is_prime[i*m] when iterating on m
                    is_prime[j] = false;
                }
            }
        }
        return count;
    }
};

int main()
{
    std::cout << Solution().countPrimes(0);
    return 0;
}
