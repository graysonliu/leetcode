/*
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
        Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should
also have finished course 1. So it is impossible.


Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
*/
#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

class Solution
{
public:

    bool canFinish(int numCourses, vector<vector<int>> &prerequisites)
    {
        // this is actually to detect whether there is a cycle in the directed graph
        // topological sorting
        // construct the graph
        unordered_map<int, vector<int>> G;
        vector<int> in_degree(numCourses, 0);
        for (auto &pre : prerequisites)
        {
            G[pre[1]].push_back(pre[0]);
            in_degree[pre[0]] += 1;
        }
        // bfs
        queue<int> Q;
        int n = numCourses; // courses left to be studied
        // start with nodes that has zero in-degree
        // courses in Q are ready to be studied since all their prerequisites are satisfied (in-degree equals to 0)
        for (int i = 0; i < numCourses; ++i)
        {
            if (in_degree[i] == 0)
                Q.push(i);
        }
        while (!Q.empty())
        {
            int course = Q.front();
            Q.pop();
            n--; // a course is studied, the number of courses left to be studied decreased by 1
            for (auto i: G[course])
            {
                if (--in_degree[i] == 0)
                    Q.push(i);
            }
        }
        return n == 0; // n equals to 0 means all courses are studied
    }
};