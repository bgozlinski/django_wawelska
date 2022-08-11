import sqlite3
from datetime import datetime, timedelta
from yeastar_gateway import *

connect = sqlite3.connect('../db.sqlite3')


c = connect.cursor()

danger_alert = datetime.today()
warning_alert = datetime.today() + timedelta(days=30)

yeastar = Yeastar('192.168.221.161', 5038, 'isander', '075TovoneL')
yeastar.connect_to_yeastar()

for row in c.execute('SELECT car_number, car_service_inspection_date, car_technical_inspection_date FROM cars_car'):
    if row[1] is not None and row[2] is not None:
        car_service_inspection_date = datetime.strptime(row[1], '%Y-%m-%d')
        car_technical_inspection_date = datetime.strptime(row[2], '%Y-%m-%d')
    else:
        continue

    if danger_alert > car_service_inspection_date:
        yeastar.send_sms(
            sim_port=1,
            phone_number='+48572720038',
            message=f'Pojazd numer: {row[0]}. Zakończyła się data przeglądu serwisowego {row[1]}'
        )

    elif warning_alert > car_service_inspection_date:
        yeastar.send_sms(
            sim_port=1,
            phone_number='+48572720038',
            message=f'Pojazd numer: {row[0]}. Zbliza się termin przeglądu serwisowego {row[1]}'
        )

    if danger_alert > car_technical_inspection_date:
        yeastar.send_sms(
            sim_port=1,
            phone_number='+48572720038',
            message=f'Pojazd numer: {row[0]}. Zakończyła się data przeglądu serwisowego {row[2]}'
        )

    elif warning_alert > car_technical_inspection_date:
        yeastar.send_sms(
            sim_port=1,
            phone_number='+48572720038',
            message=f'Pojazd numer: {row[0]}. Zbliza się termin przeglądu serwisowego {row[2]}'
        )
