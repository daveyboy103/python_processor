import pyodbc
from pprint import pprint as pp

try:
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=Northwind;UID=sa;PWD=AskB4ntRy')

    cur = conn.cursor()
    ret = cur.execute('select * from Customers')

    for row in ret:
        pp(row)

    ret = cur.execute('select * from Orders')

    for row in ret:
        pp(row)

finally:
    conn.close()


