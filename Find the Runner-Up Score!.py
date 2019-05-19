n=int(input())
k=list(map(int,input().split()))

j=max(k)
q=[]
for i in k:
    if i!=j:
        q.append(i)

print(max(q))
