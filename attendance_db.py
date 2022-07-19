import psycopg2 as ps

try:
    con = ps.connect(host='127.0.0.1',
                     user='postgres',
                     password='11082004m',
                     database='test',
                     port=5432)
    con.autocommit = True

    # # csv file to sql
    with con.cursor() as cur:
        sql2 = '''COPY attendance(employee_id, day, month, year, time)
        FROM 'D:\python\Company\Database_PostgreSQL\CLEAN_DATA.csv'
        DELIMITER ','
        CSV HEADER;'''

        cur.execute(sql2)
        print("Table created successfully")

except Exception as ex:
    print("[ INFO ] Error while working with PostgreSQL: ", ex)
finally:
    if con:
        con.close()
        print("[ INFO ] PostgreSQL connection closed")
