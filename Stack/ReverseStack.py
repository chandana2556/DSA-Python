"""
============================================================
Problem: Reverse a Stack

Description:
Given a stack of integers, reverse the order of its elements.

The top element should become the bottom element, and the
bottom element should become the top element.

Concept:
Stack follows LIFO (Last In, First Out).

Reversing a stack means changing the order of its elements
so that popping them produces the reverse order.

Example:

Input Stack (Bottom -> Top):
[10, 20, 30, 40]

Output Stack (Bottom -> Top):
[40, 30, 20, 10]
============================================================
"""


"""
============================================================
Approach 1: Using an Auxiliary Stack

- Create an empty temporary stack.
- Pop each element from the original stack.
- Push each popped element into the temporary stack.
- Return the temporary stack.

Time Complexity: O(n)
Space Complexity: O(n)
============================================================
"""

def reverse_stack(stack):
    temp = []

    while stack:
        temp.append(stack.pop())

    return temp


"""
============================================================
Approach 2: Using Indexing and an Auxiliary Stack

- Copy elements from the original stack into a new stack
  using indexing.
- Pop elements from the new stack and push them into
  another stack.
- Return the result stack.

Note:
This approach uses two additional stacks and is less
space-efficient in practice than Approach 1.

Time Complexity: O(n)
Space Complexity: O(n)
============================================================
"""

def reverse_stack(stack):
    reversed_stack = []

    for i in range(len(stack)):
        reversed_stack.append(stack[i])

    result = []

    while reversed_stack:
        result.append(reversed_stack.pop())

    return result