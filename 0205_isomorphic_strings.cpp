/*
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
*/

#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution
{
public:
    bool isIsomorphic(string s, string t)
    {
        // bijection
        unordered_map<char, char> map;
        unordered_set<char> used;
        for (int i = 0; i < s.size(); ++i)
        {
            if (map.find(s[i]) == map.end())
            {
                if (used.find(t[i]) != used.end())
                    return false;
                map[s[i]] = t[i];
                used.insert(t[i]);
                continue;
            }
            else if (map[s[i]] != t[i])
                return false;
        }
        return true;
    }
};
