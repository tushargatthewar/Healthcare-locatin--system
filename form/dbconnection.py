
from flask import Flask, render_template, request,session,jsonify
import mysql.connector
# from flask import Flask, render_template, request,jsonify
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
import pandas as pd
import os
import joblib
from flask_cors import CORS
import sqlite3
# MySQL configurations
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Yadnyesh@6119'
app.config['MYSQL_DB'] = 'webdata'

mydb = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)


app.secret_key =b'bb70e46b1271eda075742e011314a5b2e99a5e093f75cb85'


CORS(app)  # Enable CORS for all routes
model = joblib.load('disease_classifier.pkl')
model1 = joblib.load('disease_classifier_random.pkl')
model2 = joblib.load('disease_classifier_bayes.pkl')

@app.route('/')
def home():
    return render_template('pateint_home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/schemes')
def schemes():
    return render_template('scheme.html')

@app.route('/symptomes', methods=['POST'])
def symptomes():
    select1 = request.form['select1']
    select2 = request.form['select2']
    select3 = request.form['select3']
    select4 = request.form['select4']
    print(select1,select2,select3,select4)
    l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
    'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
    'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
    'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
    'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
    'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
    'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
    'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
    'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
    'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
    'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
    'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
    'yellow_crust_ooze']

    disease=['Fungal_infection', 'Allergy', 'GERD', 'Chronic_cholestasis',
       'Drug_Reaction', 'Peptic_ulcer_diseae', 'AIDS', 'Diabetes ',
       'Gastroenteritis', 'Bronchial_Asthma', 'Hypertension ', 'Migraine',
       'Cervical_spondylosis', 'Paralysis_brain_hemorrhage', 'Jaundice',
       'Malaria', 'Chicken_pox', 'Dengue', 'Typhoid', 'hepatitis_A',
       'Hepatitis_B', 'Hepatitis_C', 'Hepatitis_D', 'Hepatitis_E',
       'Alcoholic_hepatitis', 'Tuberculosis', 'Common_Cold', 'Pneumonia',
       'Dimorphic_hemmorhoids', 'Heart_attack', 'Varicose_veins',
       'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
       'Osteoarthristis', 'Arthritis',
       'Varicose_veins', 'Acne',
       'Urinary_tract_infection', 'Psoriasis', 'Impetigo','Paroymsal_Positional_Vertigo']
    
    l2=[]
    for i in range(0,len(l1)):
        l2.append(0)
    print(l2)
    
    psymptoms=[select1,select2,select3,select4]
    for k in range(0,len(l1)):
     for z in psymptoms:
        if(z==l1[k]):
            l2[k]=1

    inputtest = [l2]
    print(inputtest)
    predicted_disease=[]
    predict1=model.predict(inputtest)
    predicted1=predict1[0]
    h='no'
    for a in range(0,len(disease)):
        if(predicted1 == a):
            h='yes'
            break

    predicted_disease.append(disease[a])
    if (h=='yes'):
        print("Predicted disease:", disease[a])
    else:
        print("not found")

    predict2=model1.predict(inputtest)
    predicted2=predict2[0]
    h='no'
    for a in range(0,len(disease)):
        if(predicted2 == a):
            h='yes'
            break
    predicted_disease.append(disease[a])
    if (h=='yes'):
        print("Predicted disease:", disease[a])
    else:
        print("not found")  


    predict3=model2.predict(inputtest)
    predicted3=predict3[0]
    h='no'
    for a in range(0,len(disease)):
        if(predicted3 == a):
            h='yes'
            break
    predicted_disease.append(disease[a])
    if (h=='yes'):
        print("Predicted disease:", disease[a])
    else:
        print("not found")
    predicted_disease=list(set(predicted_disease)) 
    print(predicted_disease) 
    predicted_disease[0]

    
    disease_info = {
    "Drug_Reaction": [["stop irritation", "consult nearest hospital", "stop taking drug", "follow up"],
                      "Common -More than 1 million cases per year (India)"],
    "Malaria": [["Consult nearest hospital", "avoid oily food", "avoid non veg food", "keep mosquitos out"],
                "Rare -Fewer than 1 million cases per year (India)"],
    "Allergy": [["apply calamine", "cover area with bandage", "use ice to compress itching"],
                "Very common-More than 10 million cases per year (India)"],
    "Hypothyroidism": [["reduce stress", "exercise", "eat healthy", "get proper sleep"],
                        "Very common-More than 10 million cases per year (India)"],
    "Psoriasis": [["wash hands with warm soapy water", "stop bleeding using pressure", "consult doctor", "salt baths"],
                  "Very common-More than 10 million cases per year (India)"],
    "GERD": [["avoid fatty spicy food", "avoid lying down after eating", "maintain healthy weight", "exercise"],
             "Very common-More than 10 million cases per year (India)"],
    "Chronic_cholestasis": [["cold baths", "anti itch medicine", "consult doctor", "eat healthy"],
                             "Common -More than 1 million cases per year (India)"],
    "hepatitis_A": [["Consult nearest hospital", "wash hands through", "avoid fatty spicy food", "medication"],
                     "Rare -Fewer than 1 million cases per year (India)"],
    "Osteoarthristis": [["acetaminophen", "consult nearest hospital", "follow up", "salt baths"],
                         "Very common-More than 10 million cases per year (India)"],
    "Paroymsal_Positional_Vertigo": [["lie down", "avoid sudden change in body", "avoid abrupt head movment", "relax"],
                                      "Common -More than 1 million cases per year (India)"],
    "Hypoglycemia": [["lie down on side", "check in pulse", "drink sugary drinks", "consult doctor"],
                      "Common -More than 1 million cases per year (India)"],
    "Acne": [["bath twice", "avoid fatty spicy food", "drink plenty of water", "avoid too many products"],
             "Very common-More than 10 million cases per year (India)"],
    "Diabetes": [["have balanced diet", "exercise", "consult doctor", "follow up"],
                 "Very common-More than 10 million cases per year (India)"],
    "Impetigo": [["soak affected area in warm water", "use antibiotics", "remove scabs with wet compressed cloth", "consult doctor"],
                 "Very common-More than 10 million cases per year (India)"],
    "Hypertension": [["meditation", "salt baths", "reduce stress", "get proper sleep"],
                      "Very common-More than 10 million cases per year (India)"],
    "Peptic_ulcer_diseae": [["avoid fatty spicy food", "consume probiotic food", "eliminate milk", "limit alcohol"],
                             "Common -More than 1 million cases per year (India)"],
    "Dimorphic_hemmorhoids": [["avoid fatty spicy food", "consume witch hazel", "warm bath with epsom salt", "consume alovera juice"],
                                "Very common-More than 10 million cases per year (India)"],
    "Common_Cold": [["drink vitamin c rich drinks", "take vapour", "avoid cold food", "keep fever in check"],
                     "Very common-More than 10 million cases per year (India)"],
    "Chicken_pox": [["use neem in bathing", "consume neem leaves", "take vaccine", "avoid public places"],
                    "Rare -Fewer than 1 million cases per year (India)"],
    "Cervical_spondylosis": [["use heating pad or cold pack", "exercise", "take otc pain reliver", "consult doctor"],
                              "Very common-More than 10 million cases per year (India)"],
    "Hyperthyroidism": [["eat healthy", "massage", "use lemon balm", "take radioactive iodine treatment"],
                         "Very common-More than 10 million cases per year (India)"],
    "Urinary_tract_infection": [["drink plenty of water", "increase vitamin c intake", "drink cranberry juice", "take probiotics"],
                                 "Very common-More than 10 million cases per year (India)"],
    "Varicose_veins": [["lie down flat and raise the leg high", "use oinments", "use vein compression", "dont stand still for long"],
                        "Very common-More than 10 million cases per year (India)"],
    "AIDS": [["avoid open cuts", "wear ppe if possible", "consult doctor", "follow up"],
             "Common -More than 1 million cases per year (India)"],
    "Paralysis_brain_hemorrhage": [["massage", "eat healthy", "exercise", "consult doctor"],
                                    "Common -More than 1 million cases per year (India)"],
    "Typhoid": [["eat high calorie vegitables", "antiboitic therapy", "consult doctor", "medication"],
                "Very rare- Fewer than 100 thousand cases per year (India)"],
    "Hepatitis_B": [["consult nearest hospital", "vaccination", "eat healthy", "medication"],
                     "Rare -Fewer than 1 million cases per year (India)"],
    "Fungal_infection": [["bath twice", "use detol or neem in bathing water", "keep infected area dry", "use clean cloths"],
                          "Common -More than 1 million cases per year (India)"],
    "Hepatitis_C": [["Consult nearest hospital", "vaccination", "eat healthy", "medication"],
                     "Rare -Fewer than 1 million cases per year (India)"],
    "Migraine": [["meditation", "reduce stress", "use poloroid glasses in sun", "consult doctor"],
                 "Very common-More than 10 million cases per year (India)"],
    "Bronchial_Asthma": [["switch to loose cloothing", "take deep breaths", "get away from trigger", "seek help"],
                          "Very common-More than 10 million cases per year (India)"],
    "Alcoholic_hepatitis": [["stop alcohol consumption", "consult doctor", "medication", "follow up"],
                             "Rare -Fewer than 1 million cases per year (India)"],
    "Jaundice": [["drink plenty of water", "consume milk thistle", "eat fruits and high fiberous food", "medication"],
                 "Common -More than 1 million cases per year (India)"],
    "Hepatitis_E": [["stop alcohol consumption", "rest", "consult doctor", "medication"],
                     "Rare -Fewer than 1 million cases per year (India)"],
    "Dengue": [["drink papaya leaf juice", "avoid fatty spicy food", "keep mosquitos away", "keep hydrated"],
               "Very rare- Fewer than 100 thousand cases per year (India)"],
    "Hepatitis_D": [["consult doctor", "medication", "eat healthy", "follow up"],
                     "Rare -Fewer than 1 million cases per year (India)"],
    "Heart_attack": [["call ambulance", "chew or swallow asprin", "keep calm", ""],
                     "Very common-More than 10 million cases per year (India)"],
    "Pneumonia": [["consult doctor", "medication", "rest", "follow up"],
                   "Very common-More than 10 million cases per year (India)"],
    "Arthritis": [["exercise", "use hot and cold therapy", "try acupuncture", "massage"],
                   "Very common-More than 10 million cases per year (India)"],
    "Gastroenteritis": [["stop eating solid food for while", "try taking small sips of water", "rest", "ease back into eating"],
                         "Very common-More than 10 million cases per year (India)"],
    "Tuberculosis": [["cover mouth", "consult doctor", "medication", "rest"],
                      "Common -More than 1 million cases per year (India)"]
}


    for disease_name in predicted_disease:
        precautions = disease_info[disease_name][0]
        # precautions2 = disease_info[disease_name][0][1]
        # precautions3 = disease_info[disease_name][0][2]
        # precautions4 = disease_info[disease_name][0][3]
        occurrences = disease_info[disease_name][1]
        print("Precautions for", disease_name, ":", precautions)
        print("Occurrence of the disease:", occurrences)

    
    return render_template('desease.html', predicted_disease=predicted_disease, precautions=precautions, occurrences=occurrences)

@app.route('/nearby_hospitals')
def nearby_hospitals():
    
    
    return render_template('nearby_hospitals.html')

@app.route('/hospital_info', methods=['POST'])
def hospital_info():
  
    if request.method == 'POST':
        # Get the JSON data from the request
        data = request.get_json()

        # Process the received data as needed
        # For example, you can print the received data
        print("Received hospital names:", data)

        # You can also return a response if needed
        return jsonify({'message': 'Data received successfully'})
    else:
        return jsonify({'message not recieved'})

@app.route('/hospital_info1', methods=['POST'])
def hospital_info1():
  
    if request.method == 'POST':
        # Get the JSON data from the request
        data1 = request.get_json()
        hospital_in = get_hospital_info(data1)
        print(hospital_in)
        
        if hospital_in:
            
            return render_template('prof.html',hospital_in=hospital_in)
        else:
            return "Hospital not found."

        # Process the received data as needed
        # For example, you can print the received data
        print("Received hospital names:", data1)

        # You can also return a response if needed
        return jsonify({'message': 'Data received successfully'})
    else:
        return jsonify({'message not recieved'})



# @app.route('/')
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         aadhar = request.form['aadhar']
#         password = request.form['password']
#         # table=request.form['personal'].strip("'")
#         cursor = mydb.cursor(dictionary=True)
#         if request.form['personal']=='patient_info':
#             cursor.execute('SELECT * FROM patient_info WHERE patient_aadhar = %s AND patient_pass = %s', (aadhar, password))
#         elif request.form['personal']=='doctor_info':
#             cursor.execute('SELECT * FROM doctor_info WHERE doctor_aadhar = %s AND doctor_pass = %s', (aadhar, password))    
#         elif request.form['personal']=='hospital_info':
#             cursor.execute('SELECT * FROM hospital_info WHERE hospital_aadhar = %s AND hospital_pass = %s', (aadhar, password))    
#         account = cursor.fetchone()
#         if account:
#             session['loggedin'] = True
#             return render_template('/pateint_home')
#         else:
#             return 'Incorrect aadhar/password!'
#     return render_template('login.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
       
#         table=request.form['personal']
#         return render_template(f'{table}.html')
    
#     return render_template('register.html')

# # @app.route('/')
# @app.route('/patinfo', methods=['GET', 'POST'])
# def patinfo():
#     if request.method == 'POST':
#         aadhar_number = request.form['aadhar']
#         first_name = request.form['firstName']
#         middle_name = request.form['middleName']
#         last_name = request.form['lastName']
#         dob = request.form['dob']
#         gender = request.form['gender']
#         age = request.form['age']
#         passw = request.form['pass']

#         session['aadhar']=aadhar_number
#         # Connect to MySQL
#         mydb = mysql.connector.connect(
#             host=app.config['MYSQL_HOST'],
#             user=app.config['MYSQL_USER'],
#             password=app.config['MYSQL_PASSWORD'],
#             database=app.config['MYSQL_DB']
#         )

#         mycursor = mydb.cursor()

#         # Insert into the database
#         query = "INSERT INTO patient_info (patient_aadhar, patient_fname, patient_mname, patient_lname, patient_dob, patient_gender, patient_age, patient_pass) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
#         values = (aadhar_number, first_name, middle_name, last_name, dob, gender, age,passw)
        

#         mycursor.execute(query, values)

       
#         mydb.commit()
#         mycursor.close()

#         return render_template('patcont.html')

#     return render_template('patinfo.html')

# @app.route('/patcont', methods=['GET', 'POST'])
# def patcont():
#     if request.method == 'POST':
#         aadhar=session.get('aadhar')  
#         mobile = request.form['phone']
#         email = request.form['email']
#         street = request.form['street']
#         state = request.form['state']
#         district = request.form['district']
#         zipcode = request.form['zipcode']
#         city=request.form['city']

#         # Connect to MySQL
#         mydb = mysql.connector.connect(
#             host=app.config['MYSQL_HOST'],
#             user=app.config['MYSQL_USER'],
#             password=app.config['MYSQL_PASSWORD'],
#             database=app.config['MYSQL_DB']
#         )

#         mycursor = mydb.cursor()

#         # Insert into the database
#         query = "INSERT INTO patient_contact (patient_aadhar,patient_street,patient_city, patient_district, patient_state, patient_zipcode,patient_phone,patient_email) VALUES (%s, %s, %s, %s, %s, %s ,%s ,%s)"
#         values = (aadhar,street,city,district,state,zipcode,mobile,email)

#         mycursor.execute(query, values)
#         mydb.commit()
#         mycursor.close()

#         return render_template('patient_home.html')

#     return render_template('patcont.html')


# @app.route('/docinfo', methods=['GET', 'POST'])
# def docinfo():
#     if request.method == 'POST':
        
#         aadhar = request.form['aadhar']
#         fname = request.form['firstname']
#         mname = request.form['middlename']
#         lname = request.form['lastname']
#         gender = request.form['gender']
#         dob = request.form['dob']
#         age = request.form['age']
#         passw = request.form['pass']
        
#         session['aadhar']=aadhar

#         # Connect to MySQL
#         mydb = mysql.connector.connect(
#             host=app.config['MYSQL_HOST'],
#             user=app.config['MYSQL_USER'],
#             password=app.config['MYSQL_PASSWORD'],
#             database=app.config['MYSQL_DB']
#         )

#         mycursor = mydb.cursor()

#         # Insert into the database
#         query = "INSERT INTO doctor_info (doctor_aadhar,doctor_fname,doctor_mname,doctor_lname,doctor_gender,doctor_DOB,doctor_age,doctor_pass) VALUES (%s, %s, %s, %s, %s ,%s ,%s ,%s )"
#         values = (aadhar,fname,mname,lname,gender,dob,age,passw)

#         mycursor.execute(query, values)
#         mydb.commit()
#         mycursor.close()

#         return render_template('doccont.html')

#     return render_template('docinfo.html')

# @app.route('/patient_home')
# def patient_home():
#     return render_template('\patient_home')

# @app.route('/doccont', methods=['GET', 'POST'])
# def doccont():
#     if request.method == 'POST':
#         aadhar=session.get('aadhar')
#         registr = request.form['registration']
#         dept = request.form['department']
#         phone = request.form['mobile']
#         email = request.form['email']
        
        

#         # Connect to MySQL
#         mydb = mysql.connector.connect(
#             host=app.config['MYSQL_HOST'],
#             user=app.config['MYSQL_USER'],
#             password=app.config['MYSQL_PASSWORD'],
#             database=app.config['MYSQL_DB']
#         )

#         mycursor = mydb.cursor()

#         # Insert into the database
#         query = "INSERT INTO doctor_contact (doctor_aadhar,doctor_hospitalregistnum,doctor_number,doctor_departname,doctor_emaill) VALUES (%s, %s, %s, %s, %s )"
#         values = (aadhar,registr,phone,dept,email)

#         mycursor.execute(query, values)
#         mydb.commit()
#         mycursor.close()

#         return render_template('doclic.html')

#     return render_template('doccont.html')



# @app.route('/doclic', methods=['GET', 'POST'])
# def doclic():
#     if request.method == 'POST':
#         aadhar=session.get('aadhar')
#         lic = request.form['license']
#         spec = request.form['speciality']
#         validfr = request.form['effective']
#         validtil = request.form['expire']
#         status = request.form['status']
#         dea = request.form['DEA']
#         author = request.form['authority']
        
        

#         # Connect to MySQL
#         mydb = mysql.connector.connect(
#             host=app.config['MYSQL_HOST'],
#             user=app.config['MYSQL_USER'],
#             password=app.config['MYSQL_PASSWORD'],
#             database=app.config['MYSQL_DB']
#         )

#         mycursor = mydb.cursor()

#         # Insert into the database
#         query = "INSERT INTO doctor_license (doctor_aadhar,doctor_licensenum,doctor_speciality,doctor_datelicensure,doctor_expiration,doctor_licensestatus,doctor_DEAregistraion,doctor_licenseauthor) VALUES (%s, %s, %s, %s ,%s ,%s ,%s )"
#         values = (aadhar,lic,spec,validfr,validtil,status,dea,author)

#         mycursor.execute(query, values)
#         mydb.commit()
#         mycursor.close()

#         return render_template('hospital_dash.html')

#     return render_template('doclic.html')

# @app.route('/hosinfo', methods=['GET', 'POST'])
# def hosinfo():
#     if request.method == 'POST':
          
#         registr = request.form['registr']
#         name = request.form['name']
#         type = request.form['type']
#         passw= request.form['pass']
    
#         session['registr']=registr

#         # Connect to MySQL
#         mydb = mysql.connector.connect(
#             host=app.config['MYSQL_HOST'],
#             user=app.config['MYSQL_USER'],
#             password=app.config['MYSQL_PASSWORD'],
#             database=app.config['MYSQL_DB']
#         )

#         mycursor = mydb.cursor()

#         # Insert into the database
#         query = "INSERT INTO hospital_info (hospital_registrationnum,hospital_name,hospital_type,hospital_pass) VALUES (%s, %s, %s, %s)"
#         values = (registr,name,type,passw)

#         mycursor.execute(query, values)
#         mydb.commit()
#         mycursor.close()

#         return render_template('hoscont.html')

#     return render_template('hosinfo.html')

# @app.route('/hoscont', methods=['GET', 'POST'])
# def hoscont():
#     if request.method == 'POST':
#         registr=session.get('registr')        
#         street = request.form['street']
#         city = request.form['city']
#         district = request.form['district']
#         state = request.form['state']
#         zip = request.form['zipcode']
#         recep = request.form['recepnum']
#         admin = request.form['adminnum']
#         emerg = request.form['emergnum']
#         email = request.form['email']
        
        
    
        

#         # Connect to MySQL
#         mydb = mysql.connector.connect(
#             host=app.config['MYSQL_HOST'],
#             user=app.config['MYSQL_USER'],
#             password=app.config['MYSQL_PASSWORD'],
#             database=app.config['MYSQL_DB']
#         )

#         mycursor = mydb.cursor()

#         # Insert into the database
#         query = "INSERT INTO hospital_contact (hospital_registrationnum,hospital_street,hospital_city,hospital_district,hospital_state,hospital_zipcode,hospital_receptionnum,hospital_administrationnum,hospital_emergencynum,hospital_email) VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s)"
#         values = (registr,street,city,district,state,zip,recep,admin,emerg,email)

#         mycursor.execute(query, values)
#         mydb.commit()
#         mycursor.close()

#         return render_template('hosleg.html')

#     return render_template('hoscont.html')

# @app.route('/hosleg', methods=['GET', 'POST'])
# def hosleg():
#         if request.method == 'POST':
#             registr=session.get('registr')  
#             type = request.form['type']
#             license = request.form['license']

         
#             # file = request.files['file']
#             # if file:
#             #     content = file.read()  # Read the file content
#             #     cursor = mysql.connection.cursor()
#             #     cursor.execute("INSERT INTO documents (content) VALUES (%s)", (content,))
#             #     mysql.connection.commit()
#             #     cursor.close()
#             #     return "File uploaded successfully"
#             # return "No file provided"
       
#         # Connect to MySQL
#         mydb = mysql.connector.connect(
#             host=app.config['MYSQL_HOST'],
#             user=app.config['MYSQL_USER'],
#             password=app.config['MYSQL_PASSWORD'],
#             database=app.config['MYSQL_DB']
#         )

#         mycursor = mydb.cursor()

#         # Insert into the database
#         query = "INSERT INTO hospital_legalinfo (hospital_registrationnum,hospital_typeoforaniz,hospital_licensenum) VALUES (%s, %s, %s)"
#         values = (registr,type,license)

#         mycursor.execute(query, values)
#         mydb.commit()
#         mycursor.close()

#         return render_template('hoslog.html')

#     # return render_template('hosleg.html')


# Function to retrieve information about a specific hospital from the database
def get_hospital_info(hospital_name):
    mydb = mysql.connector.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB']
        )  # Replace 'your_database.db' with your actual database file
    cursor = mydb.cursor()
    # Modify the SQL query to select only specific fields
    cursor.execute('''
    SELECT hospital_info.hospital_name, hospital_contact.hospital_receptionnum, hospital_info.hospital_type, hospital_contact.hospital_city 
    FROM hospital_info 
    JOIN hospital_contact ON hospital_info.hospital_registrationnum = hospital_contact.hospital_registrationnum
    WHERE hospital_info.hospital_name = %s
''', (hospital_name,))
    
    hospital_in = cursor.fetchone()
    # print(hospital_in)
    mydb.close()
    return hospital_in

# @app.route('/')
#def home():
   # return render_template('near.html')

# @app.route('/near', methods=['POST'])
# def near():
#     if request.method == 'POST':  
#         hospital_name = request.form['type']
#         hospital_in = get_hospital_info(hospital_name)
#         print(hospital_in)
#         if hospital_in:
#             return render_template('prof.html', hospital_in=hospital_in)
#         else:
#             return "Hospital not found."
#     return render_template('near.html')

@app.route('/prof/<hospital_name>')
def prof(hospital_name):
    # Use hospital_name as needed
    hospital_in=get_hospital_info(hospital_name)
    
    return render_template('prof.html', hospital_info=hospital_in)




if __name__ == '__main__':
    app.run(debug=True)
