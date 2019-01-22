'''
Created on 26-May-2017

@author: John
'''
#from datetime import date

from DButility.DoctorDB import DoctorDB 
sdb=DoctorDB()


#insert doctor record
did=raw_input('Enter Doctor ID')
doctorname=raw_input('Enter Doctor Name')
specialization=raw_input('Enter Doctor Specialization')
print("ID of this Doctor --",did) 
sdb.addDoctor(did, doctorname, specialization)
print('Successfully inserted one Doctor')

#query doctor with given ID
did=raw_input('Enter Doctor ID')
print(sdb.displayDoctorid(did))
print('Successfully displayed the doctor')
#query doctors with given specialization 
specialization=raw_input('Enter Specialization - NS/CL/DB')
sdb.displayDoctorspec(specialization)
print('Successfully displayed the doctor')


#update specialization for a doctor
did=raw_input('Enter Doctor ID')
specialization=raw_input('Enter new specialization')
sdb.updateSpecialization(did, specialization)
print('Doctor specialization successfully updated')



