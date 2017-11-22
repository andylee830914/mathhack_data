import json
from pprint import pprint
import subprocess
import zipfile
import os
import os.path
import csv
import mysql.connector
import shutil

import csv
foldername = "reg_data_pdf"


full_folder = foldername + '/full/'
file = os.listdir(full_folder)
for fn in file:
    print(fn)
    try:
        output = subprocess.check_output(['pdf2txt.py',foldername + '/full/' +fn])
        output = output.decode("utf-8").replace(' ', '').replace('\n\n', '\n')
        f = open(foldername + '/txt/' + fn.replace('pdf','txt'), 'w')
        f.write(output)
        f.close()
    except :
        print('skip')

