import sqlite3
import pandas as pd
connect = sqlite3.connect('../db.sqlite')
# c = connect.curosr()

df = pd.read_sql_query('select * from members where age >= 25', connect)

connect.close()