from os import listdir, path
from datetime import datetime, timedelta
import csv
import math
from tinydb import TinyDB, Query


def initialize():
    avgVolume = [average(dir) for dir in listdir('app_mod/data')]
    dateList = [dates(dir) for dir in listdir('app_mod/data')]

    db = TinyDB('db.json')
    db.truncate()

    temp = sorted(zip(dateList, avgVolume), key=lambda x: x[0])
    for i, (dat, vol) in enumerate(temp):
        volLit = round(vol, 2) * 1000

        notValid = False
        consumption = 0

        if i != 0:
            consumption = round(temp[i-1][1] - vol, 2)
            notValid = consumption < -3
        db.insert({'date': str(dat), 'volume': math.floor(volLit), 'consumption': math.floor(consumption*1000), 'trueConsumption': consumption, 'valid': not notValid, 'fixed': False})


def fix(db, date):
    q = Query()
    res = db.search(q.date == str(date))[0]
    date = datetime.strptime(date, '%Y-%m-%d').date()
    avg = 0

    if not res['valid']:
        dir = 'Arhiv_' + str(date.day).zfill(2) + '_' + str(date.month).zfill(2) + '_' + str(date.year)
        file = open(path.join('app_mod/data', dir, listdir(path.join('app_mod/data', dir))[0]))
        values = [line.split('!')[1].strip() for line in file]
        for i, value in enumerate(values[1:-6]):
            if float(value) - float(values[i-1]) > 3:
                refill = float(values[i+6]) - float(values[i-1])
                if refill > 3:
                    break
            avg += float(value)

        day_before = db.search(q.date == str(date - timedelta(1)))[0]
        consumption = day_before['volume']/1000 - avg / (i+1)

        next_volume = sum([float(value) for value in values[i:]])/len(values[i:])
        next_day = db.search(q.date == str(date + timedelta(1)))[0]
        next_consumption = next_day['volume']/1000 - next_volume
        if i < (len(values) - 8):
            db.update({'trueConsumption': math.floor(round(next_consumption, 2)*1000)}, q.date == str(date + timedelta(1)))
            db.update({'fixed': True}, q.date == str(date + timedelta(1)))

    else:
        consumption = res['consumption']

    if not res['fixed']:
        db.update({'trueConsumption': math.floor(round(consumption, 2)*1000)}, q.date == str(date))
        db.update({'fixed': True}, q.date == str(date))


def export(data):
    fieldnames = ['date', 'volume', 'consumption', 'trueConsumption', 'valid', 'fixed']
    with open('poraba-2021.csv', 'w') as f:
        write = csv.DictWriter(f, fieldnames=fieldnames)
        write.writeheader()
        write.writerows(data)


def dates(dir):
    file = open(path.join('app_mod/data', dir, listdir(path.join('app_mod/data', dir))[0]))

    line = file.read().strip()
    value = line.split(' ')[0]
    return datetime.strptime(value, '%d/%m/%Y').date()


def average(dir):
    file = open(path.join('app_mod/data', dir, listdir(path.join('app_mod/data', dir))[0]))
    counter = 0
    avg = 0

    for line in file:
        value = line.split('!')[1].strip()
        avg += float(value)
        counter += 1

    avg /= counter
    return avg
