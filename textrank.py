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
# file = [ 'men.txt','women.txt']
for fn in file:
    try:
        print(fn)
        csvname = fn.replace('txt', 'csv')
        with open(foldername + '/purpose/' + fn, 'r') as file:
            # f = open(foldername + '/' + fn, 'w')
            data = file.read().replace('研究經驗及心得', '').replace('報名目的', '').replace('報名⽬的', '').replace(
                '\n', '').replace('若組員有撰寫小論文或是參加科展等活動的經驗，請簡述活動經驗及其心得（無則免）。','')
            # f.write(data)
            # f.close()
            seg_list = jieba.analyse.textrank(data, topK=200, withWeight=True)
            with open(foldername + '/textrank/' + csvname, 'w', newline='') as csvfile:
                csv_out = csv.writer(csvfile)
                csv_out.writerow(['keyword', 'textrank'])
                for row in seg_list:
                    csv_out.writerow(row)
    except:
        print('error')
