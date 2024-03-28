import requests
from requests.structures import CaseInsensitiveDict
import os
import time
import json
import gspread
import datetime


token = "sfrkckngnfbxuhy2zj59"
company_id = "123456"
url = "https://api.alteg.io/api/v1/reports/z_report/{company_id}"
katusenapi = set()
narva = set()
narva2 = set()
tartuyaama = set()
tartutyaha = set()
parnohomiku = set()
narvakerase =set()
mehaanika = set()


def get_data_from_api(token, company_id, url):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Autoritation"] = "Bearer {token}"
    

    r = requests.get(url, headers=headers, date_from="2024-03-01", date_to =datetime.today())

    print(r.status_code)


def dump_to_json(data_from_api):
    data = json.dump(data_from_api)
    return(data)
    

#финансовые показатели
    #https://api.alteg.io/api/v1/finance_transactions/{company_id}/{transaction_id}


# # gc = gspread.service_account()
# wks = gc.open("Where is the money Lebowski?").sheet1
# wks.update('A1', [[1, 2], [3, 4]])
# wks.update('B42', "")
# wks.format('A1:B1', {'textFormat': {'bold': True}})



if __name__ == "__main__":
    print("exporting data to google sheets...")

# Выполнение плана
# План
# Выручка по услугам
# Выручка по аб-там общая
# Выручка доплаты
# Выручка серт-ы
# Выручка косметика
# Общая выручка
# Всего записей
# % отмен
# Завершенных
# % улучшений
# всего лидов
# записи новых клиентов
# % конверсия лид/запись
# новых клиентов
# % конверсия лид/клиент
# Всего клиентов
# Новых клиентов
# Повторных клиентов
# CRR
# Потерянных клиентов
# % потерянных
# Клиенты с абонементами
# Клиентам можно продать абон-т
# Продали абонементов шт
# Продали косметики шт
# Средний чек услуги
# Средний чек абон-т
# Средний чек косметика
# рабочих дней
# максимальная загрузка часов
# незакрытых дней
# отработано дней
# рабочих часов
# отработано часов
# Стоимость часа работы
# часов простоя
# заполненность
# % загрузки