from clinic.patient_record import PatientRecord
from clinic.note import Note
from clinic.patient_record import PatientRecord
#from controller import loggedIn

class Patient:
    def __init__(self, PHN, name, birthday, phone, email, address):
        self.phn = PHN
        self.name = name
        self.bday = birthday
        self.phone = phone
        self.email = email
        self.address = address
        self.record = PatientRecord()
    
    def create_note(self, text):
        #if self.loggedIn:
        self.record.create_note(text)
        return True
        #else:
            #return None

    def __eq__(self, other):
        if isinstance(other, Patient):
            return (self.phn == other.phn and self.name == other.name and 
                    self.bday == other.bday and self.phone == other.phone and 
                    self.email == other.email and self.address == other.address)
        return False




    
