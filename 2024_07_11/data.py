from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

def get_areas():
    conn = psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])
    with conn: #with conn會自動commit(),手動close
         with conn.cursor() as cursor: #自動close()
            sql = '''
                select distinct sarea
                From youbike;
            '''
            cursor.execute(sql)
            print(cursor.fetchall())
    conn.close()
