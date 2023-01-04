def NhapMT(file):
    f=open(file,'r')
    n=int(f.readline())
    return n
def tong(n):
    global num
    tong,num=0,[0,0,0,0,0,0,0,0,0,0]
    for i in range(1, (2*n)):
        if i%2==1:
            tong+=i
    while tong>0:
        num[tong%10]+=1
        tong=tong//10
def XuatMT(file):
    f=open(file,'w')
    for i in num:
        if i!=0:
            f.write(str(num.index(i)))
            f.write(' ')
            f.write(str(i))
            f.write('\n')


n=NhapMT('demso.inp')
tong(n)
XuatMT('demso.out')