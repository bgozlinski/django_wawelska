import sqlite3
from datetime import datetime, timedelta

connect = sqlite3.connect('../db.sqlite3')


c = connect.cursor()

danger_alert = datetime.today()
warning_alert = datetime.today() + timedelta(days=30)


for row in c.execute('SELECT car_number, car_service_inspection_date, car_technical_inspection_date FROM cars_car'):
    if row[1] is not None and row[2] is not None:
        car_service_inspection_date = datetime.strptime(row[1], '%Y-%m-%d')
        car_technical_inspection_date = datetime.strptime(row[2], '%Y-%m-%d')
    else:
        continue

    if danger_alert > car_service_inspection_date:
        print(f'Danger: {car_service_inspection_date}')
    elif warning_alert > car_service_inspection_date:
        print(f'Warning: {car_service_inspection_date}')
    elif danger_alert < car_service_inspection_date:
        print(f'OK: {car_service_inspection_date}')

    if danger_alert > car_technical_inspection_date:
        print(f'Danger: {car_technical_inspection_date}')
    elif warning_alert > car_technical_inspection_date:
        print(f'Warning: {car_technical_inspection_date}')
    elif danger_alert < car_technical_inspection_date:
        print(f'OK: {car_technical_inspection_date}')
