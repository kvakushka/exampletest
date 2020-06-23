#импортируем все нужные модули
import os
import pandas as pd
import fnmatch
import re
import sys

#запрашиваем от пользователя пути к файлам, если ввод неправильный, прога выключается
try:
    begin_path = input('Please, enter path to xslx file: ')
    match = re.fullmatch('C:\\D+', begin_path) #так должен выглядеть ввод
    print('ok' if match else sys.exit(1))
except:
    print('Please, enter correctly')
    sys.exit(1)

try:
    yourdir = input('Please, enter path where you want to place xls file: ')
    match = re.fullmatch('C:\\D+', yourdir)
    print('ok' if match else sys.exit(1))
except:
    print('Please, enter correctly')
    sys.exit(1)
#производим все нужные нам действия
files_in_path = os.listdir(begin_path) #создаем список из элементов, которые есть в указанном пути
for file in files_in_path: #создаём цикл для поиска файлов нужного нам формата
    if fnmatch.fnmatch(file, '*.xlsx'): #проверяем, что за .xlsx есть
      df = pd.read_excel(file) #читаем файл с помощью пандаса
      final_name = r'\result.xls' #имя финального .xls
      final_path = yourdir + final_name #прописываем путь к папке, в которую хотим сохранить данные в .xls, суммируем строки
      writer = pd.ExcelWriter(final_path , engine='xlsxwriter') #записываем данные в файл в указанном пути
      df = df.to_excel(writer, index = False) #форматируем датафрейм в xls, убираем столбец индексов
      writer.save() #сохраняем результат