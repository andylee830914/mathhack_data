import os
import sys
import csv
from pprint import pprint
foldername = "reg_data"
full_folder = foldername + '/profile/'
file = sorted(os.listdir(full_folder))
high = {}

if len(sys.argv) < 2:
    print(
        'usage: python summary_parse.py [ profile | gender | school ]')
    sys.exit()

class School:
    def __repr__(self):
        from pprint import pformat
        return pformat(vars(self))
    name = ""
    total = 0
    reg = []


def school_same(line):
    if line == '台北市東山高中':
        line = '東山高中'
    if line == '台南市港明高中':
        line = '港明高中'
    if line == '台南慈濟高中':
        line = '慈濟高中'
    if line == '屏東高中':
        line = '屏東高中'
    if line == '高雄師範大學附屬高中':
        line = '高師大附中'
    if line == '鳳新高中':
        line = '鳳新高中'
    if line == '市安樂高中' or line == '基隆市立安樂高中' or line == '基隆市立安樂高中' or line == '基隆市立安樂高中數理實驗班':
        line = '安樂高中'
    if line == '新北市格致高中' or line == '新北市格致中學':
        line = '格致高中'
    if line == '新北市立中和高中':
        line = '中和高中'
    if line == '精誠高中' or line == '彰化縣精誠中學' or line == '精誠中學':
        line = '精誠高中'
    if line == '高雄市立新莊高中':
        line = '新莊高中'
    if line == '高雄市立高中':
        line = '高雄中學'
    if line == '台南瀛海中學':
        line = '瀛海中學'
    if line == '中山女高' or line == '台北市立中山女子高中':
        line = '中山女中'
    if line == '美和中學':
        line = '美和高中'
    if line == '台南第一高中' or line == '臺南第一高中':
        line = '台南一中'
    if line == '台中市立中港高中':
        line = '中港高中'
    if line == '高雄市前鎮高中':
        line = '前鎮高中'
    if line == '復興實驗高中':
        line = '復興實中'
    if line == '南投縣普台高中' or line == '南投縣普台高中':
        line = '普台高中'
    if line == '南科國際實驗高中':
        line = '南科實中'
    if line == '台中市立台中第一高級中等':
        line = '台中一中'
    if line == '台中市立台中第二高級中等':
        line = '台中二中'
    if line == '台中市立文華高級中等':
        line = '文華高中'
    if line == '台中市立龍津高級中等':
        line = '龍津高中'
    if line == '台南第二高中':
        line = '台南二中'
    if line == '臺北市立成功高中':
        line = '成功高中'
    if line == '台南大學附屬高中':
        line = '南大附中'
    if line == '高雄市立鼓山高中':
        line = '鼓山高中'
    if line == '政治大學附屬高中':
        line = '政大附中'
    if line == '暨南國際大學附屬高中':
        line = '暨大附中'
    if line == '衛理女子高中':
        line = '衛理女中'
    if line == '台北市立建國中學':
        line = '建國中學'
    if line == '中興大學附屬高中' or line == '興中興大學附屬高中':
        line = '興大附中'
    if line == '臺中市明道高中':
        line = '明道高中'
    if line == '臺中市立臺中女子高級中等':
        line = '台中女中'
    if line == '台北市立松山高中' or line == '台北市立松山高中':
        line = '松山高中'
    if line == '高雄市立福誠高中':
        line = '福誠高中'
    if line == '武陵⾼中':
        line = '武陵高中'
    if line == '中山大學附屬國光高中':
        line = '國光高中'
    if line == '彰化師範大學附屬高工業職業':
        line = '彰化附工'
    if line == '海青高工商職業':
        line = '海青高工'

    return line


if sys.argv[1] == 'gender':
    gender = []
    mlist = ['男童']
    wlist = ['女中', '女高', '女貌', '女子', '女超人']
    for fn in file:
        print(fn)
        reg_id = fn.split()[0]
        i = 0
        try:
            with open(foldername + '/txt/' + fn, 'r') as file:
                men = 0
                women = 0
                for line in file:
                    if '報名目的' in line:
                        break
                    if '男' in line and all(word not in line for word in mlist):
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
    nsk = ['慈中', '隊', '快樂中山人', '農場', '人類', '交椅']
    for fn in file:
        print(fn)
        reg_id = fn.split()[0]
        i = 0
        try:
            with open(foldername + '/profile/' + fn, 'r') as file:
                for line in file:
                    line = line.strip('\n')
                    line = line.replace('國立', '').replace('臺', '台')
                    line = line.replace('私立', '').replace('數理實驗班','')
                    line = line.replace('高雄市立', '').replace(
                        '台中市立', '').replace('台中市', '').replace('台北市立', '').replace('屏東縣', '').replace(
                        '彰化縣', '').replace('新北市立', '').replace('基隆市立', '').replace('基隆', '')
                    if '高級' in line:
                        line = line.replace('高級', '高').replace(
                            '中學', '中').replace('中等','中')
                    if '第' in line:
                        line = line.replace('高','').replace('第','')
                    line = line.replace('女子高中', '女中').replace('市立', '')
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
