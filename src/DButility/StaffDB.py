'''
Created on 26-May-2017

@author: John
'''
from DBconnectivity.DBconnect import DBConnect

class StaffDB(object):
    
    def __init__(self):
        pass
    
    def addStaff(self, staffid, staffname, wardno):
        dbc = DBConnect()
        insdata=[(staffid, staffname, wardno)]
        insstmt="insert into staff (staffid, staffname, wardno) values(:1, :2, :3)"
        res=dbc.query(insstmt,insdata)
    
    def displayStaffid(self, staffid):
        dbc = DBConnect()
        sltdata={'stfid':staffid}
        sltstmt="select * from staff where staffid=:stfid"
        res=dbc.sqlquery(sltstmt,sltdata)
        return self.displayStaff(res)
        
    def displayStaffWardno(self, wardno):
        dbc = DBConnect()
        sltdata={'wrdnum':wardno}
        sltstmt="select * from staff where wardno=:wrdnum"
        res=dbc.sqlquery(sltstmt,sltdata)
        return self.displayStaff(res)
        
    def displayStaff(self,results):
        stfstr="<table>"
        stfstr=stfstr+"<tr><th>Staff ID</th><th>Staff Name</th><th>Ward Number</th></tr>"
        #print("StaffID      StaffName            Ward Number")
        for row in results:
            staffid = row[0]
            staffname = row[1]
            wardno = row[2]
            stfstr=stfstr+"<tr><td>"+staffid+"</td><td>"+staffname+"</td><td>"+wardno+"</td></tr>"
            #print('{0:11} {1:15} {2:10}'.format(staffid, staffname, wardno))
        stfstr=stfstr+"</table>"
        return stfstr
            
    def updateWardnum(self, staffid, wardno):
        dbc = DBConnect()
        sltdata={'wardnum':wardno, 'stfid':staffid}
        sltstmt="update staff set wardno=:wardnum where staffid=:stfid"
        dbc.updatequery(sltstmt,sltdata)