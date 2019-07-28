# Задание №1

data1='разработка'
data2='сокет'
data3='декоратор'
print ('\n',data1.encode(),'\n',data2.encode(),'\n',data3.encode())

#Задание №2
import sys

bytes_data1=b'class'
bytes_data2=b'function'
bytes_data3=b'method'
print ('\n',type(bytes_data1),'- тип','\n',sys.getsizeof(bytes_data1),'- размер строки в байтах','\n',bytes_data1,'- содержимое')
print ('\n',type(bytes_data2),'- тип','\n',sys.getsizeof(bytes_data2),'- размер строки в байтах','\n',bytes_data2,'- содержимое')
print ('\n',type(bytes_data3),'- тип','\n',sys.getsizeof(bytes_data3),'- размер строки в байтах','\n',bytes_data3,'- содержимое','\n')

#Задание №3

data1=b'attribute'
#data2=b'класс'  #  не содержит элементов ASCII  и не может быть записана в байтовом типе
#data3=b'функция'    #  не содержит элементов ASCII  и не может быть записана в байтовом типе
data4=b'type'


#Задание №4

data1='разработка'
data2='администрирование'
data3='protocol'
data4='standard'

bytes_data1=data1.encode()
print(bytes_data1) # байтовое представление слова "разработка"
data1=bytes_data1.decode()
print(data1) # обратное преобразование байтового представления слова "разработка" в строку

bytes_data2=data2.encode()
print(bytes_data2) # байтовое представление слова "администрирование"
data2=bytes_data2.decode()
print(data2) # обратное преобразование байтового представления слова "администрирование" в строку

bytes_data3=data3.encode()
print(bytes_data3) # байтовое представление слова "protocol"
data3=bytes_data3.decode()
print(data3) # обратное преобразование байтового представления слова "protocol" в строку

bytes_data4=data4.encode()
print(bytes_data4) # байтовое представление слова "standard"
data4=bytes_data4.decode()
print(data4) # обратное преобразование байтового представления слова "standard" в строку
