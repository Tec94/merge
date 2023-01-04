def NhapMT(file):
    f = open(file, 'r')
    b = [[int(num) for num in line.split(' ')] for line in f]
    return b
def reverse(x):
    y=0
    while x>0:
        r = x%10
        y = (y*10) + r
        x = x//10
    return y
def rev(m):
    for x in range(len(m[0])):
        for y in range(len(m[0])):
            m[x][y] = reverse(m[x][y])
def s_lon_nhat():
    global s_max
    s_max,max=0,0
    for x in range(len(m[0])):
        for y in range(len(m[0])):
            if m[x][y]>max:
                max=m[x][y]
    for x in range(len(m[0])):
        for y in range(len(m[0])):
            if m[x][y]>s_max and m[x][y]<max:
                s_max=m[x][y]
def sap_xep(m):
    chan,le=[],[]
    for x in m:
        if int(x)%2==0:
            chan.append(x)
        else:
            le.append(x)
    print(chan,"\n", le)
def sort(m):
    chan,le=[],[]
    for x in range(len(m[0])):
        for y in range(len(m[0])):
            if m[x][y]%2==0:
                chan.append(m[x][y])
            else:
                le.append(m[x][y])
    chan,le,dem_c,dem_l = sorted(chan),sorted(le),0,0
    for x in range(len(m[0])):
        for y in range(len(m[0])):
            if dem_c<len(chan):
                m[x][y]=chan[dem_c]
                dem_c+=1
            else:
                m[x][y]=le[dem_l]
                dem_l+=1
def sq_be_nhat():
    global min,xpos,ypos
    max,min,xpos,ypos=0,0,0,0
    for x in range(len(m[0])-2):
        for y in range(len(m[0])-2):
            if (int(m[x][y]) + int(m[x+1][y]) + int(m[x][y+1]) + int(m[x+1][y+1])) > max:
                max=int(m[x][y]) + int(m[x+1][y]) + int(m[x][y+1]) + int(m[x+1][y+1])
                min=max
    for x in range(len(m[0])-2):
        for y in range(len(m[0])-2):
            if (int(m[x][y]) + int(m[x+1][y]) + int(m[x][y+1]) + int(m[x+1][y+1])) < min:
                min,xpos,ypos=int(m[x][y]) + int(m[x+1][y]) + int(m[x][y+1]) + int(m[x+1][y+1]),x,y
    return int(m[xpos][ypos]),int(m[xpos][ypos+1]),int(m[xpos+1][ypos]),int(m[xpos+1][ypos+1])
def XuatMT(file):
    f,dem=open(file, 'w'),0
    f.write(str(s_max))
    f.write('\n''\n')
    for r in m:
        for c in r:
            f.write(str(c) + ' ')
        f.write('\n')
    f.write('\n')
    for r in min:
        if dem>=2:
            f.write('\n')
            f.write(str(r) + ' ')
            dem=0
        else:
            f.write(str(r) + ' ')
        dem+=1
    f.close()

m = NhapMT('data.inp')
sq_be_nhat() # min
min = sq_be_nhat()
rev(m) # m
s_lon_nhat() # s_max
m = NhapMT('data.inp')
sort(m)
XuatMT('ketqua.out')

