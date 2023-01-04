def NhapMT(file):
    f=open(file,'r')
    line=f.readline()
    k = [int(num) for num in line.split(' ')]
    k2 = f.readlines()
    k2=[x.strip('\n') for x in k2]
    m,n=k[0],k[1]
    return m,n,k2
def dientich():
    l,w,l_max,w_max,brk=1,1,1,1,False
    for x in range(m-1):
        for y in range(n-1):
            i,j=x,y
            while i<m-1:
                while j<n-1:
                    if k2[i][j]!=k2[i][j+1]!=k2[i+1][j]!=k2[i+1][j+1]:
                        l+=1
                    else:
                        brk=True
                        break
                    j+=1
                if brk==True:
                    brk=False
                    break
                w+=1
                i+=1
                if l>l_max and w>w_max:
                    l_max,w_max=l,w
                l,w=1,1
    return l_max,w_max
m,n,k2=NhapMT('dientich.inp')
l_max,w_max=dientich()
print(l_max,w_max)