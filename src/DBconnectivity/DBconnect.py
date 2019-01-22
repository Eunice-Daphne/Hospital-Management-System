'''
Created on 26-May-2017

@author: John
'''
#To resolve cx_Oracle error
#Select Project-> RightClick-> PyDev-> Remove PyDev Project Config
#file-> restart

import cx_Oracle
class DBConnect(object):
    '''
    classdocs
    '''
    _db_connection = None
    _db_cur = None   

    def __init__(self):
        '''
        Constructor
        '''
        self._db_connection = cx_Oracle.connect('SYSTEM/lion@127.0.0.1:1521/XE')
        self._db_cur = self._db_connection.cursor()
        
    #used for insert
    def query(self, query, params):
        try:
            self._db_cur.prepare(query)
            res=self._db_cur.executemany(None,params)
            self._db_connection.commit()
            print(res)
            return res
        except OSError as err:
            print('Exception in Insert'+err)
            self._db_connection.rollback()
    
    #used for select query
    def sqlquery(self, query, params):
        try:
            self._db_cur.prepare(query)
            self._db_cur.execute(None,params)
            #self._db_cur.execute(query, params)
            res=self._db_cur.fetchall()
            #self._db_cur.execute(query, params) -- not working
            #self._db_connection.commit()
            return res
        except:
            print('Exception in Select query')
            self._db_connection.rollback()

    #used for update query
    def updatequery(self, query, params):
        try:
            self._db_cur.prepare(query)
            res=self._db_cur.execute(None,params)
            self._db_connection.commit()
            return res
        except:
            print('Exception in Update')
            self._db_connection.rollback()

    def __del__(self):
        self._db_connection.close()