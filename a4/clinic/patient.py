from .patient_record import PatientRecord
from .note import Note
from .patient_record import PatientRecord

class Patient:
    def __init__(self, PHN, name, birthday, phone, email, address):
        # initialized the patient object with the given parameters, as well as creates an instance of PatienttRecord for every patient
        self.phn = PHN
        self.name = name
        self.bday = birthday
        self.phone = phone
        self.email = email
        self.address = address
        self.record = PatientRecord()

    def __eq__(self, other):
        # defines what equality of patient objects means
        # returns true to indicate both objects exist
        if isinstance(other, Patient):
            return (self.phn == other.phn and self.name == other.name and 
                    self.bday == other.bday and self.phone == other.phone and 
                    self.email == other.email and self.address == other.address)
        return False
    
    def __str__(self):
        # defines what a string representation of patient objects should look like
        return f"Patient: {self.name}, Birthday: {self.bday}"

    def create_note(self, text):
        # once again passes this call to patient_record now that the patients record is accesible through self
        # returns true to indicate success
        self.record.create_note(text)
        return True






    
