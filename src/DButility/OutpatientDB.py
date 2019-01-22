'''
Created on 26-May-2017

@author: John
'''
from datetime import datetime

from DBconnectivity.DBconnect import DBConnect
from DButility.PatientDB import PatientDB

class OutpatientDB(PatientDB):
    
    def __init__(self):
        pass
    
    def addoldoutPatient(self, tokenid, patientid, doctorid, dateofappointment, remarks):
        dbc = DBConnect()
        insdata=[(tokenid, patientid, doctorid, dateofappointment, remarks)]
        #self.validatePatientid(patientid)
        #self.validateDoctorid(doctorid)
        insstmt="insert into outpatient (tokenid, patientid, doctorid, dateofappointment, remarks) values(:1, :2, :3, TO_DATE(:4,'dd/mm/yyyy'), :5)"
        res=dbc.query(insstmt,insdata)
        
    def addnewoutPatient(self, patientid, patientname, dob, sex, address, contactno, patienttype, tokenid, doctorid, dateofappointment, remarks):
        self.addPatient(patientid, patientname, dob, sex, address, contactno, patienttype)
        dbc = DBConnect()
        insdata=[(tokenid, patientid, doctorid, dateofappointment, remarks)]
        #self.validateDoctorid(doctorid)
        insstmt="insert into outpatient (tokenid, patientid, doctorid, dateofappointment, remarks) values(:1, :2, :3, TO_DATE(:4,'dd/mm/yyyy'), :5)"
        res=dbc.query(insstmt,insdata)
        
    def displayOutPatientid(self, tokenid):
        dbc = DBConnect()
        sltdata={'tokid':tokenid}
        sltstmt="select * from outpatient where tokenid=:tokid"
        res=dbc.sqlquery(sltstmt,sltdata)
        return self.displayOutPatient(res)
        
    def displayOutPatientPID(self, patientid):
        dbc = DBConnect()
        sltdata={'patid':patientid}
        sltstmt="select * from outpatient where patientid=:patid"
        res=dbc.sqlquery(sltstmt,sltdata)
        return self.displayOutPatient(res)

    def displayOutPatient(self,results):
        #print("No of records = "+str(len(results)))
        if (len(results)<1):
             outpatstr="<h3> The patient has not been treated as Out-Patient.</h3>"
        else:
            outpatstr="</p><h3>Out-Patient Treatment Details</h3></p>"
            outpatstr=outpatstr+"<table>"
            outpatstr=outpatstr+"<tr><th>Token ID</th><th>Patient ID</th><th>Doctor ID</th><th>Date of Appointment</th><th>Remarks</th></tr>"
            #print("Token ID       Patient ID     Doctor ID      Date of Appointment         Remarks")
            for row in results:
                tokenid = row[0]
                patientid = row[1]
                doctorid = row[2]
                dateofappointment=datetime.date(row[3]).strftime("%d/%m/%Y")
                remarks = row[4]
                outpatstr=outpatstr+"<tr><td>"+tokenid+"</td><td>"+patientid+"</td><td>"+doctorid+"</td><td>"+dateofappointment+"</td><td>"+remarks+"</td></tr>"
                #print('{0:11} {1:10} {2:10} {3:10} {4:10}'.format(tokenid, patientid, doctorid, dateofappointment, remarks ))
            outpatstr=outpatstr+"</table>"
        return outpatstr