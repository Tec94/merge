def NhapMT(file):
    f=open(file,'r')
    line=f.readline()
    m = [int(num) for num in line.split(' ')]
    m2 = [[int(num) for num in line.split(' ')] for line in f]
    m,n,x=m[0],m[1],m2[0]
    m2.remove(m2[0])
    return m,n,m2,x

def matran():
    matrix,max,d,test,loop=[],1,1,True,True
    for i in range(m):
        a=[]
        for j in range(n):
            a.append(0)
        matrix.append(a)
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end = " ")
        print()   
    for x in range(m):
        for y in range(n):
            for j in range(len(m2)):
                if x==m2[j][0] and y==m2[j][1]:
                    matrix[x][y]=1
    try:
        for i in range(m):
            d=1
            for j in range(n):
                if test==True:
                    while loop:
                        for x in range(i,i+d+1):
                            for y in range(j,j+d+1):
                                if matrix[x][y]==1:
                                    test,loop=False,False
                                    break
                            max=d
                            d+=1
                elif test==False:
                    test=True
    except IndexError:
        pass
    print(max)

m,n,m2,x=NhapMT('board.inp')
matran()