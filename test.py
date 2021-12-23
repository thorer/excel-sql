import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.types import String, SmallInteger
import shutil, os
from os import listdir
from os.path import isfile, join
import glob

cwd = os.getcwd()

new_ex = r'/Users/thomasnoirclerc/Documents/test_excel/new_excel'
old = r'/Users/thomasnoirclerc/Documents/test_excel/old_source'

fichiers = [f for f in listdir(new_ex) if isfile(join(new_ex, f))]
print(fichiers)

def action():
    for files in fichiers :
        print(files)
        data_xls = pd.read_excel(os.path.join(new_ex, files), dtype=str, index_col=None)
        df_exe = data_xls.to_csv(os.path.join(new_ex, files)+'.csv', encoding='utf-8', index=False)
        shutil.move(os.path.join(new_ex, files),old)


     #faire que le df va dans new_csv

    new_files_2 = os.listdir(new_ex)
    print(new_files_2)
    #je suis vraiment le meilleur dans mon daomaine 


    for files in new_files_2 :
        df_sources = pd.read_csv(os.path.join(new_ex, files))
        engine = create_engine('postgresql+psycopg2://thomasnoirclerc:tiger@localhost:5662/thomasnoirclerc')
        df_sources.to_sql('test8', con = engine, if_exists = 'append',index=False)
    

if __name__ == '__main__':
    print('Application started')

    while True:
        action()

