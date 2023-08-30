def factorial(n):
    if n == 1:
       return n
    else:
       return n*factorial(n-1)


if __name__ == "__main__":
    test_cases = int(input())
    for tc in range(1, test_cases + 1):
        n = int(input())

        res = factorial(n)
        print(res)