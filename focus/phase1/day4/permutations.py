stack = []

def swap(letters, x, y):
    letters[x], letters[y] = letters[y], letters[x]

def permutation(letters, l, n):
    if l == n:
        return stack.append("".join(letters))
    else:
        for i in range(l, n + 1, 1):
            swap(letters, l, i)
            permutation(letters, l + 1, n)
            swap(letters, l, i)


if __name__ == "__main__":
    test_cases = int(input())
    for tc in range(1, test_cases + 1):
        letters = ['a','b','c','d','e','f','g','h']
        n = int(input())

        permutation(letters, 0, n-1)

        for i in sorted(stack):
            print(i)

        del stack[:]