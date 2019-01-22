'''
Created on 26-May-2017

@author: John
'''
from DButility.StaffDB import StaffDB 

sdb=StaffDB()
#insert staff record
staffid=raw_input('Enter Staff ID')
staffname=raw_input('Enter Staff Name')
wardno=raw_input('Enter Staff Ward Number')
print("ID of this Staff --",staffid) 
sdb.addStaff(staffid, staffname, wardno)
print('Successfully inserted one Staff')

#query staff with given ID
staffid=raw_input('Enter Staff ID')
sdb.displayStaffid(staffid)
print('Successfully displayed the staff')
#query staff with given specialization 
wardno=raw_input('Enter Ward Number')
sdb.displayStaffWardno(wardno)
print('Successfully displayed the staff')


#update ward for a staff
staffid=raw_input('Enter Staff ID')
wardno=raw_input('Enter new Ward Number')
sdb.updateWardnum(staffid, wardno)
print('Staff Ward Number successfully updated')