from os import listdir, path
from datetime import datetime
from app_mod.models import Data


def initialize():
    avgVolume = [average(dir) for dir in listdir('app_mod/data')]
    dateList = [dates(dir) for dir in listdir('app_mod/data')]
    dataList = []
    fixedDataList = []
    temp = sorted(zip(dateList, avgVolume), key=lambda x: x[0])
    for i, (dat, vol) in enumerate(temp):
        if i != 0:
            notValid = round(temp[i-1][1] - vol, 2) < -3
            dataList.append(Data(dat, vol, round(temp[i-1][1] - vol, 2), not notValid))
        else:
            dataList.append(Data(dat, vol, 0, True))

    return dataList

def fix():
    pass

def export():
    pass


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
