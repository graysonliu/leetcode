# You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.
#
# If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.
#
# Operations allowed:
#
# Fill any of the jugs completely with water.
#     Empty any of the jugs.
# Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
# Example 1: (From the famous "Die Hard" example)
#
# Input: x = 3, y = 5, z = 4
# Output: True
# Example 2:
#
# Input: x = 2, y = 6, z = 5
# Output: False
#
#
# Constraints:
#
# 0 <= x <= 10^6
# 0 <= y <= 10^6
# 0 <= z <= 10^6

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # steps:
        # 1. fill jug x to full
        # 2. pour water from jug x to jug y util y is full or x is empty
        # 3. if y is full, empty it, then repeat step 2, else if x is empty, fulfill x, then repeat step 2
        if z == 0:
            return True
        if x == 0:
            return z == y
        if y == 0:
            return z == x
        v_x, v_y = 0, 0
        possible_z = {0, x, y, x + y}
        while True:
            possible_z.update([v_x, v_y, v_x + v_y])
            if v_y == y:  # if jug y is full
                v_y = 0  # empty it first
            if v_x == 0:  # if x is empty
                v_x = x  # fill jug x
            # pour water from x to y
            v_x, v_y = v_x - min(v_x, y - v_y), v_y + min(v_x, y - v_y)
            # after pouring, if x becomes empty and y is full
            # in the next round, y will be emptied and then both x and y are empty, which returns to the initial status
            if v_x == 0 and v_y == y:
                break
        return z in possible_z

        # mathematical solution
        # z should satisfy that a * x + b * y = z
        # which means z should be a multiple of the the greatest common divisor (GCD) of x and y
        if x + y < z:  # z cannot be larger than x+y
            return False
        # note: gcd(a,0)=a, gcd(0,0)=0
        if x == 0 and y == 0:
            return z == 0
        import math
        return z % math.gcd(x, y) == 0

        # my own version of gcd: Euclid's algorithm
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        return z % gcd(x, y) == 0


print(Solution().canMeasureWater(x=0, y=2, z=1))
