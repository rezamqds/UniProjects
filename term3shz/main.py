class Interval:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

class UnionFind:
    def __init__(self, n):
        self.parent = {}
        for i in range(1, n + 1):
            self.parent[i] = i

    def find(self, x):
        if x == self.parent[x]:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.parent[x] = y

class ShortestPath:
    def __init__(self, intervals):
        self.intervals = intervals
        self.n = len(intervals)
        self.activeStack = []
        self.specialInactiveStack = []
        self.succ = {}



    def processIntervals(self, i):
        while True:
            interval = self.intervals[i]
            if interval.start > self.succ[interval]:
                break

            if interval.end < self.succ[interval]:
                label = interval.end + interval.weight
                while len(self.specialInactiveStack) and self.specialInactiveStack[-1].end < interval.end:
                    specialInterval = self.specialInactiveStack.pop()
                    if specialInterval.end < self.succ[specialInterval]:
                        self.findAndMerge(specialInterval, label)

                while len(self.activeStack) and self.activeStack[-1].end < interval.end:
                    activeInterval = self.activeStack.pop()
                    if activeInterval.end < self.succ[activeInterval]:
                        self.findAndMerge(activeInterval, label)

                self.pushInactive(interval, label)

            i += 1

    def findAndMerge(self, interval, label):
        setId = self.find(interval.start)
        for k in interval.set:
            self.parent[k] = setId

        #overlap_intervals
        while len(self.specialInactiveStack) and self.specialInactiveStack[-1].end >= interval.end:
            specialInterval = self.specialInactiveStack.pop()
            self.union(interval.start, specialInterval.start)

    def pushInactive(self, interval, label):
        interval.set = []
        for i in range(interval.end + 1, self.succ[interval]):
            interval.set.append(i)

        self.specialInactiveStack.append(interval)

    def computeShortestPaths(self):
        self.processIntervals(1)

        paths = {}
        for interval in self.intervals:
            path = [interval.start]
            while interval.start != 1:
                interval = self.find(interval.start)
                path.append(interval.start)

            paths[interval.end] = path

        return paths

def parse_input(input_string):
    lines = input_string.split("\n")
    n = int(lines[0])
    intervals = []
    for i in range(1, n + 1):
        line = lines[i]
        intervals.append([int(x) for x in line.split(" ")])
    return intervals
def main():
    txt = open("sample.txt", "r")
    input_txt = txt.read()
    intervals = parse_input(input_txt)
    print(intervals)

    # intervals = []
    #
    # n = int(input())
    # for _ in range(n):
    #     start, end, weight = map(int, input().split())
    #     intervals.append(Interval(start, end, weight))

    shortestPaths = ShortestPath(intervals).computeShortestPaths()

    shortestPaths = sorted(shortestPaths.items(), key=lambda x: x[1])
    for i, path in shortestPaths:
        if path[0] != 1:
            print(i, -1)
        else:
            print(i, path[1:])

main()
