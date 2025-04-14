import psycopg2


conn = psycopg2.connect(database = "snake",
                        user = "postgres",
                        host = "localhost",
                        password = "hello_122"
)

current_user = ''

def create_table(query):
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()
    

def input_user():
    global current_user
    current_user = input("Input your name: ")


def add_user(username):
    query = "INSERT INTO users(Username) VALUES (%s)"
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, (username,))
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def add_user_score(score, level):
    query = "INSERT INTO users_score(Username, Score, Level) VALUES (%s, %s, %s)"
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, (current_user, score, level))
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def check_user(username):
    query = "SELECT Username FROM users WHERE Username = %s"
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, (username,))
            result = cursor.fetchall()
            return bool(result)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def process_score(score, level):
    user_exist = check_user(current_user)
    if not user_exist:
        add_user(current_user)
    add_user_score(score, level)


query_user_table = "CREATE TABLE users(ID SERIAL PRIMARY KEY, Username VARCHAR(30) UNIQUE)"
query_user_score_table = "CREATE TABLE users_score(ID SERIAL PRIMARY KEY, Username VARCHAR(30), Score INTEGER, Level INTEGER)"


# create_table(query_user_table)
# create_table(query_user_score_table)
    