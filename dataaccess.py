from pprint import pprint as pp

import pyodbc

with pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=Northwind;UID=sa;PWD=AskB4ntRy') as conn:
    cur = conn.cursor()
    ret = cur.execute('GetCustomers')

    for row in ret:
        pp(row)

    ret = cur.execute('select * from Orders')

    for row in ret:
        pp(row)
