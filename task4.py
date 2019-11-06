import mysql.connector
connection = mysql.connector.connect(host="localhost",user="testuser",passwd="test123",database="TESTDB")
cursor = connection.cursor()
cursor.execute("SELECT gene,slno FROM gene")
result = cursor.fetchall()

proDict = {'U': {'U': {'U': 'F', 'C': 'F', 'A': 'L', 'G': 'L'},'C': {'U': 'S', 'C': 'S', 'A': 'S', 'G': 'S'},'A': {'U': 'Y', 'C': 'Y', 'A': 'Stop', 'G': 'Stop'},'G': {'U': 'C', 'C': 'C', 'A': 'Stop', 'G': 'W'}},
           'C': {'U': {'U': 'L', 'C': 'L', 'A': 'L', 'G': 'L'},'C': {'U': 'P', 'C': 'P', 'A': 'P', 'G': 'P'},'A': {'U': 'H', 'C': 'H', 'A': 'Q', 'G': 'Q'},'G': {'U': 'R', 'C': 'R', 'A': 'R', 'G': 'R'}},
           'A': {'U': {'U': 'I', 'C': 'I', 'A': 'I', 'G': 'M'},'C': {'U': 'T', 'C': 'T', 'A': 'T', 'G': 'T'},'A': {'U': 'N', 'C': 'N', 'A': 'K', 'G': 'K'},'G': {'U': 'S', 'C': 'S', 'A': 'R', 'G': 'R'}},
           'G': {'U': {'U': 'V', 'C': 'V', 'A': 'V', 'G': 'V'},'C': {'U': 'A', 'C': 'A', 'A': 'A', 'G': 'A'},'A': {'U': 'D', 'C': 'D', 'A': 'E', 'G': 'E'},'G': {'U': 'G', 'C': 'G', 'A': 'G', 'G': 'G'}}}
for x in result:
    i=3
    y = x[0].replace('T','U')
    pro =proDict[y[0]][y[1]][y[2]]
    seq=pro
    if len(y)%3==0:
        for i in range(0, len(y), 3):
            if seq == 'Stop':
                print('Stop occured in the middle of "{}"'.format(x[1]))
            seq = proDict[y[i]][y[i + 1]][y[i + 2]]
            pro = pro + seq

    sql='UPDATE gene SET protein="{}" WHERE slno={}'.format(pro,x[1])
    cursor.execute(sql)
    #print(pro)
connection.commit()