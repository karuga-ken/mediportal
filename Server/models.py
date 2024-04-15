from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Doctor(db.Model):

    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)


    def __repr__(self) -> str:
        return f'{self.id}, {self.name}, {self.email}, {self.password}'
    
class Patient(db.Model):

    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    nationalno = db.Column(db.Integer, unique = True)
    password = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f'{self.id}, {self.name}, {self.email}, {self.nationalno}, {self.password}'
    

class PatientRecord(db.Model):

    __tablename__ = 'patientrecords'

    id = db.Column(db.Integer, primary_key = True)
    nationalno = db.Column(db.Integer)
    hospital = db.Column(db.String)
    DoctorName = db.Column(db.String)
    date = db.Column(db.Integer)



    def __repr__(self) -> str:
        return f'{self.nationalno}, {self.hospital},  {self.DoctorName}, {self.date}'
    
  