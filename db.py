import psycopg2

QUERY = "select * from recipes where item = 'FOOD_ITEM'"

def create_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="root")
    cursor = conn.cursor()
    return conn,cursor


def execute_query(connection,cursor,query_param):
    print(QUERY.replace("FOOD_ITEM",query_param))
    cursor.execute(QUERY.replace("FOOD_ITEM",query_param))
    rows = cursor.fetchall()
    connection.close()
    return rows
