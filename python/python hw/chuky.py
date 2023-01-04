def NhapMT(file):
    f=open(file,'r')
    k=f.readline()
    m=[int(num) for num in k.split(' ')]
    i=m[0]
    j=m[1]
    return i,j
def chuky():
    chu_ky,max=[],0
    for n in range(i,j+1):
        len=1
        while n>1:
            if n==1:
                break
            elif n%2==1:
                n=(3*n)+1
                len+=1
            elif n%2==0:
                n=n/2
                len+=1
        chu_ky.append(len)
    for x in chu_ky:
        if x>max:
            max=x
    min=max
    for x in chu_ky:
        if x<min:
            min=x
    ket_qua=max+min
    return ket_qua
def XuatMT(file):
    f=open(file,'w')
    f.write(str(ket_qua))
i,j=NhapMT('chuky.inp')
ket_qua=chuky()
XuatMT('chuky.out')