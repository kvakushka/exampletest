import os
import pandas as pd
import fnmatch

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.xlsx'):
        df = pd.read_excel(file)
        df = df.to_excel('result.xls', engine = 'xlsxwriter', index = False)
