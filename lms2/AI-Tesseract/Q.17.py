l=[3,1,4]
m=[11,5,9]
l.insert(1,21)
m.insert(0,7)
print(l)
print(m)
L=len(l)
N=[]
for a in range(L):
    N.append(l[a]+m[a])
    print(N)
print(N)