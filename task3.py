import mysql.connector
connection = mysql.connector.connect(host="localhost",user="testuser",passwd="test123",database="TESTDB")
cursor = connection.cursor()
i=0
geneDict = {}
with open("GeneDetails.txt","r") as fd:
    for line in fd:
        if i == 3:
            line = line.split()
            geneDict[line[0]] = [line[index] for index in range(1,len(line))]
        else:
            i+=1

cursor.execute("SELECT * FROM gene")
myresult = cursor.fetchall()
for row in myresult:
    r=row[1].split()
    index=r[0].find(':')
    location= r[0][index+1:]
    if location.find(',')!= -1:
        cursor.execute("DELETE FROM gene WHERE slno = {}".format(row[0]))
        print(location)
        connection.commit()
    elif location[0]=='c':
        location=location.split('-')
        location=location[1]+'..'+location[0][1:]
        try:
            strand=geneDict[location][0]
            length=geneDict[location][1]
            pid=geneDict[location][2]
            gene=geneDict[location][3]
            synonym=geneDict[location][4]
            code=geneDict[location][5]
            cog=geneDict[location][6]
            product=" ".join(geneDict[location][7:])
        except:
            print('error')
        else:
            print(location,strand,int(pid),gene,synonym,code,cog,product,row[0])
            sql='UPDATE gene SET location="{}",strand="{}",pid={},geneshort="{}",synonym="{}",code="{}",cog="{}",product="{}" WHERE slno={}'.format(location,strand,int(pid),gene,synonym,code,cog,product,row[0])
            cursor.execute(sql)
            connection.commit()
    else:
        location = location.split('-')
        location = location[0] + '..' + location[1]
        try:
            strand = geneDict[location][0]
            length = geneDict[location][1]
            pid = geneDict[location][2]
            gene = geneDict[location][3]
            synonym = geneDict[location][4]
            code = geneDict[location][5]
            cog = geneDict[location][6]
            product = " ".join(geneDict[location][7:])
        except:
            print('error')
        else:
            print(location, strand, int(pid), gene, synonym, code, cog, product, row[0])
            sql = 'UPDATE gene SET location="{}",strand="{}",pid={},geneshort="{}",synonym="{}",code="{}",cog="{}",product="{}" WHERE slno={}'.format(location,strand,int(pid),gene,synonym,code,cog,product,row[0])
            cursor.execute(sql)
            connection.commit()

