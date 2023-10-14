a=int(input())
n=list(map(int,input().split()))
s=0
for i in range(1,a-1):
    if n[i]%2!=0 and n[i-1]%2==0 and n[i+1]%2==0:
        s+=1
print(s)