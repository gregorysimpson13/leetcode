class FreqStack:

    def __init__(self):
        self.stack, self.count = [], defaultdict(int)

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.count[x] += 1
        

    def pop(self) -> int:
        mfreq = max(self.count.values())
        item = iloc = None
        for i in range(len(self.stack) - 1, -1, -1):
            if self.count[self.stack[i]] == mfreq: iloc = i; item = self.stack[i]; break
        self.count[item] -= 1
        return self.stack.pop(iloc)