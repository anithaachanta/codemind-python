a=int(input())
n=list(map(int,input().split()))
for i in range(len(n)):
    if n[i]%2!=0:
        ind=i
print(ind)