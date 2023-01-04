def NhapMT(file):
    f=open(file,'r')
    n=int(f.readline())
    k=int(f.readline())
    line=f.readline()
    lst=[]
    for _ in range(0,n): 
        lst.append([int(num) for num in line.split(' ')])
        line=f.readline()
    return n,k,lst
def min_max():
    min,max,dem=lst[k-1][1],lst[k-1][1],0
    for x in range(1,len(lst[k-1]),2):
        if lst[k-1][x]<min:
            min=lst[k-1][x]
        elif lst[k-1][x]>max:
            max=lst[k-1][x]
    min_2,max_2=min,max
    for x in range(0,3):
        for y in range(1,len(lst[x]),2):
            if lst[x][y]<min:
                min_2=lst[x][y]
            elif lst[x][y]>max:
                max_2=lst[x][y]
        if min_2<min and max_2>max:
            dem+=1
    return dem-1
def XuatMT(file):
    f=open(file,'w')
    f.write(str(dem))

n,k,lst=NhapMT('poly.inp')
dem=min_max()
XuatMT('poly.out')