a=int(input())
n=list(map(int,input().split()))
avg=sum(n)//a
print(avg in n)