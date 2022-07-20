import psycopg2 as ps
import pickle

try:
    con = ps.connect(host='database-1.cfgq8mkp2air.us-east-1.rds.amazonaws.com',
                     user='postgres',
                     password='iface123',
                     database='test_db',
                     port=5432)
    con.autocommit = True

    # How to select np.array from database and compare with face
    with con.cursor() as cur:
        cur.execute("""SELECT face FROM employees WHERE employee_id = 1""")
        some_array = pickle.loads(cur.fetchone()[0])
        print(some_array)

except Exception as ex:
    print("[ INFO ] Error while working with PostgreSQL", ex)
finally:
    if con:
        con.close()
        print("[ INFO ] PostgreSQL connection closed")