/*
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
*/

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_map>

using namespace std;


class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_map<string, int> count;
        vector<string> res;
        for (int i = 0; i + 9 < s.size(); i++) {
            string sub = s.substr(i, 10);
            count[sub] += 1;
            if (count[sub] == 2)
                res.push_back(sub);
        }
        return res;
    }
};
