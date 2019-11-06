import mysql.connector
connection = mysql.connector.connect(host="localhost",user="testuser",passwd="test123",database="TESTDB")

cursor = connection.cursor()
flag=0
#taking data from output.txt
with open("Output.txt", "r") as fd:
    max=0
    for line in fd:
        if flag!=0:
                parts = line.split()
                info = parts[1]+' '+parts[2]+' '+parts[3]+' '+parts[4]+' '+parts[5]+' '+parts[6]+' '+parts[7]+' '+parts[8]+' '+parts[9]
                slno = int(parts[0])
                gene = parts[10]
                length = int(parts[11])
                a = int(parts[12])
                c = int(parts[13])
                g = int(parts[14])
                t = int(parts[15])
                if(length>max):
                    max=length
                gc = ((g+c)/(a+t+g+c))*100
                print(type(length))
                sql = 'INSERT INTO gene (slno, info, gene, count_A, count_T, count_G, count_C, length, GC) VALUES ({},"{}","{}",{},{},{},{},{},{})'.format(slno, info, gene, a, t, g, c, length, gc)
                #cursor.execute(sql, %(slno, info, gene, a, t, g, c, length, gc))
                cursor.execute(sql)
                #break
        else:
            flag=1
print(max)
connection.commit()
connection.close()