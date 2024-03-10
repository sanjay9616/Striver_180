# Approach 1: Using Stack

class StockSpanner:

    def __init__(self):
        self.span = []
        self.stock = []

    def next(self, price: int) -> int:
        if (self.stock == []):
            self.stock.append(price)
            self.span.append(1)
            return 1
        count = 1
        while (self.stock):
            if (self.stock[-1] <= price):
                count += self.span.pop()
                self.stock.pop()
            else:
                break
        self.stock.append(price)
        self.span.append(count)
        return count

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(2N)
