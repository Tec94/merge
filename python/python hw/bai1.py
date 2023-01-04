def NhapMT(file):
    f=open(file,'r')
    n=int(f.readline())
    line=f.readline()
    lst=[int(temp) for temp in line.split(' ')]
    return n,lst

def Set():
    global be_hon,lon_hon
    be_hon,lon_hon=0,0
    num=0
    for x in lst:
        if int(x)-(len(lst)//2)<1:
            num=int(x)
    for x in lst:
        if x<num:
            be_hon+=1
        elif x>num:
            lon_hon+=1

def XuatMT(file):
    f=open(file,'w')
    if be_hon==lon_hon:
        f.write('1')
    else:
        f.write('0')


n,lst=NhapMT('set.inp')
Set()
XuatMT('set.out')