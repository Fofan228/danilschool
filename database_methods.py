import sqlite3
import json
import parser_avito as pa

#TODO: �������������

#���������� ������������ � ��
def create_user(chat_id, city):
    conn = sqlite3.connect('BuyBot.db')
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO Users VALUES (chat_id, city, datetime(now))
    """)
    cur.commit()

#��������� ���������� � �����
def get_avito_list(user_id, request, lower_bound, upper_bound):
    #TODO: �������� �����
    p = pa.AvitoParse(city)
    p.avito_start()
    data = p.parse_20_cards(request, lower_bound, upper_bound)
    for i in range(0, len(data)):
        print(data[i])
