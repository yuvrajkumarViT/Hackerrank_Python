n=int(input())
d={}
for i in range(0,n):
    l=list(map(str,input().split()))
    p={l[0]:[float(l[1]),float(l[2]),float(l[3])]}
    d.update(p)
c=input()
for i in d:
    if(i==c):
        print(format(sum(d.get(i))/3,'.2f'))

