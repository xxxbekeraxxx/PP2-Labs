import csv
import psycopg2

conn = psycopg2.connect(database = "postgres", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "hello_122",
                        port = 5432)

cursor = conn.cursor()

# sql = "CREATE DATABASE phonebook"
# cursor.execute(sql)
# conn.commit()
# print("datebase created")

def create_table():
    sql = "CREATE TABLE users (ID SERIAL PRIMARY KEY, First_Name VARCHAR(20), Second_Name VARCHAR(20), Phone VARCHAR(20));"
    cursor.execute(sql)
    conn.commit()
    print("table created")

def insert_values(sql):

    with open("phonebook.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cursor.execute(sql, row)
    conn.commit()
    print("data from csv file uploaded")

    y_n = input("Will you enter another phones? y/n: ")
    if y_n.lower() == 'y':
        number = int(input("Enter number of people that you will insert: "))
        for i in range(number):
            first_name = input("Enter First_name: ")
            second_name = input("Enter Second_Name: ")
            phone = input("Enter phone number (Example: +7(777)....): ")
            cursor.execute(sql, (first_name, second_name, phone))
        conn.commit()

def update_info():
    
    name = input("Enter the first_name whose info you want to change: ")
    field = input("What do you want to update? (first_name/second_name/phone): ").lower()
    enter = input("Enter the new value: ")

    if field in ['first_name', 'f']:
        sql = "UPDATE users SET First_Name = %s WHERE First_Name = %s;"
    elif field in ['second_name', 's']:
        sql = "UPDATE users SET Second_Name = %s WHERE First_Name = %s;"
    elif field in ['phone', 'p']:
        sql = "UPDATE users SET Phone = %s WHERE First_Name = %s;"
    else:
        print("Invalid field")

    cursor.execute(sql, (enter, name))
    conn.commit()

def select_info():
    name = input("Enter name that you want to take info: ")
    sql = 'SELECT * FROM users WHERE First_Name = "%s" OR Second_Name = "%s";'
    cursor.execute(sql, (name, name))
    results = cursor.fetchall()
    for row in results:
        print(row)

def delete_info():
    name = input("Enter name that you want to delete: ")
    sql = 'DELETE FROM users WHERE First_Name = "%s" OR Second_Name = "%s";'
    cursor.execute(sql, (name, name))
    conn.commit()
    
create_table()

sql = "INSERT INTO users(Fisrt_name, Second_Name, Phone) VALUES (%s, %s, %s);"
insert_values(sql)

y_n = input("Will you update info? y/n: ")
if y_n.lower() == 'y':
    update_info()

select_info()

y_n = input("Will you delete info? y/n: ")
if y_n.lower() == 'y':
    delete_info()

cursor.close()
conn.close()
    
