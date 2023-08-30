class MovingSum():
    def __init__(self):
        self.queue = []
        self.total = 0

    def add(self, num):
        self.total += num
        if len(self.queue) < 10000:
            self.queue.append(num)
        else:
            remove = self.queue.pop(0)
            self.queue.append(num)
            self.total = self.total - remove
    
    def query(self):
        return self.total
    

if __name__ == "__main__":
    test_case = int(input())

    for tc in range(1, test_case + 1):
        movingSum = MovingSum()
        ans = f"Case #{tc}:"
        c = int(input())

        for _ in range(c):
            val = input().split()
            if val[0] == "0":
                movingSum.add(int(val[1]))
            elif val[0] == "1":
                result = movingSum.query()
                ans += f" {str(result)}"
        
        print(ans)