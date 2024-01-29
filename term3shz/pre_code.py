from heapq import heappush, heappop

class SPF:
    def __init__(self, n):
        self.dist = [float("inf") for _ in range(n)]
        self.parent = [-1 for _ in range(n)]
        self.pq = []

    def push(self, u, d):
        heappush(self.pq, (d, u))

    def pop(self):
        d, u = heappop(self.pq)
        return u

    def update(self, u, d):
        self.dist[u] = d
        self.push(u, d)

def shortest_path(intervals):
    n = len(intervals)
    spf = SPF(n)

    # Initialize SPF for vertex 1
    spf.dist[0] = 0
    spf.push(0, 0)

    # Iterate over all vertices that are not in SPF yet
    for i in range(1, n):
        while spf.dist[i] == float("inf"):
            u = spf.pop()

            # Update distances for all vertices reachable from u
            for j in range(n):
                if intervals[j][0] >= intervals[u][1]:
                    d = spf.dist[u] + intervals[u][2] + intervals[j][2]
                    if d < spf.dist[j]:
                        spf.update(j, d)

    return spf.dist

def parse_input(input_string):
    lines = input_string.split("\n")
    n = int(lines[0])
    intervals = []
    for i in range(1, n + 1):
        line = lines[i]
        intervals.append([int(x) for x in line.split(" ")])
    return intervals

def print_output(output):
    for i, d in enumerate(output):
        print(i, d)

if __name__ == "__main__":
    input_string = "5\n1 2 2\n3 5 3\n6 7 1\n8 10 2\n11 12 3" #test string
    # txt = open("sample.txt", "r")
    # input_txt= txt.read()
    intervals = parse_input(input_string)
    # intervals = parse_input(input_txt)
    output = shortest_path(intervals)
    print_output(output)
