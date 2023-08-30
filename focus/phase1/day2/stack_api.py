class Stack:
    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        return self.stack.pop()
    

if __name__ == "__main__":
    test_case = int(input())

    for tc in range(1, test_case + 1):
        stack = Stack()

        ans = f"Case #{tc}:"
        c = int(input())

        for _ in range(c):
            val = input().split()

            if val[0] == "1" and len(stack.stack) == 0:
                continue
            elif val[0] == "0":
                stack.push(int(val[1]))
            elif val[0] == "1":
                ret = stack.pop()
                ans += f" {str(ret)}"

        print(ans)