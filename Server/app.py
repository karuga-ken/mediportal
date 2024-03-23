from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from models import db, Doctor, Patient, PatientRecord
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)
CORS(app)

# doctor registration endpoint
class RegsiterDoc(Resource):
    def post(self):
        # change to request.json when linking 
        data = request.json 

        new_doc = Doctor(
            name = data['name'],
            email = data['email'],
            password = data['password']
        )

        # queries the database to check for existing doctor
        doctor = Doctor.query.filter(Doctor.email == new_doc.email).first()

        if doctor is not None:
            response = make_response(
                jsonify({
                    'error': 'Account Already Exists!!'
                }), 401
            )
            return response
        
        # add the new doctor if they dont have an account
        db.session.add(new_doc)
        db.session.commit()

api.add_resource(RegsiterDoc, '/auth/registedoc')

# endpoint for login doctor
class DocLogin(Resource):
    def post(self):

        email = request.json['email']
        password = request.json['password']

        doctor = Doctor.query.filter(Doctor.email == email).first()

        if not doctor:
            response = make_response(
                jsonify({
                    "error": "Account not Found!!"
                }), 401
            )
            return response
        
        doctor_password = Doctor.query.filter(Doctor.password == password).first()

        if not doctor_password:
            response = make_response(
                jsonify({
                    "error": "check password!"
                }),401
            )
            return response
        response_data = {
            "message": "Log in Successful" 
        }
        response = jsonify(response_data)
        return response
    
api.add_resource(DocLogin, "/auth/doctorlogin")

#endpoint for patient registration
class RegisterPatient(Resource):

    def post(self):

        data = request.json

        new_patient = Patient(
            name = data['name'],
            email = data["email"],
            nationalno = data['nationalno'],
            password = data['password']
        )

        patient = Patient.query.filter(Patient.nationalno == new_patient.nationalno).first()

        if patient is not None:
            response = make_response(
                jsonify({
                    "error": "Account Exists!!"
                }), 401
            )
            return response
        
        db.session.add(new_patient)
        db.session.commit()

api.add_resource(RegisterPatient, "/auth/registerpatient")

# patient login endpoint

class PatientLogin(Resource):
    def post(self):

        nationalno = request.form['nationalno']
        password = request.form['password']

        patient_nationalno = Patient.query.filter(Patient.nationalno == nationalno).first()

        if not patient_nationalno:
            response = make_response(
                jsonify({
                    "error": "Account not Found!!"
                }), 401
            )
            return response
        
        patient_password = Patient.query.filter(Patient.password == password).first()

        if not patient_password:
            response = make_response(
                jsonify({
                    "error": "Check Password"
                }), 401
            )
            return response
        
        response_data = {
            "message": "Login Successful"
        }

        response = jsonify(response_data)
        return response

api.add_resource(PatientLogin, "/auth/patientlogin")

class PostPatientRecord(Resource):
    def post(self):
        data = request.form

        new_post = PatientRecord(
            nationalno = data['nationalno'],
            hospital = data['hospital'],
            DoctorName = data['DoctorName'],
            date = data['date']
        )

        db.session.add(new_post)
        db.session.commit()
api.add_resource(PostPatientRecord, '/addpatientrecord')

if __name__ == '__main__':
    app.run(port = 7777, debug=True)
