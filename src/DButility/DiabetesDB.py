'''
Created on 21-Dec-2017

@author: John
'''
from DBconnectivity.DBconnect import DBConnect
class DiabetesDB(object):
    
    def __init__(self):
        pass
    
    def addDiabetesdetails(self, no_times_pregnant, plasma_glucose, diastolic_bp,triceps,serum_insulin ,bmi ,diabetes_pedigree ,age ,class_variable):
        dbc = DBConnect()
        insdata=[(no_times_pregnant, plasma_glucose, diastolic_bp,triceps,serum_insulin,bmi,diabetes_pedigree,age,class_variable)]
        insstmt="insert into diabetes (no_times_pregnant, plasma_glucose, diastolic_bp,triceps,serum_insulin,bmi,diabetes_pedigree,age,class_variable) values(:1, :2, :3, :4, :5, :6, :7, :8, :9)"
        res=dbc.query(insstmt,insdata)