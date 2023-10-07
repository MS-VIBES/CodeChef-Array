# cook your dish here
for _ in range(int(input())):
    s=input()
    a=[]
    for i in range(len(s)-1):
        a.append(s[i:i+2])
    print(len(set(a)))