def NhapMT(file):
    f=open(file,'r')
    line=f.readline()
    m2 = [int(num) for num in line.split(' ')]
    m = [[int(num) for num in line.split(' ')] for line in f]
    m,n,k=m[0],m2[0],m2[1]
    return n,k,m
def circle(k):
    global max
    max,tong=0,0
    for x in range(k-1):
        m.append(m[x])
    for x in range(len(m)-(k-1)):
        tong=0
        for y in range(k):
            tong+=m[x+y]
        if tong>max:
            max=tong
def XuatMT(file):
    f=open(file,'w')
    f.write(str(max))
    f.close()

n,k,m=NhapMT('circle.inp')
circle(k)
XuatMT('circle.out')