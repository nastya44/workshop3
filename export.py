import cx_Oracle
import csv

username = 'xrot'
password = 'assword'
database = 'localhost'


connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()

tables = ['School','AlcoholCons','Human','HumanSex','HumanHealth','HumanGuardian','SchoolTitle','AlcoholConsDalc','AlcoholConsWalc'] 


try:
    
    for i in tables:
        with open(i + '.csv', 'w', newline='') as newCreatedFile:
            cursor.execute("SELECT * FROM " + i)
            row = cursor.fetchone()


            titles = []
            for j in cursor.description:
                titles.append(j[0])   
            csv_writer = csv.writer(newCreatedFile, delimiter=',')
            csv_writer.writerow(titles)


           
            while row:
                csv_writer.writerow(row)
                row = cursor.fetchone()


finally:
    cursor.close()
    connection.close()

