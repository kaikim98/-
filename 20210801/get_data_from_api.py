from urllib import request
import json
from prettytable import PrettyTable
import sqlite3
dataTable = PrettyTable()
URL = 'http://api.openweathermap.org/data/2.5/weather?q={city name}&lang={lang}&appid={API key}'

CITIES = ['seoul', 'busan', 'chuncheon']
LANG = 'kr'
API_KEY = '91a04cfe728b2b65ee677c7f7360f3eb'

connection_sqlite3 = sqlite3.connect('weather.db')
cursor_sqlite3 = connection_sqlite3.cursor()

city_weatehr_table_create = "CREATE TABLE IF NOT EXISTS city_weather (id integer, main text, description text, icon text)"
cursor_sqlite3.execute(city_weatehr_table_create)

for CITY in CITIES:
    with request.urlopen(URL.replace('{city name}', CITY).replace('{lang}', LANG).replace('{API key}', API_KEY)) as response:
        result_json = response.read()

parsed_json = json.loads(result_json)

dataTable.filed_names = parsed_json['weather'][0].keys()

for i in parsed_json["weather"]:
    list_values = list(i.values())
    # print(list_values[0],list_values[1],list_values[2],list_values[3])
    dataTable.add_row(i.values())
    cursor_sqlite3.execute(
        "INSERT INTO city_weather VALUES ('" + 
            str(list_values[0]) + "', '" + 
            list_values[1] + "', '" + 
            list_values[2] + "', '" + 
            list_values[3] + "')"
    )
connection_sqlite3.commit()
print(dataTable)