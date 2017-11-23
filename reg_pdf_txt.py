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
            file = list(set(file) - set(txt_file))
except :
    pass
        


if not os.path.exists(foldername + '/txt/'):
    os.makedirs(foldername + '/txt/')
for fn in file:
    print(fn)
    try:
        output = subprocess.check_output(['pdf2txt.py',foldername + '/full/' +fn])
        output = output.decode("utf-8").replace(' ', '').replace('姓名', '\n姓名').replace('學校', '\n學校').replace(
            '電話', '\n電話').replace('E-mail', '\nE-mail').replace('報名表', '\n報名表').replace('報名目的', '\n報名目的').replace('研究經驗及心得', '\n研究經驗及心得').replace('\n\n', '\n')
        f = open(foldername + '/txt/' + fn.replace('pdf','txt'), 'w')
        f.write(output)
        f.close()
    except :
        print('skip')

