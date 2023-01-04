def NhapMT(file):
    f=open(file,'r')
    n=str(f.readline())
    return n
def DL(n):
    dem,a,b=1,0,0
    while n!='6174':
        a=sorted(n,reverse=True)
        a=''.join([str(x) for x in a])
        b=sorted(n)
        b=''.join([str(x) for x in b])
        n=int(a)-int(b)
        n=str(n)
        dem+=1
    return dem
def XuatMT(file):
    f=open(file,'w')
    f.write(str(dem))

n=NhapMT('DL6174.inp')
dem=DL(n)
XuatMT('DL6174.out')