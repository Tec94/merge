def ReadInp(file):
    f=open(file,'r')
    m=f.readlines()
    m=[x.strip('\n') for x in m]
    print(m)
    return m
def Input(file):
    

m=ReadInp('info.inp')