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

with open('mathhack_2017-11-22_下午5-03.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['id'], row['your_name'])
        id_folder = foldername + '/' + row['id']
        file = os.listdir(id_folder)
        for fn in file:
            if 'pdf' in fn:
                old_filename = fn
                new_filename = row['id'] +' '+ row['your_name']
                shutil.copyfile(id_folder + '/' + old_filename,
                          foldername + '/full/' + new_filename+'.pdf')
                # output = subprocess.check_output(['pdf2txt.py',foldername + '/full/' + new_filename+'.pdf'])
                # print(output)

