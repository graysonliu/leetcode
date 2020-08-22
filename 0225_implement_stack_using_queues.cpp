/*
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
*/
#include <queue>

using namespace std;

class MyStack
{

public:
    queue<int> Q1;
    queue<int> Q2;

    /** Initialize your data structure here. */
    MyStack()
    {

    }

    /** Push element x onto stack. */
    void push(int x)
    {
        // two queues solution
//        Q2.push(x);
//        while (!Q1.empty())
//        {
//            int i = Q1.front();
//            Q1.pop();
//            Q2.push(i);
//        }
//        swap(Q1, Q2);

        // one queue solution
        int n = Q1.size();
        Q1.push(x); // add x to the end
        for (int i = n; i > 0; --i) // move all elements before x to the end
        {
            Q1.push(Q1.front());
            Q1.pop();
        }
    }

    /** Removes the element on top of the stack and returns that element. */
    int pop()
    {
        int i = Q1.front();
        Q1.pop();
        return i;
    }

    /** Get the top element. */
    int top()
    {
        return Q1.front();
    }

    /** Returns whether the stack is empty. */
    bool empty()
    {
        return Q1.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
