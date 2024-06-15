import heapq

# Queue Class
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Priority Queue Class
class PriorityQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item, priority):
        heapq.heappush(self.items, (priority, item))

    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.items)[1]
        else:
            raise IndexError("dequeue from empty priority queue")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Circular Queue Class
class CircularQueue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.max_size == self.front:
            raise OverflowError("enqueue on full circular queue")
        elif self.front == -1:  # First element
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty circular queue")
        item = self.queue[self.front]
        if self.front == self.rear:  # Queue has only one element
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return item

    def is_empty(self):
        return self.front == -1

    def size(self):
        if self.is_empty():
            return 0
        elif self.rear >= self.front:
            return self.rear - self.front + 1
        else:
            return self.max_size - self.front + self.rear + 1


# Question 1: Maze Solver using Queues
def maze_solver(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = Queue()
    queue.enqueue((start, [start]))  # (current_position, path)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    while not queue.is_empty():
        (current, path) = queue.dequeue()
        if current == end:
            return path

        for direction in directions:
            next_row, next_col = current[0] + direction[0], current[1] + direction[1]
            if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == '0':
                queue.enqueue(((next_row, next_col), path + [(next_row, next_col)]))
                maze[next_row][next_col] = '1'  # Mark as visited

    return None  # No path found


# Question 2: Josephus Problem
def josephus(n, k):
    queue = Queue()
    for i in range(1, n + 1):
        queue.enqueue(i)

    while queue.size() > 1:
        for _ in range(k - 1):
            queue.enqueue(queue.dequeue())
        queue.dequeue()

    return queue.dequeue()


# Question 3: Which One
class AsciiPriorityQueue:
    def __init__(self, string):
        self.queue = PriorityQueue()
        for char in string:
            self.enqueue(char)

    def enqueue(self, item):
        self.queue.enqueue(item, -ord(item))  # Use negative ASCII value for max-heap behavior

    def dequeue(self):
        return self.queue.dequeue()

    def __str__(self):
        return ', '.join([item for priority, item in self.queue.items])

    def is_empty(self):
        return self.queue.is_empty()

    def size(self):
        return self.queue.size()


# Example usage
if __name__ == "__main__":
    # Maze Solver
    maze = [
        ['0', '1', '0', '0', '0'],
        ['0', '1', '0', '1', '0'],
        ['0', '0', '0', '1', '0'],
        ['0', '1', '1', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    start = (0, 0)
    end = (4, 4)
    path = maze_solver(maze, start, end)
    print(f"Maze path: {path}")

    # Josephus Problem
    n, k = 7, 3
    last_person = josephus(n, k)
    print(f"Last person standing: {last_person}")

    # Which One
    str_input = 'ARYAN'
    ascii_queue = AsciiPriorityQueue(str_input)
    print(f"Queue: {ascii_queue}")  # Output: Y, R, N, A, A
    ascii_queue.enqueue('Z')
    print(f"Dequeued: {ascii_queue.dequeue()}")  # Output: Z
    print(f"Queue after dequeue: {ascii_queue}")
