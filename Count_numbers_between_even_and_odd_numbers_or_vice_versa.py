a=int(input())
n=list(map(int,input().split()))
s=0
c=0
for i in range(0,a-2):
    if n[i]%2!=0 and n[i+2]%2==0:
        s+=1
    elif n[i]%2==0 and n[i+2]%2!=0:
        c+=1
print(s+c)