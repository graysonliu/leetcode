/*
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.
*/

#include <algorithm>
#include <iostream>

class Solution
{
public:
    int get_overlap(int a, int b, int c, int d)
    {
        if (a > c)
        {
            std::swap(a, c);
            std::swap(b, d);
        } // make sure that a<=c
        if (b <= c)
            return 0;
        if (d <= b)
            return d - c;
        return b - c;
    }

    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H)
    {
        int area1 = (C - A) * (D - B);
        int area2 = (G - E) * (H - F);
        return -get_overlap(A, C, E, G) * get_overlap(B, D, F, H) + area1 + area2;
    }
};

int main()
{
    std::cout << Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2);
}
