# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.
#
# Example:
#
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def recur(nums, s):
            if len(nums) == 4:
                if len(s) == 0:
                    res.append('.'.join(nums))
                else:
                    return
            elif len(s) > 0:
                if s[0] == '0':
                    recur(nums + [s[0]], s[1:])
                else:
                    for i in range(1, 4):
                        if i <= len(s) and 0 <= int(s[:i]) <= 255:
                            recur(nums + [s[:i]], s[i:])

        recur([], s)
        return res


print(Solution().restoreIpAddresses("25525511135"))
