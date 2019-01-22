'''
Created on 26-May-2017

@author: John
'''
from flask import Flask, render_template, request
import csv
#from werkzeug.utils import secure_filename
from DButility.DoctorDB import DoctorDB
from DButility.StaffDB import StaffDB 
from DButility.InpatientDB import InpatientDB
from DButility.OutpatientDB import OutpatientDB
from DButility.PatientDB import PatientDB
from DButility.LaboratoryDB import LaboratoryDB
from DButility.DiabetesDB import DiabetesDB
from MachineLearningPrograms.BayesClassifier import BayesClassifier
from MachineLearningPrograms.DecisionTree import DecisionTree 
from MachineLearningPrograms.BackPropogation import BackPropogation 
from MachineLearningPrograms.CNNPark import CNNPark
from MachineLearningPrograms.DBtoCSV import DBtoCSV
 
dobj=DoctorDB()
sobj=StaffDB()
inobj=InpatientDB()
outobj=OutpatientDB()
pobj=PatientDB()
lobj=LaboratoryDB()
diaobj=DiabetesDB()
bayesobj=BayesClassifier()
decisiontreeobj=DecisionTree()
backpropogationobj=BackPropogation()
cnnparkobj=CNNPark()
dbtocsvobj=DBtoCSV()
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('Welcome.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/admin")
def admin():
    return render_template('admin.html')
@app.route("/reception")
def reception():
    return render_template('reception.html')
@app.route("/doctor")
def doctor():
    return render_template('doctor.html')
@app.route("/patient")
def patient():
    return render_template('patient.html')
@app.route("/laboratory")
def laboratory():
    return render_template('laboratory.html')

@app.route('/adminlogin',methods=['POST','GET'])
def adminlogin():
    user = request.form['uid']
    pwd = request.form['pwd']
    if user=='admin' and pwd=='admin':
        return render_template('admin_menu.html')
    else:
        return '''
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="ISO-8859-1">
        <title>Administrator LOGIN</title>
        </head>
        <body>
        <center><h2>INVALID LOGIN</h2></center>
        </body>
        </html>'''
@app.route('/receplogin',methods=['POST','GET'])
def receplogin():
    user = request.form['uid']
    pwd = request.form['pwd']
    if user=='admin' and pwd=='admin':
        return render_template('recep_menu.html')
    else:
        return '''
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="ISO-8859-1">
        <title>Reception LOGIN</title>
        </head>
        <body>
        <center><h2>INVALID LOGIN</h2></center>
        </body>
        </html>'''
@app.route('/doclogin',methods=['POST','GET'])
def doclogin():
    user = request.form['uid']
    pwd = request.form['pwd']
    if user=='admin' and pwd=='admin':
        return render_template('pat_menu.html')
    else:
        return '''
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="ISO-8859-1">
        <title>Doctor LOGIN</title>
        </head>
        <body>
        <center><h2>INVALID LOGIN</h2></center>
        </body>
        </html>'''        
@app.route('/patlogin',methods=['POST','GET'])
def patlogin():
    user = request.form['uid']
    pwd = request.form['pwd']
    if user=='admin' and pwd=='admin':
        return render_template('pat_menu.html')
    else:
        return '''
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="ISO-8859-1">
        <title>Patient LOGIN</title>
        </head>
        <body>
        <center><h2>INVALID LOGIN</h2></center>
        </body>
        </html>'''
@app.route('/lablogin',methods=['POST','GET'])
def lablogin():
    user = request.form['uid']
    pwd = request.form['pwd']
    if user=='admin' and pwd=='admin':
        return render_template('lab_menu.html')
    else:
        return '''
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="ISO-8859-1">
        <title>Laboratory LOGIN</title>
        </head>
        <body>
        <center><h2>INVALID LOGIN</h2></center>
        </body>
        </html>'''
        
@app.route("/adddoc")
def adddoc():
    return render_template('adddoctor.html')
@app.route("/addstf")
def addstf():
    return render_template('addstaff.html')
@app.route("/upddocspec")
def upddocspec():
    return render_template('UpdateDoctorSpec.html')
@app.route("/dispdoc")
def dispdoc():
    return render_template('displaydoc.html')
@app.route("/dispstf")
def dispstf():
    return render_template('displaystaff.html')
@app.route("/dispinpat")
def dispinpat():
    return render_template('displayinpatient.html')
@app.route("/dispoutpat")
def dispoutpat():
    return render_template('displayoutpatient.html')

@app.route('/dbadddoc',methods=['POST','GET'])
def dbadddoc():
    if request.method == 'POST':
        doctid = request.form['docid']
        doctname = request.form['docname']
        doctspec = request.form['docspec']
        dobj.addDoctor(doctid, doctname, doctspec)
        return render_template('admin_menu.html')
@app.route('/dbaddstf',methods=['POST','GET'])
def dbaddstf():
    staffid = request.form['stfid']
    staffname = request.form['stfname']
    staffwardno = request.form['stfwardno']
    sobj.addStaff(staffid, staffname, staffwardno)
    return render_template('admin_menu.html')
@app.route('/dbupddocspec',methods=['POST','GET'])
def dbupddocspec():
    if request.method == 'POST':
        doctorid = request.form['docid']
        specialization = request.form['docspec']
        dobj.updateSpecialization(doctorid, specialization)
        return '''
        <!DOCTYPE html>
        <html>
        <head>
        </head>
        <body>
        <center><h2>SUCCESSFULLY UPDATED</h2></center>
        </body>
        </html>'''
@app.route("/dispdocid")
def dispdocid():
    return render_template('displaydoctor.html')
@app.route("/dispdocspec")
def dispdocspec():
    return render_template('displaydoctorSpec.html')

@app.route('/dbdispdoc',methods=['POST','GET'])
def dbdispdoc():
    doctid = request.form['docid']
    docstr=dobj.displayDoctorid(doctid)
    return "<html><head><style> table {border: 5px solid green;}  th, td {border: 1px solid black;} </style></head><body><center><h2>Doctor Details</h2>"+docstr+"</center></body></html>"

@app.route('/dbdispdocspec',methods=['POST','GET'])
def dbdispdocspec():
    specialization = request.form['docspec']
    docstr=dobj.displayDoctorspec(specialization)
    return "<html><head><style> table {border: 5px solid green;}  th, td {border: 1px solid black;} </style></head><body><center><h2>Doctor Details</h2>"+docstr+"</center></body></html>"

@app.route('/dbdispstf',methods=['POST','GET'])
def dbdispstf():
    staffid = request.form['stfid']
    stfstr=sobj.displayStaffid(staffid);
    return "<html><head><style> table {border: 5px solid green;}  th, td {border: 1px solid black;} </style></head><body><center><h2>Staff Details</h2>"+stfstr+"</center></body></html>"

@app.route('/dbdispinpat',methods=['POST','GET'])
def dbdispinpat():
    admid = request.form['adinpid']
    inpatstr=inobj.displayInPatientid(admid)
    return "<html><head><style> table {border: 5px solid green;}  th, td {border: 1px solid black;} </style></head><body><center><h2>InPatient Details</h2>"+inpatstr+"</center></body></html>"

@app.route('/dbdispoutpat',methods=['POST','GET'])
def dbdispoutpat():
    tokenid = request.form['tkotpid']
    outpatstr=outobj.displayOutPatientid(tokenid)
    return "<html><head><style> table {border: 5px solid green;}  th, td {border: 1px solid black;} </style></head><body><center><h2>OutPatient Details</h2>"+outpatstr+"</center></body></html>"

@app.route("/addnewinpat")
def addnewinpat():
    return render_template('addnewinpatient.html')
@app.route("/addoldinpat")
def addoldinpat():
    return render_template('addoldinpatient.html')
@app.route("/addnewoutpat")
def addnewoutpat():
    return render_template('addnewoutpatient.html')
@app.route("/addoldoutpat")
def addoldoutpat():
    return render_template('addoldoutpatient.html')
@app.route("/updpatadd")
def updpatadd():
    return render_template('UpdatePatientAddress.html')
@app.route("/updpatcont")
def updpatcont():
    return render_template('UpdatePatientContactNo.html')

@app.route('/dbaddnewinpat',methods=['POST','GET'])
def dbaddnewinpat():
    if request.method == 'POST':
        patientid = request.form['patid']
        patientname = request.form['patname']
        dob = request.form['dofb']
        sex = request.form['se']
        address = request.form['addr']
        contactno = request.form['contno']
        patienttype = request.form['pattype']
        admid = request.form['adid']
        roomno = request.form['roono']
        dateofadmission = request.form['dofa']
        dateofdischarge = request.form['dofd']
        doctorid = request.form['docid']
        remarks = request.form['rem']
        inobj.addnewinPatient(patientid, patientname, dob, sex, address, contactno, patienttype, admid, roomno, dateofadmission, dateofdischarge, doctorid, remarks)
        return render_template('recep_menu.html')

@app.route('/dbaddoldinpat',methods=['POST','GET'])
def dbaddoldinpat():
    if request.method == 'POST':
        admid = request.form['adid']
        patientid = request.form['patid']
        roomno = request.form['roono']
        dateofadmission = request.form['dofa']
        dateofdischarge = request.form['dofd']
        doctorid = request.form['docid']
        remarks = request.form['rem']
        inobj.addoldinPatient(admid, patientid, roomno, dateofadmission, dateofdischarge, doctorid, remarks)
        return render_template('recep_menu.html')

@app.route('/dbaddnewoutpat',methods=['POST','GET'])
def dbaddnewoutpat():
    if request.method == 'POST':
        patientid = request.form['patid']
        patientname = request.form['patname']
        dob = request.form['dofb']
        sex = request.form['se']
        address = request.form['addr']
        contactno = request.form['contno']
        patienttype = request.form['pattype']
        tokenid = request.form['tkid']
        doctorid = request.form['docid']
        dateofappointment = request.form['dofa']
        remarks = request.form['rem']
        outobj.addnewoutPatient(patientid, patientname, dob, sex, address, contactno, patienttype, tokenid, doctorid, dateofappointment, remarks)
        return render_template('recep_menu.html')

@app.route('/dbaddoldoutpat',methods=['POST','GET'])
def dbaddoldoutpat():
    if request.method == 'POST':
        tokenid = request.form['tkid']
        patientid = request.form['patid']
        doctorid = request.form['docid']
        dateofappointment = request.form['dofa']
        remarks = request.form['rem']
        outobj.addoldoutPatient(tokenid, patientid, doctorid, dateofappointment, remarks)
        return render_template('recep_menu.html')

@app.route('/dbupdpatadd',methods=['POST','GET'])
def dbupdpatadd():
    if request.method == 'POST': 
        patientid = request.form['patid']
        address = request.form['pataddr'] 
        pobj.updateAddress(patientid, address)  
        return '''
        <!DOCTYPE html>
        <html>
        <head>
        </head>
        <body>
        <center><h2>SUCCESSFULLY UPDATED</h2></center>
        </body>
        </html>'''

@app.route('/dbupdpatcont',methods=['POST','GET'])
def dbupdpatcont():
    if request.method == 'POST': 
        patientid = request.form['patid']
        contactno = request.form['patcont'] 
        pobj.updateContactnum(patientid, contactno)
        return '''
        <!DOCTYPE html>
        <html>
        <head>
        </head>
        <body>
        <center><h2>SUCCESSFULLY UPDATED</h2></center>
        </body>
        </html>'''       

@app.route("/disppat")
def disppat():
    return render_template('displaypatient.html')

@app.route("/patupload")
def patupload():
    return render_template('pat_upload.html')

@app.route('/dbdisppat',methods=['POST','GET'])
def dbdisppat():
    if request.method == 'POST':
        patientid = request.form['patid']
        patstr=pobj.displayPatientid(patientid)
        inpatstr=inobj.displayInPatientPID(patientid)
        outpatstr=outobj.displayOutPatientPID(patientid)
        return "<html><style> table {border: 5px solid green;}  th, td {border: 1px solid black;} </style><body><center><h2>Patient Details</h2>"+patstr+inpatstr+outpatstr+"</center></body></html>"
    
@app.route('/uploader',methods=['POST','GET'])
def uploader():
    if request.method == 'POST':
        #f = request.files['file']
        #f.save(secure_filename(f.filename))
        return 'file uploaded successfully'
    
@app.route("/displab")
def displab():
    return render_template('displaylaboratory.html')


@app.route("/dbaddlabdetails", methods=['POST'])
def dbaddlabdetails():
    if request.method == 'POST':
        patid = request.form['patid']
        dot = request.form['dot']
        BSY = request.form['BSY']
        BDI = request.form['BDI']
        breath = request.form['breath']
        pulse = request.form['pulse']
        temp = request.form['temp']
        trigly = request.form['trigly']
        HDL = request.form['HDL']
        LDL = request.form['LDL']
        totalcho = request.form['totalcho']
        WBC = request.form['WBC']
        RBC = request.form['RBC']
        HTC = request.form['HTC']
        HGB = request.form['HGB']
        pets = request.form['pets']
        lobj.addLabdetails(patid, dot, BSY, BDI, breath, pulse, temp, trigly, HDL, LDL, totalcho, WBC, RBC, HTC, HGB, pets)
        return render_template('lab_menu.html')

@app.route("/dispdiabetesbay")
def dispdiabetes():
    return render_template('displaydiabetesbay.html')
@app.route("/dbadddiabetesdetails", methods=['POST'])
def dbadddiabetesdetails():
    if request.method == 'POST':
        ntp = request.form['ntp']
        plasmaglo = request.form['plasmaglo']
        diastolbp = request.form['diastolbp']
        tricep = request.form['tricep']
        serumins = request.form['serumins']
        bmi = request.form['bmi']
        diabetespedi = request.form['diabetespedi']
        age = request.form['age']
        classvar = request.form['classvar']
        diaobj.addDiabetesdetails(ntp, plasmaglo, diastolbp, tricep, serumins, bmi, diabetespedi, age, classvar)
        dbtocsvobj.dbtocsv()
        return render_template('lab_menu.html')   
@app.route("/bayesianclassifier",methods=['GET','POST'])
def bayesianclassifier():
    if request.method == 'GET':
        var=bayesobj.main()
        #return render_template('aaa.html')
        return "<html><head><style> table {border: 5px solid green;}  th, td {border: 1px solid black;} </style></head><body><center><h2>Accuracy</h2>"+str(var)+"</center></body></html>"#'Bayesian Classifier successfully run'

@app.route("/dispdiabetesDT")
def dispdiabetesDT():
    return render_template('displaydiabetesDT.html')  
@app.route("/decisiontree",methods=['GET','POST'])
def decisiontree():
    if request.method == 'GET':
        var=decisiontreeobj.main()
        return "<html><head><style> table {border: 5px solid green;}  th, td {border: 1px solid black;} </style></head><body><center><h2>Accuracy</h2>"+str(var)+"</center></body></html>"#'Bayesian Classifier successfully run'

@app.route("/dispdiabetesBP")
def dispdiabetesBP():
    return render_template('displaydiabetesBP.html')
@app.route("/backpropogation",methods=['GET','POST'])
def backpropogation():
    if request.method == 'GET':
        var=backpropogationobj.main()
        return "<html><head><style> table {border: 5px solid green;}  th, td {border: 1px solid black;} </style></head><body><center><h2>Accuracy</h2>"+str(var)+"</center></body></html>"#'Bayesian Classifier successfully run'

@app.route("/dispparkinsonCNN")
def dispparkinsonCNN():
    return render_template('dispparkinsonCNN.html')
@app.route("/parkinsonCNN",methods=['GET','POST'])
def parkCNN():
    if request.method == 'GET':
        var=cnnparkobj.main()
        return "<html><head><style> table {border: 5px solid green;}  th, td {border: 1px solid black;} </style></head><body><center><h2>Accuracy</h2>"+str(var)+"</center></body></html>"#'Bayesian Classifier successfully run'            
    
if __name__ == "__main__":
    app.run(debug = True)