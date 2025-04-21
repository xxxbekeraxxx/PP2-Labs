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


def insert_values_from_csv(sql):
    with open("phonebook.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cursor.execute(sql, row)
    conn.commit()
    print("data from csv file uploaded")


def insert_values_from_terminal(sql):
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
        sql = "UPDATE users SET first_name = %s WHERE first_name = %s;"
    elif field in ['second_name', 's']:
        sql = "UPDATE users SET second_name = %s WHERE first_name = %s;"
    elif field in ['phone', 'p']:
        sql = "UPDATE users SET phone = %s WHERE first_name = %s;"
    else:
        print("Invalid field")

    cursor.execute(sql, (enter, name))
    conn.commit()

def select_info():
    name = input("Enter name that you want to take info: ")
    sql = 'SELECT * FROM users WHERE first_name = %s OR second_name = %s;'
    cursor.execute(sql, (name, name))
    results = cursor.fetchall()
    for row in results:
        for item in row:
            print(item, end = " ")
        print()

def delete_info():
    name = input("Enter name that you want to delete: ")
    sql = 'DELETE FROM users WHERE first_name = %s OR second_name = %s;'
    cursor.execute(sql, (name, name))
    conn.commit()

def create_fn_pr(command):
    cursor.execute(command)
    conn.commit()


def fn_select_based_pattern():
    command = "SELECT * FROM pattern_search(%s)"
    pattern = input("Enter pattern:")
    cursor.execute(command, (pattern,))
    result = cursor.fetchall()
    for row in result:
        for item in row:
            print(item, end = " ")
        print()

def pr_insert_update():
    first_name = input("Enter First_name: ")
    second_name = input("Enter Second_Name: ")
    phone = input("Enter phone number (Example: +7(777)....): ")
    command = "CALL insert_update(%s, %s, %s)"
    cursor.execute(command, (first_name, second_name, phone))
    conn.commit()
    print("data changed")

def pr_insert_update_list():
    number = int(input("Enter number of users:"))
    first_names, second_names, phones = [], [], []
    command = "CALL insert_update_list(%s, %s::varchar[], %s::varchar[], %s::varchar[])"
    for i in range(number):
        first_names.append(input("Enter First_name: "))
        second_names.append(input("Enter Second_Name: "))
        phones.append(input("Enter phone number (Example: +7(777)....): "))
    cursor.execute(command, (number, first_names, second_names, phones))
    conn.commit()
    print("data inserted")

def fn_limit_offset():
    limit = int(input("Number of rows: "))
    offset = int(input("Number of offset: "))
    command = "SELECT * FROM limit_offset(%s, %s)"
    cursor.execute(command, (limit, offset))
    result = cursor.fetchall()
    for row in result:
        for item in row:
            print(item, end = " ")
        print()

def pr_delete_user():
    info = input("Enter info to delete: ")
    command = "CALL delete_user(%s)"
    cursor.execute(command, (info,))
    conn.commit()
    print("user deleted")
    
# create_table()

sql = "INSERT INTO users(first_name, second_name, phone) VALUES (%s, %s, %s);"
# insert_values_from_csv(sql)
# insert_values_from_terminal(sql)

# y_n = input("Will you update info? y/n: ")
# if y_n.lower() == 'y':
#     update_info()

# select_info()

command_pattern_search = """CREATE OR REPLACE FUNCTION pattern_search(pattern VARCHAR(255))
                            RETURNS TABLE (id INTEGER, first_name VARCHAR(20), second_name VARCHAR(20), phone VARCHAR(20))
                            AS
                            $$
                            BEGIN
                                RETURN QUERY
                                SELECT * FROM users
                                WHERE users.first_name ILIKE '%' || pattern || '%' 
                                OR users.second_name ILIKE '%' || pattern || '%'
                                OR users.phone ILIKE '%' || pattern || '%';

                                IF NOT FOUND THEN
                                    RAISE EXCEPTION 'No rows.';
                                END IF;
                            END;
                            $$ LANGUAGE plpgsql;"""
# create_fn_pr(command_pattern_search)
# fn_select_based_pattern()

command_insert_update = """
            CREATE OR REPLACE PROCEDURE insert_update(f_name VARCHAR(20), s_name VARCHAR(20), number VARCHAR(20))
            AS $$
            BEGIN 
                IF EXISTS(SELECT first_name, second_name, phone FROM users
                          WHERE first_name = f_name OR second_name = s_name OR phone = number) 
                THEN
                    UPDATE users SET first_name = f_name, second_name = s_name, phone = number 
                    WHERE first_name = f_name OR second_name = s_name OR phone = number;
                ELSE
                    INSERT INTO users(first_name, second_name, phone)
                    VALUES (f_name, s_name, number);
                END IF;
            END;
            $$ LANGUAGE plpgsql;"""
# create_fn_pr(command_insert_update)
# pr_insert_update()

command_insert_update_list = """
            CREATE OR REPLACE PROCEDURE insert_update_list(
                IN len INTEGER, 
                IN f_names VARCHAR[], 
                IN s_names VARCHAR[], 
                IN phones VARCHAR[])
            AS $$
            BEGIN
                FOR i IN 1..len LOOP
                    IF phones[i] ~ '^\+7\(\d{3}\)\d{3} \d{4}$' THEN
                        IF EXISTS(SELECT first_name, second_name, phone FROM users
                            WHERE first_name = f_names[i] OR second_name = s_names[i] OR phone = phones[i]) 
                        THEN
                            UPDATE users SET first_name = f_names[i], second_name = s_names[i], phone = phones[i] 
                            WHERE first_name = f_names[i] OR second_name = s_names[i] OR phone = phones[i];
                        ELSE
                            INSERT INTO users(first_name, second_name, phone)
                            VALUES (f_names[i], s_names[i], phones[i]);
                        END IF;
                    ELSE
                        RAISE EXCEPTION 'Error phone number.';
                    END IF;
                END LOOP;
            END;
            $$ LANGUAGE plpgsql;"""
create_fn_pr(command_insert_update_list)
pr_insert_update_list()


command_limit_offset = """CREATE OR REPLACE FUNCTION limit_offset(limit_num INTEGER, offset_num INTEGER)
                          RETURNS TABLE (id INTEGER, first_name VARCHAR(20), second_name VARCHAR(20), phone VARCHAR(20))
                          AS $$
                          BEGIN
                                RETURN QUERY
                                SELECT * FROM users
                                LIMIT limit_num OFFSET offset_num;
                          END;
                          $$ LANGUAGE plpgsql;"""
# create_fn_pr(command_limit_offset)
# fn_limit_offset()

command_delete = """
            CREATE OR REPLACE PROCEDURE delete_user(info VARCHAR(20))
            AS $$
            BEGIN 
                IF EXISTS(SELECT first_name, second_name, phone FROM users
                          WHERE first_name = info OR second_name = info OR phone = info) 
                THEN
                    DELETE FROM users 
                    WHERE first_name = info OR second_name = info OR phone = info;
                ELSE
                    RAISE EXCEPTION 'No rows.';
                END IF;
            END;
            $$ LANGUAGE plpgsql;"""
# create_fn_pr(command_delete)
# pr_delete_user()

# y_n = input("Will you delete info? y/n: ")
# if y_n.lower() == 'y':
#     delete_info()

cursor.close()
conn.close()
    

