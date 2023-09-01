b=int(input())
if(b<=10000):
    gs=b+(0.8*b)+(0.2*b)
elif(b>10000 and b<20000):
    gs=b+(0.9*b)+(0.25*b)
elif(b>20000):
    gs=b+(0.95*b)+(0.30*b)
print("%.2f"%gs)