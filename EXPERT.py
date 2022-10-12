# cook your dish here
for i in range(int(input())):
    x,y=map(int,input().split())
    per=x/2
    if(y>=per):
        print("YES")
    else:
        print("NO")
