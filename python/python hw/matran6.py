def NhapMT(file):
    f=open(file,'r')
    k=int(f.readline())
    s=list(f.readline())
    return k,s
def convert(list):
    s = [str(i) for i in list]
    res = int("".join(s))
    return(res)
def XuatMT(file,list):
    f=open(file,'w')
    f.write(str(convert(list)))
k,s=NhapMT('KMIN.inp')
i,u=0,k
while i < len(s):
    try:
        int(s[i])
    except ValueError:
        s.remove(s[i])
        i-=1
    else:
        i+=1
s=[int(i) for i in s]
min,vtbd,vtkt,kq,t=1,0,len(s)-k+1,[],False
while len(kq)!=u:
    for x in range(vtbd,vtkt):
        if s[x]==min:
            kq.append(s[x])
            vtbd=x+1
            k-=1
            vtkt,t=len(s)-k+1,True
            break
    if vtbd==vtkt:
        kq.append()
    if not t==True:
        min+=1
    elif t==True:
        t,min=False,0
XuatMT('KMIN.out',kq)