/*
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
*/
#include <string>
#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int calculate(string s)
    {
        vector<int> stack;
        string ops = "+-*/";
        char pre_op = '+';
        int num = 0;
        for (int i = 0; i < s.size(); ++i)
        {
            char c = s[i];
            if (c >= '0' && c <= '9')
            {
                num = 10 * num + (c - '0');
            }
            if (ops.find(c) != string::npos ||
                i == s.size() - 1) // we reach the next operation symbol or the end of the string
            {
                switch (pre_op)
                {
                    case '+':
                        stack.push_back(num);
                        break;
                    case '-':
                        stack.push_back(-num);
                        break;
                    case '*':
                        stack.back() *= num;
                        break;
                    case '/':
                        stack.back() /= num;
                        break;
                }
                num = 0;
                pre_op = c;
            }
        }
        int res = 0;
        for (int &i :stack)
            res += i;
        return res;
    }
};

int main()
{
    cout << Solution().calculate("3+2*2") << endl;
    return 0;
}
