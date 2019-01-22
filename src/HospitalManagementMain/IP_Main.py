'''
Created on 26-May-2017

@author: John
'''
from DButility.InpatientDB import InpatientDB 

sdb=InpatientDB()
#insert inpatient record
'''inp=raw_input('The inpatient is a new patient or a old patient - N/O')
if(inp=='O'):
    admid=raw_input('Enter Admission ID')
    patientid=raw_input('Enter Patient ID')
    roomno=raw_input('Enter Room no')
    doa=raw_input('Enter date of admission- dd/mm/yyyy')
    dod=raw_input('Enter date of discharge- dd/mm/yyyy')
    doctorid=raw_input('Enter the Doctor ID')
    remarks=raw_input('Enter Remarks')
    print("ID of this Patient --",patientid)
    sdb.addoldinPatient(admid, patientid, roomno, doa, dod, doctorid, remarks)
    print('Successfully inserted one patient')
else:
    patientid=raw_input('Enter Patient ID')
    patientname=raw_input('Enter patient Name')
    dob=raw_input('Enter date of birth- dd/mm/yyyy')
    sex=raw_input('Enter the sex')
    address=raw_input('Enter patients address')
    contactno=raw_input('Enter Contact no')
    patienttype=raw_input('Enter Patient Type- IP/OP')
    admid=raw_input('Enter Admission ID')
    roomno=raw_input('Enter Room no')
    dateofadmission=raw_input('Enter date of admission- dd/mm/yyyy')
    dateofdischarge=raw_input('Enter date of discharge- dd/mm/yyyy')
    doctorid=raw_input('Enter the Doctor ID')
    remarks=raw_input('Enter Remarks')
    print("ID of this Patient --",patientid) 
    sdb.addnewinPatient(patientid, patientname, dob, sex, address, contactno, patienttype, admid, roomno, dateofadmission, dateofdischarge, doctorid, remarks)
    print('Successfully inserted one patient')'''
    
#query inpatient with given ID
admid=raw_input('Enter Admin ID')
sdb.displayInPatientPID(admid)
print('Successfully displayed the patient') 
    

    

