import cx_Oracle
import chart_studio
import re

chart_studio.tools.set_credentials_file(username='nastya44', api_key='dDGMdlHnUcyJpzhNeH4S')


import plotly.graph_objects as go
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dash


def getFileid(url):
    fileId = re.findall("~[0-z.]+/[0-9]+", url)[0][1:]
    return fileId.replace('/', ':')


username = 'Xrot'
password = 'assword'
database = 'localhost'


connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()



#query1
print("Вивести Школу(Назву) - середній рівень здоров'я учнів школи(Запит1).\n")
names = []
values = []
query = """
SELECT title,AVG(health)
From human_info
Group by title
"""


cursor.execute(query) 


for row in cursor.fetchall():
    names.append (row[0])
    values.append(row[1]) 
bar = go.Bar (x = names, y = values)
bar = py.plot([bar],auto_open = True)


#query2
print("Кіл-ть алкоголя в день - % людей 15 років для кожного з рівнів споживання алкоголю.(Запит2)\n")
names = []
values = []
query = """
select t2.dalc, t2.sum/t1.total * 100 as percent
from
(
Select sum(age) as total
From Human_info
where age = 15
)t1,
(
Select dalc,sum(age) as sum
From Human_info
where age = 15
Group by dalc
)t2
"""


cursor.execute(query)

for row in cursor.fetchall():
    names.append (row[0])
    values.append(row[1]) 
pie = go.Pie (labels = names, values = values)
pie = py.plot([pie],auto_open = True)


#query3
print("Динаміка споживання кіл-ті алкоголю в вихідні відносно віку людини.(Запит3)\n")
names = []
values = []
query = """
Select age, avg(walc) as avg
From Human_info
Group by age
Order by age
"""


cursor.execute(query) 
for row in cursor.fetchall():
    names.append (row[0])
    values.append(row[1]) 
scatter = go.Scatter (x = names, y = values)
scatter = py.plot([scatter],auto_open = True)


dashboard = dash.Dashboard()
barid = getFileid(bar)
pieid = getFileid(pie)
scatterid = getFileid(scatter)


frame1= {'type': 'box',
    'boxType': 'plot',
    'fileId': barid,
    'title': ' 1'}


frame2 = {'type': 'box',
    'boxType': 'plot',
    'fileId': pieid,
    'title': ' 2'}


frame3 = {'type': 'box',
    'boxType': 'plot',
    'fileId': scatterid,
    'title': ' 3'}



dashboard.insert(frame1)
dashboard.insert(frame2, 'left', 1)
dashboard.insert(frame3, 'below', 2)

py.dashboard_ops.upload(dashboard, 'dashboard_ws3')


cursor.close()
connection.close()

