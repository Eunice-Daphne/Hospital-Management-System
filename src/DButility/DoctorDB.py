'''
Created on 26-May-2017

@author: John
'''
from DBconnectivity.DBconnect import DBConnect

class DoctorDB(object):
    
    def __init__(self):
        pass
    
    def addDoctor(self, doctorid, doctorname, specialization):
        dbc = DBConnect()
        insdata=[(doctorid, doctorname, specialization)]
        insstmt="insert into doctor (doctorid, doctorname, specialization) values(:1, :2, :3)"
        res=dbc.query(insstmt,insdata)
    
    def displayDoctorid(self, doctorid):
        dbc = DBConnect()
        sltdata={'doctid':doctorid}
        sltstmt="select * from doctor where doctorid=:doctid"
        res=dbc.sqlquery(sltstmt,sltdata)
        return self.displayDoctor(res)
        
    def displayDoctorspec(self, specialization):
        dbc = DBConnect()
        sltdata={'doctorspec':specialization}
        sltstmt="select * from doctor where specialization=:doctorspec"
        res=dbc.sqlquery(sltstmt,sltdata)
        return self.displayDoctor(res)
        
    def displayDoctor(self,results):
        docstr="<table>"
        docstr=docstr+"<tr><th>DoctorID</th><th>DoctorName</th><th>Specialization</th></tr>"
        #print("DoctorID      DoctorName            Specialization")
        for row in results:
            doctorid = row[0]
            doctorname = row[1]
            specialization = row[2]
            docstr=docstr+"<tr><td>"+doctorid+"</td><td>"+doctorname+"</td><td>"+specialization+"</td></tr>"
            #print('{0:11} {1:15} {2:10}'.format(doctorid, doctorname, specialization))
        docstr=docstr+"</table>"
        return docstr
            
    def updateSpecialization(self, doctorid, specialization):
        dbc = DBConnect()
        sltdata={'doctorspec':specialization, 'doctid':doctorid}
        sltstmt="update doctor set specialization=:doctorspec where doctorid=:doctid"
        dbc.updatequery(sltstmt,sltdata)
        
    