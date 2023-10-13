a=int(input())
n=list(map(int,input().split()))
for i in range(a):
    if n[i]%2==0:
        ind=i
print(ind)