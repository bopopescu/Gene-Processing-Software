import mysql.connector
connection = mysql.connector.connect(host="localhost",user="testuser",passwd="test123",database="TESTDB")
cursor = connection.cursor()
cursor.execute("SELECT gene,slno,pid FROM gene")
result = cursor.fetchall()

dist1={
 "TTT": 0,
 "TTC": 0,
 "TTA": 0,
 "TTG": 0,
 "CTT": 0,
 "CTC": 0,
 "CTA": 0,
 "CTG": 0,
 "ATT": 0,
 "ATC": 0,
 "ATA": 0,
 "ATG": 0,
 "GTT": 0,
 "GTC": 0,
 "GTA": 0,
 "GTG": 0,
 "TCT": 0,
 "TCC": 0,
 "TCA": 0,
 "TCG": 0,
 "CCT": 0,
 "CCC": 0,
 "CCA": 0,
 "CCG": 0,
 "ACT": 0,
 "ACC": 0,
 "ACA": 0,
 "ACG": 0,
 "GCT": 0,
 "GCC": 0,
 "GCA": 0,
 "GCG": 0,
 "TAT": 0,
 "TAC": 0,
 "TAA": 0,
 "TAG": 0,
 "CAT": 0,
 "CAC": 0,
 "CAA": 0,
 "CAG": 0,
 "AAT": 0,
 "AAC": 0,
 "AAA": 0,
 "AAG": 0,
 "GAT": 0,
 "GAC": 0,
 "GAA": 0,
 "GAG": 0,
 "TGT": 0,
 "TGC": 0,
 "TGA": 0,
 "TGG": 0,
 "CGT": 0,
 "CGC": 0,
 "CGA": 0,
 "CGG": 0,
 "AGT": 0,
 "AGC": 0,
 "AGA": 0,
 "AGG": 0,
 "GGT": 0,
 "GGC": 0,
 "GGA": 0,
 "GGG": 0}

dist2={
 "Ala": ['GCT','GCC','GCA','GCG'],
 "Cys": ['TGT','TGC'],
 "Asp": ['GAT','GAC'],
 "Glu": ['GAA','GAG'],
 "Phe": ['TTT','TTC'],
 'Gly': ['GGT','GGC','GGA','GGG'],
 'His': ['CAT','CAC'],
 'Ile': ['ATT','ATC','ATA'],
 'Lys': ['AAA','AAG'],
 'Leu': ['TTA','TTG','CTT','CTC','CTA','CTG'],
 'Met': ['ATG'],
 'Asn': ['AAT','AAC'],
 'Pro': ['CCT','CCC','CCA','CCG'],
 'Gln': ['CAA','CAG'],
 'Arg': ['AGA','AGG','CGT','CGC','CGA','CGG'],
 'Ser': ['AGT','AGC','TCT','TCC','TCA','TCG'],
 'Thr': ['ACT','ACC','ACA','ACG'],
 'Val': ['GTT','GTC','GTA','GTG'],
 'Trp': ['TGG'],
 'Tyr': ['TAT','TAC']
}

for x in result:
    fk=[]
    for key in dist1.keys():
        dist1[key]=0
    if len(x[0])%3 != 0:
        length = len(x[0]) - len(x[0]) % 3
    else:
        length = len(x[0])
    for i in range(0, length, 3):
        codon = x[0][i]+x[0][i+1]+x[0][i+2]
        dist1[codon]+=1
    for key in dist2.keys():
        ni = []
        pi = []
        for k in dist2[key]:
            ni.append(dist1[k])
        n=sum(ni)
        if n!=0:
            for i in range(len(ni)):
                pi.append(ni[i]/n)
        pi2=list(map(lambda x: x ** 2, pi))
        fk.append(sum(pi2))
    fk=[x for x in fk if x != 0]
    fk = [round(elem, 2) for elem in fk]
    recfk=list(map(lambda x: 1/x, fk))
    reckf = [round(elem, 2) for elem in recfk]
    nc=sum(recfk)
    if x[2] == 1788544:
        print(nc)
    sql = 'UPDATE gene SET nc={} WHERE slno={}'.format(nc, x[1])
    cursor.execute(sql)

connection.commit()
