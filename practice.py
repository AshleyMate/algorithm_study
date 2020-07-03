T=int(input())

for i in range(T):
    k=int(input())
    n=int(input())
    base=[j for j in range(1,n+1)]
    for l in range(k):
        for m in range(1,n):
            base[m]+=base[m-1]
            print('m = '+ str(m))
            print(base)
    print(base[n-1])