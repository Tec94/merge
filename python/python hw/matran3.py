def NhapMT(file):
    f = open(file, 'r')
    line=f.readline()
    dc = [int(num) for num in line.split(' ')]
    b = [[int(num) for num in line.split(' ')] for line in f]
    return dc,b
def add():
    tong=0
    for x in range(dc[0][0]):
        for y in range(dc[0][1]):
            B.append(tong)
            tong=0
            for x1 in range(dc[0][0]):
                for y1 in range(dc[0][1]):
                    if x==x1 or y==y1:
                        pass
                    else:
                        tong+=dc[1][x1][y1]
    B.append(tong)
    B.remove(0)
def XuatMT(file):
    f = f,dem=open(file, 'w'),0
    for r in B:
        if dem>=3:
            f.write('\n')
            f.write(str(r) + ' ')
            dem=0
        else:
            f.write(str(r) + ' ')
        dem+=1
    f.close()

                  
dc,B=NhapMT('data.inp'),[]
add()
XuatMT('ketqua.out')
