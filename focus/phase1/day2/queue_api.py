class Qeueu:
    def __init__(self):
        self.queue = []
    
    def push(self, num):
        self.queue.append(num)

    def pop(self):
        return self.queue.pop(0)
    

if __name__ == "__main__":
    test_case = int(input())

    for tc in range(1, test_case + 1):
        queue = Qeueu()

        ans = f"Case #{tc}:"
        c = int(input())

        for _ in range(c):
            val = input().split()

            if val[0] == "1" and len(queue.queue) == 0:
                continue
            elif val[0] == "0":
                queue.push(int(val[1]))
            elif val[0] == "1":
                ret = queue.pop()
                ans += f" {str(ret)}"

        print(ans)