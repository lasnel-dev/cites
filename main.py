#
# response = requests.get("http://httpbin.org/get")
#
# print(response.text)
# print(f"Datatype - {type(response.text)}")
#
# response =  requests.post("http://httpbin.org/post", data="Test data", headers={"h1":"Test Title"})
# print(response.text)
#
# import requests
#
# response = requests.get("https://coinmarketcap.com/")
# parse_list = []
# response_text = response.text
# response_parse = response_text.split("<span>")
# for elem in response_parse:
#     if elem.startswith("$"):
#         for elem2 in elem.split("</span>"):
#             if elem2.startswith("$") and elem2[1].isdigit():
#                 parse_list.append(elem2)
#
# print(f"BitCoin = {parse_list[0]}")
#
#
# from bs4 import BeautifulSoup
# import requests
# response = requests.get("https://coinmarketcap.com/")
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, features="html.parser")
#     soup_list = soup.find_all("div", {"class":"sc-b3fc6b7-0 dzgUIj"})
#
#     res = soup_list[0].find("span")
#     print(f"BitCoin = {res.text}")

import sqlite3

connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()

# cur.execute("CREATE TABLE Animals (name TEXT, type TEXT);")

# Вставлення даних
# cur.execute("INSERT INTO Animals (name, type) VALUES ('Лев', 'Ссавець');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Kats');")
# cur.execute("INSERT INTO first_table (name) VALUES ('John');")
#
# connection.commit()
# Отримання даних із колонок rowid та name
cur.execute("SELECT rowid, name, type FROM Animals;")
# Отримання даних із колонок rowid та name по індексу 3
# cur.execute("SELECT rowid, name FROM first_table WHERE rowid=3;")
# Редагування значення по вказаному рядку та колонці
# cur.execute("UPDATE first_table SET name='Kate' WHERE rowid=3;")
#Видалення конеретного елемента
# cur.execute("DELETE FROM first_table WHERE rowid=4;")
# Видалення таблиці
# cur.execute("DROP TABLE Animals;")

connection.commit()

res = cur.fetchall()
print(res)

connection.close()