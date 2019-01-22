'''
Created on 21-Dec-2017

@author: John
'''
import csv
import cx_Oracle

class DBtoCSV(object):
   


    def __init__(self):
        pass
    def dbtocsv(self):
        connection = cx_Oracle.connect('SYSTEM/lion@127.0.0.1:1521/XE')
        cursor = connection.cursor() # assuming you know how to connect to your oracle db
        cursor.execute('select * from diabetes')
        with open('F:\Programs\Python Project\Sample1\src\Output.csv', 'wb') as fout:
            writer = csv.writer(fout)
            #writer.writerow([ i[0] for i in cursor.description ]) # heading row
            writer.writerows(cursor.fetchall())
            
        