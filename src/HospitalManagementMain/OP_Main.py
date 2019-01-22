'''
Created on 26-May-2017

@author: John
'''
from DButility.OutpatientDB import OutpatientDB 

sdb=OutpatientDB()
#insert inpatient record
inp=raw_input('The outpatient is a new patient or a old patient - N/O')
if(inp=='O'):
    tokenid=raw_input('Enter Token ID')
    patientid=raw_input('Enter Patient ID')
    doctorid=raw_input('Enter the Doctor ID')
    dateofappointment=raw_input('Enter date of appointment- dd/mm/yyyy')
    remarks=raw_input('Enter Remarks')
    print("ID of this Patient --",patientid) 
    sdb.addoldoutPatient(tokenid, patientid, doctorid, dateofappointment, remarks)
    print('Successfully inserted one patient')
else:
    patientid=raw_input('Enter Patient ID')
    patientname=raw_input('Enter patient Name')
    dob=raw_input('Enter date of birth- dd/mm/yyyy')
    sex=raw_input('Enter the sex')
    address=raw_input('Enter patients address')
    contactno=raw_input('Enter Contact no')
    patienttype=raw_input('Enter Patient Type- IP/OP')
    tokenid=raw_input('Enter Token ID')
    doctorid=raw_input('Enter the Doctor ID')
    dateofappointment=raw_input('Enter date of appointment- dd/mm/yyyy')
    remarks=raw_input('Enter Remarks')
    print("ID of this Patient --",patientid) 
    sdb.addnewoutPatient(patientid, patientname, dob, sex, address, contactno, patienttype, tokenid, doctorid, dateofappointment, remarks)
    print('Successfully inserted one patient')
    
#query inpatient with given ID
tokenid=raw_input('Enter Token ID')
sdb.displayOutPatientid(tokenid)
print('Successfully displayed the patient') 