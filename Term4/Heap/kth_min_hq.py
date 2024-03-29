"""
Python program to find k-th smallest
element in Min Heap using another
Min Heap (Or Priority Queue)
"""
import heapq

# Structure for the heap
class Heap:
    def __init__(self, n):
        self.v = [0] * n
        self.n = n
 
# Returns the index of
# the left child node
def left(i):
    return 2 * i + 1

# Returns the index of
# the right child node
def right(i):
    return 2 * i + 2
def findKthSmalles(h, k):

    # Create a Priority Queue
    p = []
 
    # Insert root into the priority queue
    heapq.heappush(p, (h.v[0], 0))
 
    for i in range(k - 1):
        j = heapq.heappop(p)[1]
        l, r = left(j), right(j)
        if l < h.n:
            heapq.heappush(p, (h.v[l], l))
        if r < h.n:
            heapq.heappush(p, (h.v[r], r))
 
    return p[0][0]



def main():
    h = Heap(7)
    h.v = [10, 50, 40, 75, 60, 65, 45]
    k = 4
    print(findKthSmalles(h, k))
 
 
main()