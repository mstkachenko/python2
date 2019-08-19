#Скрипт работает при условии нахождения файлов info_1(2,3).txt в папке '\data\hw2'. CSV файл формируется в этой же папке

import csv
import os
import re
import numpy as np

os_prod_list=[]
os_name_list=[] 
os_code_list=[] 
os_type_list=[]

catalog = os.path.abspath('data/hw2')
files = os.listdir('data/hw2')
txt_files = filter(lambda x: x.endswith('.txt'),files)

for i in list(txt_files):
    txt_file_path=os.path.join(catalog,i)
    with open(txt_file_path) as file:
        for row in file:
 
            if re.search('Изготовитель системы',row) != None:
                os_prod_list.append(row[34:-1])
            
            if re.search('Название ОС',row) != None:
                os_name_list.append(row[34:-1])
                
            if re.search('Код продукта',row) != None:
                os_code_list.append(row[34:-1])
            
            if re.search('Тип системы',row) != None:
                os_type_list.append(row[34:-1])
            
 

data = np.array([os_prod_list,
os_name_list,
os_code_list, 
os_type_list,
    ])
data=data.transpose()

headers=[['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]


with open ('data/hw2/data.csv', 'w',encoding='utf-8') as file:
    writer = csv.writer(file)
    for row in new_data:
        writer.writerow(row)
    for row in data:
        writer.writerow(row)