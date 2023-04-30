# Create Procedure edit
# (
# r_name varchar,
# r_phone_number varchar
# )
# language 'plpgsql'
# as $$
# begin
# if (not exists (Select name from phonebook where name = r_name)) then
#          insert into phonebook(name, phone_number)
#      values(r_name, r_phone_number);
# Else
#           update phonebook set phone_number = r_phone_number where phonebook.name = r_name;
# end if;
# end;
# $$

# call edit("Adi","87760228214")
import psycopg2
from psycopg2 import Error

connection = None
def edit(r_id, r_name, r_number):
    try:
    # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                    # пароль, который указали при установке PostgreSQL
                                    password="01tabiei01",
                                    host="Localhost",
                                    port="5432",
                                    database="pp2")

        # Создайте курсор для выполнения операций с базой данных
        

        cursor = connection.cursor()

        cursor.callproc('call edit(%s, %s, %s)', (r_id, r_name, r_number))

        
        connection.commit()
        print("Таблица успешно создана в PostgreSQL")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

edit(11, "Adi", "87760228214")