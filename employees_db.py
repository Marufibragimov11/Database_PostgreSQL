import psycopg2 as ps
from os import listdir
from os.path import isfile, join
import pickle
import numpy as np
import cv2
import face_recognition


def convert(filename):
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


mypath = "D:\python\Company\women"
names = [f for f in listdir(mypath) if isfile(join(mypath, f))]

try:
    con = ps.connect(host='127.0.0.1',
                     user='postgres',
                     password='11082004m',
                     database='test',
                     port=5432)
    con.autocommit = True

    # # create table
    # with con.cursor() as cur:
    # cur.execute(
    #     """CREATE TABLE attendance(
    #         id SERIAL PRIMARY KEY,
    #         employee_id SERIAL,
    #         day INT,
    #         month VARCHAR(50),
    #         year INT,
    #         time TIME);""")'

    # # csv file to sql
    # with con.cursor() as cur:
    #     sql2 = '''COPY employees(employee_id, first_name, last_name, age, gender, occupation)
    #     FROM 'D:\python\Company\Database_PostgreSQL\data\MOCK_DATA_3.csv'
    #     DELIMITER ','
    #     CSV HEADER;'''
    #
    #     cur.execute(sql2)
    #     print("Table created successfully")

    # # insert image into database
    # with con.cursor() as cur:
    #     for id_son in range(len(names)):
    #         photo = convert(f"D:\python\Company\men\{names[id_son]}")
    #         binary = ps.Binary(photo)
    #
    #         cur.execute("SELECT employee_id FROM employees WHERE gender = 'Male'")
    #         gender_list = cur.fetchall()
    #
    #         cur.execute("UPDATE employees SET face = (%s) WHERE id = (%s)", ((binary, gender_list[id_son][0])))
    #         print("Successfully joined and encoded")

    # # insert np.ndarray into postgresql
    # with con.cursor() as cur:
    #     cur.execute("SELECT employee_id FROM employees WHERE gender = 'Female'")
    #     id_list = cur.fetchall()
    #
    #     for id_son in range(len(names)):
    #         image = face_recognition.load_image_file(f"D:\python\Company\women\{names[id_son]}")
    #         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #         encoding_image = face_recognition.face_encodings(image)
    #         image_arr = np.array(encoding_image)
    #         pickle_arr = pickle.dumps(image_arr)
    #
    #         cur.execute("UPDATE employees SET face = (%s) WHERE id = (%s)", ((pickle_arr, id_list[id_son][0])))
    #         print("Successfully joined and encoded")

    # # How to select np.array from database and compare with face
    # with con.cursor() as cur:
    #     cur.execute("""SELECT face FROM employees WHERE employee_id = 1""")
    #     some_array = pickle.loads(cur.fetchone()[0])
    #     # print(some_array)
    #
    #     test_image = face_recognition.load_image_file("D:\python\Company\sorted_images\Maruf_Ibragimov.jpg")
    #     test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB)
    #     face_test = face_recognition.face_locations(test_image)[0]
    #     encoded_test = face_recognition.face_encodings(test_image)[0]
    #     cv2.rectangle(test_image, (face_test[3], face_test[0]), (face_test[1], face_test[2]), (20, 214, 17), 2)
    #     results = face_recognition.compare_faces(some_array, encoded_test)
    #     print(results)

except Exception as ex:
    print("[ INFO ] Error while working with PostgreSQL", ex)
finally:
    if con:
        con.close()
        print("[ INFO ] PostgreSQL connection closed")
