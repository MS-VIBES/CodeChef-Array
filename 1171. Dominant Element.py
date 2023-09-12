# cook your dish here
from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    x = list(map(int,input().split(' ')))
    c = Counter(x)
    ele_count = [i for i in c.values()]
    max_occ = max(ele_count)
    if len(c) == 1:
        print('YES')
    else:
        if ele_count.count(max_occ) == 1:
            print('YES')
        else:
            print('NO')

        