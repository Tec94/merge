def NhapMT(file):
    f=open(file,'r')
    n=int(f.readline())
    return n

def so_thua(n):
    tong,kq,y,test=0,0,n,False
    while test==False:
        for a in range(1,y):
            if (y%a)==0:
                tong+=a
        if tong>y:
            kq=y
            return kq
            break
        else:
            tong=0
        y+=1

def XuatMt(file):
    f=open(file,'w')
    f.write(str(kq))

n=NhapMT('anum.inp')
kq=so_thua(n)
XuatMt('anum.out')
