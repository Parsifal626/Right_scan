import requests
from bs4 import BeautifulSoup
import psycopg2

# Установите соединение с базой данных PostgreSql
conn = psycopg2.connect(database="your_database", user="your_username", password="your_password", host="your_host", port="your_port")
cur = conn.cursor()

# Отправьте запрос на получение HTML-страницы
url = "https://nedradv.ru/nedradv/ru/auction"
response = requests.get(url)
html_content = response.content

# Используйте BeautifulSoup для парсинга HTML-страницы
soup = BeautifulSoup(html_content, "html.parser")

# Извлеките данные с помощью CSS-селекторов
dates = soup.select(".date")
plots = soup.select(".plot")
regions = soup.select(".region")
statuses = soup.select(".status")
deadlines = soup.select(".deadline")
fees = soup.select(".fee")
organizers = soup.select(".organizer")

# Пройдитесь по спискам данных и сохраните их в базе данных
for i in range(len(dates)):
    date = dates[i].text.strip()
    plot = plots[i].text.strip()
    region = regions[i].text.strip()
    status = statuses[i].text.strip()
    deadline = deadlines[i].text.strip()
    fee = fees[i].text.strip()
    organizer = organizers[i].text.strip()

    # Выполните запрос на вставку данных в базу данных
    cur.execute("INSERT INTO your_table (date, plot, region, status, deadline, fee, organizer) VALUES (%s, %s, %s, %s, %s, %s, %s)", (date, plot, region, status, deadline, fee, organizer))

# Закройте соединение с базой данных
conn.commit()
cur.close()
conn.close()

print("Данные успешно извлечены и сохранены в базе данных PostgreSql!")