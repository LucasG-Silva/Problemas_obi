n=int(input())
m=list(map(int, input().split()))
pos=[4,3]
cont=0

for i in m:
    if i == 1:
        pos[0]+=1
        pos[1]+=2
    elif i == 2:
        pos[0]+=2
        pos[1]+=1
    elif i == 3:
        pos[0]+=2
        pos[1]-=1
    elif i == 4:
        pos[0]+=1
        pos[1]-=2
    elif i == 5:
        pos[0]-=1
        pos[1]-=2
    elif i == 6:
        pos[0]-=2
        pos[1]-=1
    elif i == 7:
        pos[0]-=2
        pos[1]+=1
    elif i == 8:
        pos[0]-=1
        pos[1]+=2

    cont+=1

    if(pos==[1,3] or pos==[2,3] or pos==[2,5] or pos==[5,4]):
        break

print(cont)
