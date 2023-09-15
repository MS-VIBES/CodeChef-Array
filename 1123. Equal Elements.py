from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    C = Counter(arr)
    maxi = max(C.values())
    print(n - maxi)