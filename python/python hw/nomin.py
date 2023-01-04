def NhapMT(file):
    f=open(file,'r')
    n=int(f.readline())
    m=f.readlines()
    return n,m
def nomin(m):
    m=[x.strip('\n') for x in m]
    m=[int(x) for x in m]
    global dem
    dem,vt=0,0
    while vt<=n-1:
        for x in range(vt+1,n):
            if (m[x]>m[x-1]) and (m[x]!=0) and (m[x-1]!=0):
                vt=x
            else:
                break
        for x in range(vt+1,n):
            if (m[x]<m[x-1]) and (m[x]!=0) and (m[x-1]!=0):
                vt=x
            else:
                break
        if m[vt]!=0:
            dem+=1
        vt+=1
def XuatMT(file):
    f=open(file,'w')
    f.write(str(dem))
n,m=NhapMT('nomin.inp')
nomin(m)
XuatMT('nomin.out')