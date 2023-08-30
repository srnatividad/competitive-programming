if __name__ == "__main__":
    test_cases = int(input())
    for tc in range(1, test_cases + 1):
        n = int(input())
        arr = list(map(str, input().split()))

        hashmap = {}
        for x in arr:
            if x not in hashmap: 
                hashmap[x] = 1
            else: 
                hashmap[x] += 1
        
        total = 0
        for k, v in hashmap.items():
            if v > 1: 
                total += v
        
        print(f"Case #{tc}: {total}")