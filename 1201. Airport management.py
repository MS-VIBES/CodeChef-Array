# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    arrival=list(map(int,input().split()))
    departure=list(map(int,input().split()))
    c=arrival + departure
    dictionary={}
    for i in c:
        if i not in dictionary:
            dictionary[i] =  1 
        else:
            dictionary[i] = dictionary[i]+ 1 
            
    s=0
    for i in dictionary:
        if dictionary[i] >s:
            s=dictionary[i]
    print(s)