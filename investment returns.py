import random as r
class InvestmentReturns:
    def __init__(self, IPO=10000, initial=10000, start=2000, current=2020):
        self._IPO = IPO
        self._initial = initial
        self._start = start
        self._current = current
        self.balance = -initial
        self.dataset = dict()
        
    def populate(self):
        for year in range(self._start, self._current + 1):
            low = int( self._IPO * r.uniform(-1.5, -1) + (year - self._start + r.randint(50, 5000)) * r.uniform(1, 2.5) )
            high = int( self._IPO * r.uniform(1, 3) + (year - self._start + r.randint(1, 50000))* r.uniform(1, 3))
            mReturn = r.randint(low, high)
            self.balance += mReturn
            self.dataset[year] = [mReturn, self.balance]
    def getData(self):
        for year in self.dataset.keys():
            print(f"{year}: £{self.dataset[year][0]} \t\t Balance: {self.dataset[year][1]}")

    def prefix(self):
        n = len(self.dataset)
        A = [0] * n

        for i in range(n):
            total = 0
            for j in range(self._start, self._start + i + 1):
                total = total + self.dataset[j][0]
            A[i] = total/(i + 1)

        for i in range(len(A)):
            print(f"{self._start + i}: {A[i]}")

IPO = r.randint(50000, 1000000)
investment = IPO * r.uniform(1, 2)
initial = r.randint(1980, 2010)
print("IPO:", IPO)
print("Initial investement:", investment)

o = InvestmentReturns(IPO, investment, initial)
o.populate()
o.getData()
print(o.prefix())

    
