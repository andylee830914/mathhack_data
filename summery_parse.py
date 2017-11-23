import os
import sys
import csv
from pprint import pprint
foldername = "reg_data"
full_folder = foldername + '/profile/'
file = sorted(os.listdir(full_folder))
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
    if line == '美和中學':
        line = '美和高中'
    if line == '台南第一高級中學':
        line = '台南一中'
    if line == '台中市立中港高級中學':
        line = '中港高中'
    return line


if sys.argv[1] == 'gender':
    gender = []
    wlist = ['女中', '女高', '女貌']
    for fn in file:
        print(fn)
        reg_id = fn.split()[0]
        i = 0
        try:
            with open(foldername + '/txt/' + fn, 'r') as file:
                men = 0
                women = 0
                for line in file:
                    if '男' in line:
                        men = men + 1
                    if '女' in line and all(word not in line for word in wlist):
                        women = women + 1
                        # print(repr(line))
                gender.append([reg_id, men, women])
        except:
            print('skip')
    with open(foldername + '/gender.csv', 'w', newline='') as csvfile:
        fieldnames = ['reg', 'men', 'women']
        writer1 = csv.writer(csvfile)
        writer1.writerow(fieldnames)
        for dg in gender:
            print(dg)
            writer1.writerow(dg)

elif sys.argv[1] == 'school':
    sk = ['高', '中', '工']
    nsk = ['慈中', '隊']
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
                    if len(line) >= 4 and len(line) <= 15 and any(word in line for word in sk) and all(word not in line for word in nsk):
                        line = school_same(line)
                        if line in high:
                            high[line].total = high[line].total + 1
                            if reg_id not in high[line].reg:
                                high[line].reg.append(reg_id)
                        else:
                            tschool = School()
                            tschool.total = 1
                            tschool.name = line
                            if reg_id not in tschool.reg:
                                tschool.reg = [reg_id]
                            high[line] = tschool
        except:
            print('skip')

    pprint(high)


    with open(foldername + '/schools.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'reg', 'total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for school in high:
            writer.writerow(high[school].__dict__)
elif sys.argv[1] == 'profile':
    manual = []
    with open(foldername + '/registration.csv', 'w', newline='') as csvfile:
        fieldnames = ['reg', 'name', 'school', 'email', 'phone']
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)

        for fn in file:
            print(fn)
            reg_id = fn.split()[0]
            i = 0
            try:
                with open(foldername + '/profile/' + fn, 'r') as file:
                    lines_data = file.readlines()
                    lines = len(lines_data)
                    lindex = 0
                    if lines - 1 == 16:
                        for line in lines_data[:-1]:
                            lindex = lindex + 1
                            line = line.strip('\n')
                            if lindex % 4 == 1:
                                temp = [reg_id]
                            temp.append(line)
                            if lindex % 4 == 0:
                                print(temp)
                                writer.writerow(temp)

                    elif lines - 2 == 16:
                        for line in lines_data[1:-1]:
                            lindex = lindex + 1
                            line = line.strip('\n')
                            if lindex % 4 == 1:
                                temp = [reg_id]
                            temp.append(line)
                            if lindex % 4 == 0:
                                print(temp)
                                writer.writerow(temp)

                    else:
                        manual.append(reg_id)

            except:
                print('skip')
    print(manual)