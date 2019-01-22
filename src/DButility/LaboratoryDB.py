'''
Created on 19-Dec-2017

@author: John
'''
from DBconnectivity.DBconnect import DBConnect

class LaboratoryDB(object):
    
    def __init__(self):
        pass
    
    def addLabdetails(self, patientid, dateoftest, bloodpsystolic,bloodpdiastolic,breathing,pulse,temperature,triglycerides,hdl,ldl,totalcholesterol,wbc,rbc,hct,hgb,petscan):
        dbc = DBConnect()
        insdata=[(patientid, dateoftest, bloodpsystolic,bloodpdiastolic,breathing,pulse,temperature,triglycerides,hdl,ldl,totalcholesterol,wbc,rbc,hct,hgb,petscan)]
        insstmt="insert into laboratory (patientid, dateoftest, bloodpsystolic,bloodpdiastolic,breathing,pulse,temperature,triglycerides,hdl,ldl,totalcholesterol,wbc,rbc,hct,hgb,petscan) values(:1, TO_DATE(:2,'dd/mm/yyyy'), :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16)"
        res=dbc.query(insstmt,insdata)
    
    def displayLabdetailspatid(self, patientid):
        dbc = DBConnect()
        sltdata={'patid':patientid}
        sltstmt="select * from laboratory where patientid=:patid"
        res=dbc.sqlquery(sltstmt,sltdata)
        return self.displayLabdetails(res)
        
    def displaylabdetails(self,results):
        labstr="<table>"
        labstr=labstr+"<tr><th>Patient ID</th><th>Date of Test</th><th>Blood Pressure (systolic)</th><th>Blood Pressure (diastolic)</th><th>Breathing</th><th>Pulse</th><th>Temperature</th><th>Triglycerides</th><th>HDL</th><th>LDL</th><th>Total Cholesterol</th><th>WBC</th><th>RBC</th><th>HCT</th><th>HGB</th><th>PET Scan</th></tr>"
        #print("DoctorID      DoctorName            Specialization")
        for row in results:
            patientid = row[0]
            dateoftest = row[1]
            bloodpsystolic = row[2]
            bloodpdiastolic = row[3]
            breathing = row[4]
            pulse = row[5]
            temperature = row[6]
            triglycerides = row[7]
            hdl = row[8]
            ldl = row[9]
            totalcholesterol = row[10]
            wbc = row[11]
            rbc = row[12]
            hct = row[13]
            hgb = row[14]
            petscan = row[15]
            labstr=labstr+"<tr><td>"+patientid+"</td><td>"+dateoftest+"</td><td>"+bloodpsystolic+"</td><td>"+bloodpdiastolic+"</td><td>"+breathing+"</td><td>"+pulse+"</td><td>"+temperature+"</td><td>"+triglycerides+"</td><td>"+hdl+"</td><td>"+ldl+"</td><td>"+totalcholesterol+"</td><td>"+wbc+"</td><td>"+rbc+"</td><td>"+hct+"</td><td>"+hgb+"</td><td>"+petscan+"</td></tr>"
            #print('{0:11} {1:15} {2:10}'.format(doctorid, doctorname, specialization))
        labstr=labstr+"</table>"
        return labstr
            
   
        
