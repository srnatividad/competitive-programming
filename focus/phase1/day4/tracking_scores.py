if __name__ == "__main__":
    test_cases = int(input())
    for tc in range(1, test_cases + 1):
        n = int(input())
        
        hashmap = {}
        for _ in range(n):
            name, score = map(str, input().split())
            name = name.lower()
            score = int(score)
            if name not in hashmap: hashmap[name] = [score]
            else: hashmap[name].append(score)

        ans = f"Case #{tc}:"
        for k, v in sorted(hashmap.items()):
            diff = abs(max(v)-min(v))
            ans += f"\n{k} {diff}"

        print(ans, end='\n')