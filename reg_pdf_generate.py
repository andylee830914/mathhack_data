import json
from pprint import pprint
import subprocess
import os
import sys
import os.path
import csv
import shutil
import csv

foldername = "reg_data"

if len(sys.argv) < 2:
    print('no argument')
    sys.exit()

try:
    if not os.path.exists(foldername + '/full/'):
        os.makedirs(foldername + '/full/')
    with open(sys.argv[1], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['id'], row['your_name'])
            id_folder = foldername + '/ori/' + row['id']
            file = os.listdir(id_folder)
            for fn in file:
                if 'pdf' in fn:
                    old_filename = fn
                    new_filename = row['id'] + ' ' + row['your_name']
                    shutil.copyfile(id_folder + '/' + old_filename,
                                    foldername + '/full/' + new_filename + '.pdf')
except :
    print('file error')
    sys.exit()

