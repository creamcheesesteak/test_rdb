import sqlite3
import pandas as pd
connect = sqlite3.connect('../db.sqlite')
# c = connect.curosr()

df_mask = pd.read_sql_query("select title from polls_economics where title like '%마스크%'", connect)
df_labor = pd.read_sql_query("select title from polls_economics where title like '%노동%'", connect)
df_income = pd.read_sql_query("select title from polls_economics where title like '%소득%'", connect)

# print(df_mask)
df_mask.info()
df_mask.to_sql('mask_table', connect, if_exists='replace')

print('---------------------')
df_labor.info()
df_labor.to_sql('labor_table', connect, if_exists='replace')
print('---------------------')
df_income.info()
df_income.to_sql('income_table', connect, if_exists='replace')

connect.close()