# Approach 1: Brute Force

class MedianFinder:
    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        self.stream.append(num)
        self.stream.sort()  # O(N*Log N)

    def findMedian(self) -> float:
        n = len(self.stream)
        if (n % 2 == 0):  # Even Lengthed Stream
            return (self.stream[n // 2 - 1] + self.stream[n // 2]) / 2
        return self.stream[n // 2]  # Odd Lengthed Stream

# Time Coplexicity = O(N * log(N)) => Result = TLE
# Space Complexity = O(1)


# ----------------- Brute Force Optimised ---------------------------- #

class MedianFinder:
    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        for i in range(len(self.stream)):
            if (num <= self.stream[i]):
                self.stream.insert(i, num)
                return
        self.stream.append(num)

    def findMedian(self) -> float:
        n = len(self.stream)
        if (n % 2 == 0):  # Even Lengthed Stream
            return (self.stream[n // 2 - 1] + self.stream[n // 2]) / 2
        return self.stream[n // 2]  # Odd Lengthed Stream

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1)
