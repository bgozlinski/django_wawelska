import sqlite3
from datetime import timedelta
from yeastar_gateway import *

#  Connect to local SQLite database
connect = sqlite3.connect('../db.sqlite3')
c = connect.cursor()

#  Get current date and 30 days delta
danger_alert = datetime.today()
warning_alert = datetime.today() + timedelta(days=30)

#  Connect to Yeastar tg-800 GSM gateway
yeastar = Yeastar('192.168.221.161', 5038, 'isander', '075TovoneL')
# yeastar.connect_to_yeastar()

#  Get data from SQLite database
for row in c.execute('SELECT cars_car.car_number, '
                     'cars_car.car_service_inspection_date, '
                     'cars_car.car_technical_inspection_date, '
                     'users_user.user_phone_number '
                     'FROM cars_car, users_user '
                     'WHERE cars_car.user_id = users_user.id'):

    print(row)
    yeastar.connect_to_yeastar()
    if row[1] is not None and row[2] is not None:
        #  Convert string to date
        car_service_inspection_date = datetime.strptime(row[1], '%Y-%m-%d')
        car_technical_inspection_date = datetime.strptime(row[2], '%Y-%m-%d')
        user_phone_number = f'+48{row[3]}'

    else:
        continue
    #  Check date if True send SMS message to phone_number
    if danger_alert > car_service_inspection_date:
        yeastar.send_sms(
            sim_port=1,
            phone_number=f'{user_phone_number}',
            message=f'Pojazd numer: {row[0]}. Zakończyła się data przeglądu serwisowego {row[1]}'
        )

    elif warning_alert > car_service_inspection_date:
        yeastar.send_sms(
            sim_port=1,
            phone_number=f'{user_phone_number}',
            message=f'Pojazd numer: {row[0]}. Zbliża się termin przeglądu serwisowego {row[1]}'
        )

    if danger_alert > car_technical_inspection_date:
        yeastar.send_sms(
            sim_port=1,
            phone_number=f'{user_phone_number}',
            message=f'Pojazd numer: {row[0]}. Zakończyła się data przeglądu technicznego {row[2]}'
        )

    elif warning_alert > car_technical_inspection_date:
        yeastar.send_sms(
            sim_port=1,
            phone_number=f'{user_phone_number}',
            message=f'Pojazd numer: {row[0]}. Zbliża się termin przeglądu technicznego {row[2]}'
        )

    yeastar.close_command()
