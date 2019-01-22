'''
Created on 26-May-2017

@author: John
'''
from datetime import datetime
from DBconnectivity.DBconnect import DBConnect

class PatientDB(object):
    
    def __init__(self):
        pass
    
    def validatePatientid(self,patientid):
        pass
    
    def validateDoctorid(self,doctorid):
        pass
    
    def addPatient(self, patientid, patientname, dob, sex, address, contactno, patienttype):
        dbc = DBConnect()
        insdata=[(patientid, patientname, dob, sex, address, contactno, patienttype)]
        insstmt="insert into patient (patientid, patientname, dob, sex, address, contactno, patienttype) values(:1, :2, TO_DATE(:3,'dd/mm/yyyy'), :4, :5, :6, :7)"
        res=dbc.query(insstmt,insdata)
        
    def displayPatientid(self, patientid):
        dbc = DBConnect()
        sltdata={'patid':patientid}
        sltstmt="select * from patient where patientid=:patid"
        res=dbc.sqlquery(sltstmt,sltdata)
        return self.displayPatient(res)
        
    def displayPatient(self,results):
        patstr="<table style='border:5px solid green'>"
        patstr=patstr+"<tr><th background-color: #4CAF50 color: white>Patient ID</th><th>Patient Name</th><th>Date of Birth</th><th>Sex</th><th>Address</th><th>Contact Number</th><th>Patient Type</th></tr>"
        #print("Patient ID  Patient Name             DOB     Sex   Address       Contact no        Patient Type")
        for row in results:
            patientid = row[0]
            patientname = row[1]
            dob=datetime.date(row[2]).strftime("%d/%m/%Y")
            sex = row[3]
            address = row[4]
            contactno = row[5]
            patienttype = row[6]
            patstr=patstr+"<tr><td style='border:2px solid green'>"+patientid+"</td><td style='border:2px solid green'>"
            patstr=patstr+patientname+"</td><td style='border:2px solid green'>"+dob+"</td><td style='border:2px solid green'>"
            patstr=patstr+sex+"</td><td style='border:2px solid green'>"+address+"</td><td style='border:2px solid green'>"
            patstr=patstr+str(contactno)+"</td><td style='border:2px solid green'>"+patienttype+"</td></tr>"
            #print('{0:11} {1:15} {2:10} {3:5} {4:15} {5:10} {6:5}'.format(patientid, patientname, dob, sex, address, contactno, patienttype ))
        patstr=patstr+"</table>"
        return patstr
    
    def updateAddress(self, patientid, address):
        dbc = DBConnect()
        sltdata={'addr':address, 'patid':patientid}
        sltstmt="update patient set address=:addr where patientid=:patid"
        dbc.updatequery(sltstmt,sltdata)
        
    def updateContactnum(self, patientid, contactno):
        dbc = DBConnect()
        sltdata={'contnum':contactno, 'patid':patientid}
        sltstmt="update patient set contactno=:contnum where patientid=:patid"
        dbc.updatequery(sltstmt,sltdata)