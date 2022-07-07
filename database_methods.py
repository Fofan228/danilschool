import sqlite3
import json
import asyncio
import datetime

class database_methods:

    #���������� ������������ � ��
    @staticmethod
    def create_user(chat_id, city):
        conn = sqlite3.connect('BuyBot.db')
        cur = conn.cursor()
        cur.execute("""
        SELECT strftime('%d.%m.%Y %H:%M', DATETIME('now'))
        """)
        time = str(cur.fetchone()[0])
        cur.execute("""
        INSERT INTO Users VALUES (:chat_id, :city, :reg, :last_active, 0)
        """, {'chat_id': chat_id, 'city': city, 'reg': time, 'last_active': time})
        conn.commit()
        cur.close()
        conn.close()


    #����� ������ ������ ������������ (����� ��� ������� �����) - �������!!!
    @staticmethod
    def get_user_data(user_id):
        conn = sqlite3.connect('BuyBot.db')
        cur = conn.cursor()
        cur.execute("""
        SELECT * FROM Users
        WHERE user_id = :outer
        """, {'outer': user_id})
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result


    #TODO ����� ���-�� ������ � id ���� �������� ����� � ��
    @staticmethod
    def add_coins(user_id, coins_number):
        pass


    #Todo ������� 50 ������ � ������������
    #Todo ������ ����� ������������

    #��������� ���������� � �����
    #async def get_avito_list(user_id, request, lower_bound, upper_bound):
     #   #TODO: �������� �����
      #  p = pa.AvitoParse(None)
       # p.avito_start()
        #data = p.parse_20_cards(request, lower_bound, upper_bound)
        #for i in range(0, len(data)):
         #   print(data[i])

    #��������� ���� �� id ���� � �� - �������!!!!
    @staticmethod
    def check_first_start(outer_user_id):
        conn = sqlite3.connect('BuyBot.db')
        cur = conn.cursor()
        cur.execute("""
        SELECT COUNT(*) FROM Users
        WHERE user_id =:outer
        """, {'outer': outer_user_id})
        result = cur.fetchone()
        cur.close()
        return result[0] > 0    #bool

        #TODO: ������ ������ ����� ������������� ������������������ �� ���������� �������
        #������� �������: ���� - ���������� �������
        #����� �������� ������� (����-������)

    @staticmethod
    #def get_list_rookie(start_date, end_date=datetime.date.now()):
     #   conn = sqlite3.connect('BuyBot.db')
      #  cur = conn.cursor()
       # start_date = datetime.date.strptime(start_date)
        #end_date = datetime.date.strptime(end_date)
        #days_count = datetime.timedelta(end_date - start_date)
        #cur.execute("""
          #  SELECT * FROM Users
           # WHERE registration_date =:outer
            #""")
        # result = cur.fetchall()
        # cur.close()
        # return #list

    #TODO: ������ ������ �������� �� ���������� �������
    @staticmethod
    def get_active_users(date):
        return list

    #TODO: ���-�� �������� �� ���������� �������
    @staticmethod
    def get_requests_list():
      return list

    @staticmethod
    def add_request(user, request): #bounds?
        pass

    @staticmethod
    def fill_buffer():
        pass