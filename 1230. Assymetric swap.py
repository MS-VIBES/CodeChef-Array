# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=a+b
    c.sort()
    lst=[]
    for i in range(n+1):
        lst.append(c[n+i-1]-c[i])
    print(min(lst))
    