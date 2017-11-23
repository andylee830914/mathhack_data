import os
import sys
import csv
from pprint import pprint
foldername = "reg_data"
full_folder = foldername + '/profile/'
file = os.listdir(full_folder)
high = {}

class School:
    def __repr__(self):
        from pprint import pformat
        return pformat(vars(self))
    name = ""
    total = 0
    reg = []


def school_same(line):
    if line == '台北市東山高級中學':
        line = '東山高中'
    if line == '台南市港明高級中學':
        line = '港明高中'
    if line == '台南慈濟高中':
        line = '慈濟高中'
    if line == '屏東高中':
        line = '屏東高中'
    if line == '高雄師範大學附屬高級中學':
        line = '高師大附中'
    if line == '鳳新高中':
        line = '鳳新高中'
    if line == '基隆市安樂高級中學' or line == '基隆市立安樂高級中學':
        line = '安樂高中'
    if line == '新北市格致高級中學' or line == '新北市格致中學':
        line = '格致高中'
    if line == '新北市立中和高中':
        line = '中和高中'
    if line == '精誠高級中學':
        line = '精誠高中'
    if line == '高雄市立新莊高中':
        line = '新莊高中'
    if line == '高雄市立高級中學':
        line = '高雄中學'
    if line == '台南瀛海中學':
        line = '瀛海中學'
    if line == '中山女中':
        line = '中山女高'
    return line

for fn in file:
    print(fn)
    reg_id = fn.split()[0]
    i = 0
    try:
        with open(foldername + '/profile/' + fn, 'r') as file:
            for line in file:
                line = line.strip('\n')
                line = line.replace('國立', '')
                line = line.replace('私立', '')
                if len(line) >= 4 and ('高' in line or '中' in line or '工' in line) and ('慈中' not in line and '隊' not in line):
                    line = school_same(line)
                    if line in high :
                        high[line].total = high[line].total + 1
                        if reg_id not in high[line].reg:
                            high[line].reg.append(reg_id)
                    else :
                        tschool = School()
                        tschool.total = 1
                        tschool.name = line
                        if reg_id not in tschool.reg:
                            tschool.reg = [reg_id]
                        high[line] = tschool
    except:
        print('skip')

pprint(high)


with open(foldername+'/schools.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'reg', 'total']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for school in high:
        writer.writerow(high[school].__dict__)
