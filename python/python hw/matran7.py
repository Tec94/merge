def NhapMT(file):
    f=open(file,'r')
    n=int(f.readline())
    return n
def swap(n):
    global num
    num = [int(x) for x in str(n)]
    min,swap,k,test=1,1,0,False
    while swap>0:
        for x in range(0,len(num)):
            if num[x]==min:
                for y in range(0,x):
                    if num[y]>num[x]:
                        k=num[y]
                        num[y]=num[x]
                        num[x]=k
                        swap-=1
                        break
            elif num[x]!=min:
                test=True
        if test==True:
            min+=1
            test=False
        if min==9:
            break
def convert(list):
    s = [str(i) for i in list]
    res = int("".join(s))
    return(res)
def XuatMT(file,n):
    f=open(file,'w')
    f.write(str(convert(num)))

n=NhapMT('swap.inp')
swap(n)
XuatMT('swap.out',n)
