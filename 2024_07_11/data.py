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
            return cursor.fetchall()
    conn.close()

def get_snaOfArea(area:str) -> list[tuple]:
    conn = psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])
    with conn:
        with conn.cursor() as cursor:
            sql ='''
            SELECT sna as 站點,total as 總車輛數,rent_bikes as 可借,return_bikes as 可還, mday as 時間,act as 狀態
            FROM youbike
            WHERE (updatetime,sna) IN (
	        SELECT MAX(updatetime),sna
	        FROM youbike
	        WHERE sarea = (%s)
	        GROUP BY sna
            )
            '''

            cursor.execute(sql,(area,))
            return cursor.fetchall()
    conn.close()