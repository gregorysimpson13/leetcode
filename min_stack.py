# 155. Min Stack

# https://leetcode.com/problems/min-stack/

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# [0, -2, -3]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2



class MinStack:
    def __init__(self):
        self.min_storage = []
        self.storage = []

    def push(self, x):
        self.storage.append(x)
        if self.min_storage == []:
            self.min_storage.append(x)
        else:
            for i in range(len(self.min_storage) - 1, -1, -1):
                if self.min_storage[i] > x:
                    self.min_storage.insert(i+1, x)
                    return
            self.min_storage.insert(0, x)
    
    def pop(self):
        self.storage.pop()
        self.min_storage.remove(item)

    def top(self):
        return self.storage[-1]

    def getMin(self):
        return self.min_storage[-1]

    def printStack(self):
        for i in self.min_storage:
            print(i, end=' ')
        print()


# Test Case 1
minstack = MinStack()
minstack.push(-2)
minstack.push(0)
minstack.push(-3)
# minstack.printStack()
print(minstack.getMin(), -3)
minstack.pop()
print(minstack.top(), 0)
print(minstack.getMin(), -2)


# Test Case 2
print("\n\n")
ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-1)
# ms.printStack()
print(ms.getMin(), -2)
print(ms.top(), -1)
ms.pop()
print(ms.getMin(), -2)