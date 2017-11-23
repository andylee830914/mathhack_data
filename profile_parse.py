import os
import sys
import csv
from pprint import pprint
foldername = "reg_data"
full_folder = foldername + '/profile/'
file = sorted(os.listdir(full_folder))
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
        
pprint(manual)
