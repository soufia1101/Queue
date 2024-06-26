# Queue Programming Task

## Queue Data Structure Implementation

Implement the Follwing Queues

### 1. Queue Class:

Implement a basic queue class with the following methods:

1. **init**(self): Initialize an empty queue.
2. enqueue(self, item): Add an item to the rear of the queue.
3. dequeue(self): Remove and return the front item from the queue.
4. is_empty(self): Check if the queue is empty.
5. size(self): Return the number of elements in the queue.

### 2. Priority Queue Class:

Implement a priority queue class with the following methods:

1. **init**(self): Initialize an empty priority queue.
2. enqueue(self, item, priority): Add an item to the priority queue with the
   specified priority.
3. dequeue(self): Remove and return the item with the highest priority from the
   queue.
4. is_empty(self): Check if the priority queue is empty.
5. size(self): Return the number of elements in the priority queue.

### 3. Circular Queue Class:

Implement a circular queue class with the following methods:

1. **init**(self, max_size): Initialize an empty circular queue with a maximum size.
2. enqueue(self, item): Add an item to the rear of the circular queue.
3. dequeue(self): Remove and return the front item from the circular queue.
4. is_empty(self): Check if the circular queue is empty.
5. size(self): Return the number of elements in the circular queue.

## Questions

### Question 1: Maze Solver using Queues

Given a maze represented as a 2D grid with start and end points, implement a
program to find the shortest path from the start to the end. Use your Queue class to
efficiently explore possible paths. The maze contains walls represented by '1' and
open paths represented by '0'. Each move can only be made horizontally or
vertically.

### Question 2: Josephus Problem

The Josephus problem is a theoretical problem related to a certain counting-out
game. Participants stand in a circle, and a certain number of participants are
skipped, and then the next person is eliminated. The process is repeated until only
one person remains.
Implement a function josephus(n, k) that takes two parameters, n representing the
number of participants in the circle and k representing the count of participants to
be skipped before eliminating the next person. The function should return the
position of the last remaining person.

#### Example

if n = 7 and k = 3, the function should return 4, as the elimination
process would proceed as follows:

Initial circle: 1 2 3 4 5 6 7

Round 1: Eliminate 3 (skipping 2 and 1)

New circle: 1 2 4 5 6 7

Round 2: Eliminate 6 (skipping 5 and 4)

New circle: 1 2 4 5 7

Round 3: Eliminate 2 (skipping 1 and 4)

New circle: 1 4 5 7

Round 4: Eliminate 7 (skipping 5 and 4)

New circle: 1 4 5

Round 5: Eliminate 1 (skipping 4 and 5)

New circle: 4 5

Round 6: Eliminate 5 (skipping 4)

Last remaining person: 4

### Question 3: Which One

We take a sequence of characters and enqueue each character to the queue.

When enqued, we expect the character with the highest ascii value to be removed.

You can use any of the above queues(queue, prority queue, circular queue) suited for this question

**init**(self, string): Initialize an queue of your choosing

1. enqueue(self, item): Add an item according to its asscii value into the queue.
2. dequeue(self): Remove and return the item with the highest ascci value from the queue.
3. print(self): Print all characters in the queue.
4. is_empty(self): Check if the circular queue is empty.
5. size(self): Return the number of elements in the circular queue.

#### Example

str = 'ARYAN'

queue = our_queue(str)

queue.print() --> Y, R, N, A, A

queue.enqeue() --> Y
