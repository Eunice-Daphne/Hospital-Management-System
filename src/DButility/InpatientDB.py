'''
Created on 26-May-2017

@author: John
'''
from datetime import datetime

from DBconnectivity.DBconnect import DBConnect
from DButility.PatientDB import PatientDB

class InpatientDB(PatientDB):
    
    def __init__(self):
        pass
    
    def addoldinPatient(self, admid, patientid, roomno, dateofadmission, dateofdischarge, doctorid, remarks):
        dbc = DBConnect()
        insdata=[(admid, patientid, roomno, dateofadmission, dateofdischarge, doctorid, remarks)]
        #self.validatePatientid(self,patientid)
        #self.validateDoctorid(self,doctorid)
        insstmt="insert into inpatient (admid , patientid, roomno, dateofadmission, dateofdischarge, doctorid, remarks) values(:1, :2, :3, TO_DATE(:4,'dd/mm/yyyy'), TO_DATE(:5,'dd/mm/yyyy'), :6, :7)"
        res=dbc.query(insstmt,insdata)
        
    def addnewinPatient(self, patientid, patientname, dob, sex, address, contactno, patienttype, admid, roomno, dateofadmission, dateofdischarge, doctorid, remarks):
        dbc = DBConnect()
        self.addPatient(patientid, patientname, dob, sex, address, contactno, patienttype)
        insdata=[(admid, patientid, roomno, dateofadmission, dateofdischarge, doctorid, remarks)]
        #self.validateDoctorid(doctorid)
        insstmt="insert into inpatient (admid , patientid, roomno, dateofadmission, dateofdischarge, doctorid, remarks) values(:1, :2, :3, TO_DATE(:4,'dd/mm/yyyy'), TO_DATE(:5,'dd/mm/yyyy'), :6, :7)"
        res=dbc.query(insstmt,insdata)
        
    def displayInPatientid(self, admid):
        dbc = DBConnect()
        sltdata={'adid':admid}
        sltstmt="select * from inpatient where admid=:adid"
        res=dbc.sqlquery(sltstmt,sltdata)
        return self.displayInPatient(res)
        
    def displayInPatientPID(self, patientid):
        dbc = DBConnect()
        sltdata={'patid':patientid}
        sltstmt="select * from inpatient where patientid=:patid"
        res=dbc.sqlquery(sltstmt,sltdata)
        return self.displayInPatient(res)

    def displayInPatient(self,results):
        #print("No of records = "+str(len(results)))
        if (len(results)<1):
             inpatstr="<h3> The patient has not been treated as In-Patient.</h3>"
        else:
            inpatstr="</p><h3>In-Patient Treatment Details</h3></p>"
            inpatstr=inpatstr+"<table>"
            inpatstr=inpatstr+"<tr><th>Admission ID</th><th>Patient ID</th><th>Room Number</th><th>Date of Admission</th><th>Date of Discharge</th><th>Doctor ID</th><th>Remarks</th></tr>"
            #print("Admission ID         Room no        Date of Admission     Date of Discharge   Remarks")
            for row in results:
                admid = row[0]
                patientid = row[1]
                roomno = row[2]
                dateofadmission=datetime.date(row[3]).strftime("%d/%m/%Y")
                dateofdischarge=datetime.date(row[4]).strftime("%d/%m/%Y")
                doctorid = row[5]
                remarks = row[6]
                inpatstr=inpatstr+"<tr><td>"+admid+"</td><td>"+patientid+"</td><td>"+str(roomno)+"</td><td>"+dateofadmission+"</td><td>"+dateofdischarge+"</td><td>"+doctorid+"</td><td>"+remarks+"</td></tr>"
                #print('{0:11} {1:10} {2:10} {3:10} {4:15} {5:10} {6:10}'.format(admid, patientid, roomno, dateofadmission, dateofdischarge, doctorid, remarks ))
            inpatstr=inpatstr+"</table>"
        return inpatstr