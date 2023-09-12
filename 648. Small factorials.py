t=int(input())
while(t>0):
    num=int(input())
    if(num==0):
        print('1')
    elif(num==1):
        print('1')
    else:
        f=1
        for i in range(1,num+1):
            f=f*i
        print(f)
    t-=1