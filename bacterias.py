import math as mt
n=int(input())
maior=0
imaior=0
for i in range(n):
    x,y=map(int, input().split())
    a= y*(mt.log(x,10))
    if(a>maior):
        maior=a
        imaior=i

print(imaior)
