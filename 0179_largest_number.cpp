/*
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
*/


#include <string>
#include <vector>
#include <algorithm>

using namespace std;


class Solution {
public:

    string largestNumber(vector<int> &nums) {
        vector<string> s_vec;
        for_each(nums.begin(), nums.end(), [&s_vec](const int &num) { s_vec.push_back(to_string(num)); });
        sort(s_vec.begin(), s_vec.end(), [](const string &a, const string &b) { return a + b > b + a; });
        string res;
        for_each(s_vec.begin(), s_vec.end(), [&res](const string &s) { res += s; });
        return res[0] == '0' ? "0" : res;
    }
};
