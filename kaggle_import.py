import cx_Oracle
import csv

username = 'xrot'
password = 'assword'
database = 'localhost' 
connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()

filename = "student-mat.csv"

with open(filename, newline='') as file:
    reader = csv.DictReader(file) 

    
    i = 1
    try:
        for row in reader:
            humanid = i
            i = i + 1
            title = row['school']
            sex = row['sex']
            age = int(row['age'])
            guardian = row['guardian']
            health = int(row['health'])
            dalc = int(row['Dalc'])
            walc = int(row['Walc'])           
        
            query = """INSERT INTO Human(humanid,sex,age,guardian,health) VALUES (:humanid,:sex,:age,:guardian,:health)"""
            cursor.execute(query, humanid = humanid, sex=sex, age = age, guardian = guardian, health=health)	

            query = """INSERT INTO School(humanid,title) VALUES (:humanid,:title)"""
            cursor.execute(query, humanid = humanid, title=title)		

            query = """INSERT INTO AlcoholCons(humanid,walc,dalc) VALUES (:humanid,:walc,:dalc)"""
            cursor.execute(query, humanid = humanid, walc=walc, dalc=dalc)
  

          
    except:
        
        raise
    
    finally:
        
        connection.commit()   
        cursor.close()
        connection.close()
