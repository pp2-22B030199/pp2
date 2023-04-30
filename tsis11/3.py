# CREATE OR REPLACE PROCEDURE public.insert_list(
#   IN p_id int,
#   IN p_name character varying,
#   IN p_phone_number character varying)
# LANGUAGE 'plpgsql'
# AS $BODY$
# begin
#   insert into phonebook(id, name, number) values(p_id, p_name, p_phone_number);
# end;
# $BODY$;

data = [(111, 'Aliya', '87023981276'), (112, 'Dan', '87789127359'), (113, 'Val', '87778126349')]

import psycopg2

# def check(object):
#     list = []
#     cnt = -1
#     for i in object:
#         cnt += 1
#         if not i[1].isdigit():
#             del object[cnt]
#     return object

def insert_list(object):
    connection = None
    try:
        connection = psycopg2.connect(user="postgres",
                                    # пароль, который указали при установке PostgreSQL
                                    password="01tabiei01",
                                    host="Localhost",
                                    port="5432",
                                    database="pp2")

        # Создайте курсор для выполнения операций с базой данных
        cur = connection.cursor()
        cur.executemany('call insert_list(%s, %s, %s)', object)
        connection.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if connection is not None:
            connection.close()
            
insert_list(data)