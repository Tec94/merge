def NhapMT(file):
    f=open(file, 'r')
    b=f.readlines()
    return b
def switcher(i):
    switcher={
                '0000':'0',
                '0001':'1',
                '0010':'2',
                '0011':'3',
                '0100':'4',
                '0101':'5',
                '0110':'6',
                '0111':'7',
                '1000':'8',
                '1001':'9',
                '1010':'A',
                '1011':'B',
                '1100':'C',
                '1101':'D',
                '1110':'E',
                '1111':'F'
            }
    return switcher.get(i,"")
def binary_to_hex(m):
    dem,lst,res=0,"",[]
    if len(m)%4==0:
        pass
    else:
        while len(m)%4!=0:
            m = "0" + m
    m = m + "0"
    for x in m:
        if dem==4:
            res.append(switcher(lst))
            dem,lst=0,""
        lst = lst + str(x)
        dem+=1
    print(res)
def sap_xep(m):
    chan,le=[],[]
    for x in m:
        if int(x)%2==0:
            chan.append(x)
        else:
            le.append(x)
    print(chan,"\n", le)
m = NhapMT('data.inp')
sap_xep(m)