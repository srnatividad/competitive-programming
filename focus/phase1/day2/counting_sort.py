class CountingSort():
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        mn = min(self.arr)
        mx = max(self.arr)
        offset = 10

        if mn < 0:
            offset += abs(mn)

        count_size = offset + (mx + 10)
        size = len(self.arr)
        output = [0] * size
        count = [0] * count_size

        for i in range(0, size):
            count[self.arr[i] + offset] += 1
        
        for j in range(1, count_size):
            count[j] += count[j - 1]

        k = size - 1
        while k >= 0:
            output[(count[self.arr[k] + offset]) - 1] = self.arr[k]
            count[self.arr[k] + offset] -= 1
            k -= 1

        for z in range(0, size):
            self.arr[z] = output[z]
        
        return " ".join(map(str,self.arr))


if __name__ == "__main__":
    test_case = int(input())

    for tc in range(1, test_case + 1):
        n = int(input())
        st = list(map(int, input().split()))
        
        countingSort = CountingSort(st)

        cs = countingSort.sort()
        print(f"Case #{tc}: {cs}", end="\n")