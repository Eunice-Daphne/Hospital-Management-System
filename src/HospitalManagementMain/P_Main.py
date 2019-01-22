'''
Created on 26-May-2017

@author: John
'''
#from datetime import date
from DButility.PatientDB import PatientDB 

sdb=PatientDB()
#insert patient record
'''patientid=raw_input('Enter Patient ID')
patientname=raw_input('Enter patient Name')
dob=raw_input('Enter date of birth- dd/mm/yyyy')
sex=raw_input('Enter the sex')
address=raw_input('Enter patients address')
contactno=raw_input('Enter Contact no')
patienttype=raw_input('Enter Patient Type- IP/OP')
print("ID of this Patient --",patientid) 
sdb.addPatient(patientid, patientname, dob, sex, address, contactno, patienttype)
print('Successfully inserted one patient')'''

#query patient with given ID
patientid=raw_input('Enter Patient ID')
print(sdb.displayPatientid(patientid))
print('Successfully displayed the patient')

#update address for a patient
patientid=raw_input('Enter Patient ID')
addrs=raw_input('Enter new address')
sdb.updateAddress(patientid, addrs)
print('Patient address successfully updated')

#update contactno for a patient
patientid=raw_input('Enter patient ID')
contactno=raw_input('Enter new contactno')
sdb.updateContactnum(patientid, contactno)
print('Patient contactno successfully updated')

