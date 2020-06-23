import os
import pandas as pd #импортируем все нужные модули
import fnmatch

begin_path = r'C:\example' #прописываем СВОЙ путь к папке, в которой у нас хранится .xlsx
files_in_path = os.listdir(begin_path) #создаем список из элементов, которые есть в указанном пути
for file in files_in_path: #создаём цикл для поиска файлов нужного нам формата
    if fnmatch.fnmatch(file, '*.xlsx'): #проверяем, что за .xlsx есть
        df = pd.read_excel(file) #читаем файл с помощью пандаса
        yourdir = r'C:\example' #прописываем СВОЙ путь, в который хотим записать .xls
        final_name = r'\result.xls' #имя финального .xls
        final_path = yourdir + final_name #прописываем путь к папке, в которую хотим сохранить данные в .xls, суммируем строки
        writer = pd.ExcelWriter(final_path , engine='xlsxwriter') #записываем данные в файл в указанном пути
        df = df.to_excel(writer, index = False) #форматируем датафрейм в xls, убираем столбец индексов
        writer.save() #сохраняем результат