import json
from pprint import pprint
import subprocess
import os
import os.path
import sys
import shutil
import csv

foldername = "reg_data"
full_folder = foldername + '/full/'
file = os.listdir(full_folder)

try:
    if sys.argv[1].startswith('--'):
        option = sys.argv[1][2:]
        if option == 'update':
            txt_file = os.listdir(foldername + '/txt/')
            txt_file = [w.replace('.txt', '.pdf') for w in txt_file]
            file1 = list(set(file) - set(txt_file))
            removed = list(set(txt_file) - set(file))
            print(removed)
except :
    pass
        


if not os.path.exists(foldername + '/txt/'):
    os.makedirs(foldername + '/txt/')
for fn in file1:
    print(fn)
    try:
        output = subprocess.check_output(['pdf2txt.py',foldername + '/full/' +fn])
        output = output.decode("utf-8").replace(' ', '').replace('姓名', '\n姓名\n').replace('學校', '\n學校\n').replace(
            '電話', '\n電話\n').replace('E-mail', '\nE-mail\n').replace('性別男', '\n性別男').replace('性別女', '\n性別女').replace('備註', '\n備註\n').replace('報名表', '\n報名表').replace(
            '報名目的', '\n報名目的\n').replace('報名⽬的', '\n報名⽬的\n').replace('研究經驗及⼼得', '\n研究經驗及⼼得\n').replace('在學證明', '\n在學證明\n').replace('年級', '\n年級').replace('\n\n', '\n').replace('\u200b','')
        f = open(foldername + '/txt/' + fn.replace('pdf','txt'), 'w')
        f.write(output)
        f.close()
    except :
        print('skip')

