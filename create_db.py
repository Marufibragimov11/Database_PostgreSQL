import pandas as pd
import numpy as np

data = pd.read_csv("C:Users\ibrag\Downloads\MOCK_DATA.csv")
day_1 = np.arange(1, 31)

for i in range(1, 501):
    df_1 = data.iloc[0:30]
    df_1.employee_id = i
    df_1.day = day_1
    df_1.month = 'Mart'
    df_1.year = 2022

    df_2 = data.iloc[30:60]
    df_2.employee_id = i
    df_2.day = day_1
    df_2.month = 'Aprel'
    df_2.year = 2022

    df_3 = data.iloc[60:90]
    df_3.employee_id = i
    df_3.day = day_1
    df_3.month = 'May'
    df_3.year = 2022

    con = pd.concat([df_1, df_2, df_3])

    con.to_csv('CLEAN_DATA.csv', mode='a', header=False, index=False)
