import jieba
import jieba.analyse
import os
import csv
from pprint import pprint 

foldername = "reg_data"
full_folder = foldername + '/txt/'
file = sorted(os.listdir(full_folder))
jieba.set_dictionary(foldername + '/dict.txt.big.txt')
if not os.path.exists(foldername + '/textrank/'):
        os.makedirs(foldername + '/textrank/')

for fn in file:
    try:
        print(fn)
        csvname = fn.replace('txt', 'csv')
        with open(foldername + '/purpose/' + fn, 'r') as file:
            data = file.read().replace('研究經驗及心得','').replace('報名目的','').replace('\n','')
            seg_list = jieba.analyse.textrank(data, topK=30, withWeight=True)
            with open(foldername + '/textrank/' + csvname, 'w', newline='') as csvfile:
                csv_out = csv.writer(csvfile)
                csv_out.writerow(['keyword', 'textrank'])
                for row in seg_list:
                    csv_out.writerow(row)
    except:
        print('error')
