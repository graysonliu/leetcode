# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
#
# Each LED represents a zero or one, with the least significant bit on the right.
#
#
# For example, the above binary watch reads "3:25".
#
# Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
#
# Example:
#
# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
# Note:
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

from typing import List


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        hour_list = [2 ** i for i in range(4)]
        minute_list = [2 ** i for i in range(6)]

        from queue import Queue

        def bfs(choices, i, result):
            Q = Queue()
            Q.put((0, 0, 0))  # queue item is (summation, layer, search_start_index)
            # search first i layers
            while not Q.empty():
                summation, layer, search_start_index = Q.get()
                if layer == i:
                    result.add(summation)
                    continue
                for j, c in enumerate(choices[search_start_index:]):
                    Q.put((summation + c, layer + 1, search_start_index + j + 1))

        # suppose we have i LEDs on in the hour row
        for i in range(min(num + 1, 5)):  # it cannot be larger than 4
            # we need to select i numbers from hour_list, then get their summation
            # using bfs, since we only need to search first i layers of the tree
            possible_hours = set()
            possible_minutes = set()
            bfs(hour_list, i, possible_hours)
            bfs(minute_list, num - i, possible_minutes)
            # print(possible_hours, possible_minutes)
            for hour in possible_hours:
                for minute in possible_minutes:
                    if hour < 12 and minute < 60:
                        res.append(f'{hour}:{minute if minute >= 10 else f"0{minute}"}')
        return res

        # a very simple one-line solution from leetcode discussion
        # covert hour number and minute number to binary strings and count how many '1's they have
        return ['%d:%02d' % (h, m)
                for h in range(12) for m in range(60)
                if (bin(h) + bin(m)).count('1') == num]


print(Solution().readBinaryWatch(2))
