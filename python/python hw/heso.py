def NhapMT(file):
    f=open(file,'r')
    n=f.readline()
    he_so_doi=int(f.readline())
    he_so_toi=int(f.readline())
    return n,he_so_doi,he_so_toi
def switch(i):
    switcher={
                '0':'0',
                '1':'1',
                '2':'2',
                '3':'3',
                '4':'4',
                '5':'5',
                '6':'6',
                '7':'7',
                '8':'8',
                '9':'9',
                '10':'A',
                '11':'B',
                '12':'C',
                '13':'D',
                '14':'E',
                '15':'F',
                '16':'10'
            }
    return switcher.get(i,"")
def switch_2(i):
    switcher={
                'A':'10',
                'B':'11',
                'C':'12',
                'D':'13',
                'E':'14',
                'F':'15'
            }
    return switcher.get(i,"")
def reverse(n):
    n=n[::-1]
    return n
def thap_phan_bat_ki(n):
    kq=[]
    ket_qua=''
    n=n.replace('\n','')
    while int(n)>0:
        kq.append(int(n)%he_so_toi)
        n=int(n)//he_so_toi
    kq.reverse()
    for x in kq:
        ket_qua+=switch(str(x))
    return ket_qua
def bat_ki_thap_phan(n):
    n=n.replace('\n','')
    n_reverse=reverse(n)
    ket_qua=0
    for x in range(len(n)):
        '''if n_reverse[x] in ['A','B','C','D','E','F']:
            n_reverse=n_reverse.replace(n_reverse[x],switch_2(n_reverse[x]))
            ket_qua+=(int(n_reverse[x])*(he_so_doi**x))'''
        if n_reverse[x]=='A':
            ket_qua+=(10*(he_so_doi**x))
        elif n_reverse[x]=='B':
            ket_qua+=(11*(he_so_doi**x))
        elif n_reverse[x]=='C':
            ket_qua+=(12*(he_so_doi**x))
        elif n_reverse[x]=='D':
            ket_qua+=(13*(he_so_doi**x))
        elif n_reverse[x]=='E':
            ket_qua+=(14*(he_so_doi**x))
        elif n_reverse[x]=='F':
            ket_qua+=(15*(he_so_doi**x))
        else:    
            ket_qua+=(int(n_reverse[x])*(he_so_doi**x))
    return ket_qua
def bat_ki_bat_ki(n):
    ket_qua=bat_ki_thap_phan(n)
    n=str(ket_qua)
    ket_qua=thap_phan_bat_ki(n)
    return ket_qua
def XuatMT(file):
    f=open(file,'w')
    f.write(str(ket_qua))
n,he_so_doi,he_so_toi=NhapMT('heso.inp')
#ket_qua=thap_phan_bat_ki(n)
#ket_qua=bat_ki_thap_phan(n)
ket_qua=bat_ki_bat_ki(n)
XuatMT('heso.out')