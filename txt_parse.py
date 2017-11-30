import os
import sys
foldername = "reg_data"
full_folder = foldername + '/txt/'
file = os.listdir(full_folder)
if len(sys.argv) < 2:
    print(
        'usage: python txt_parse.py [ profile | purpose ] [ --update ]')
    sys.exit()


if sys.argv[1] == 'profile' :
    try:
        if sys.argv[2].startswith('--'):
            option = sys.argv[2][2:]
            if option == 'update':
                txt_file = os.listdir(foldername + '/profile/')
                file = list(set(file) - set(txt_file))
    except:
        pass
    if not os.path.exists(foldername + '/profile/'):
        os.makedirs(foldername + '/profile/')
    klist = ['報','隊名', '姓名', '組員', '性別', '電話', '學校',
            '年級', '備註', '無', 'E-mail', '聯絡人', '基本資料', '報名目的', '若有',
            '1.','2.','3.','4.','5.',
            '所以','主題']
    glist = ['1\n', '2\n', '3\n', '10\n',
             '11\n', '12\n', "\n", "\x0c\n", '\xa0\n', '12(高三)\n']
    wlist = ['女中', '女高', '女貌', '女子', '女超人']
    for fn in file:
        print(fn)
        i = 0
        try:
            with open(foldername + '/txt/' + fn, 'r') as file:
                men = 0
                women = 0
                f = open(foldername + '/profile/' + fn, 'w')
                for line in file:
                    if '報名表' in line:
                        i=1
                    if '目的' in line or '⽬的' in line:
                        i=0
                    if '男' in line:
                        men = men + 1
                    if '女' in line and all(word not in line for word in wlist):
                        women = women + 1
                    if i == 1 and line[0]!= '\n' and all(word not in line for word in klist) and all(word != line for word in glist):
                        f.write(line)
                        # print(repr(line))
                f.write('男:'+str(men)+' 女:'+ str(women))
                f.close()
        except:
            print('skip')
elif sys.argv[1] == 'purpose' :
    try:
        if sys.argv[2].startswith('--'):
            option = sys.argv[2][2:]
            if option == 'update':
                txt_file = os.listdir(foldername + '/purpose/')
                file = list(set(file) - set(txt_file))
    except:
        pass
    if not os.path.exists(foldername + '/purpose/'):
        os.makedirs(foldername + '/purpose/')
    klist = ['無則免', '若組員有', '請簡述報名']
    for fn in file:
        print(fn)
        i = 0
        try:
            with open(foldername + '/txt/' + fn, 'r') as file:
                f = open(foldername + '/purpose/' + fn, 'w')

                for line in file:
                    line = line.replace('學校\n', '學校').replace(
                        "\x0c", '').replace('\xa0', '').replace('\u200b\u200b\n','')
                    if '目的' in line or '⽬的' in line: #這兩個目的不一樣啊幹
                        i = 1
                    if '在學證明' in line:
                        i = 0
                    if i == 1 and line != '\n' and all(word not in line for word in klist):
                        print(repr(line))
                        f.write(line)
                f.close()
        except:
            print('skip')
