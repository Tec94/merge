def NhapMT(file):
    f=open(file,'r')
    t=f.readline()
    k=f.readlines()
    m,he_so_doi=[],2
    for x in range(1,len(k),2):
        m.append(k[x].rstrip())
    return t,m,he_so_doi
def reverse(n):
    n=n[::-1]
    return n
def bat_ki_thap_phan(m):
    m_reverse,ket_qua,kq=[],0,[]
    for x in m:
        m_reverse.append(reverse(x))
    for x in range(len(m)):
        for y in range(len(m[x])):
            ket_qua+=(int(m_reverse[x][y])*(he_so_doi**y))
        if ket_qua%15==0:
            kq.append(1)
        else:
            kq.append(0)
        ket_qua=0
    return kq
t,m,he_so_doi=NhapMT('ch15.inp')
kq=bat_ki_thap_phan(m)
print(kq)