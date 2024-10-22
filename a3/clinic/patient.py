from clinic.patient_record import PatientRecord
from clinic.note import Note
from controller import patients 
from controller import current_pateint 

class Patient:
    def __init__(self, PHN, name, birthday, phone, email, address):
        self.phn = PHN
        self.name = name
        self.bday = birthday
        self.phone = phone
        self.email = email
        self.address = address
        my_record = [] 

    def search_patient(PHN):
        # input: PHN
        for patient in patients:
            if patient.PHN == PHN:
                return patient
        return None

    def create_patient(cls, PHN, name, birthday, phone, email, address):
        # input: PHN, name, other personal data
        new_patient = cls(PHN, name, birthday, phone, email, address)
        patients.appened(new_patient)

    def retrieve_patients(name):
        # input: name
        matches = [] 
        for patient in patients:
            if patient.name == name:
                matches.apppend(patient)
        return matches 

    def update_patient(PHN, patient):
        # input: PHN
        if PHN is not None:
            self.phn = PHN
        if name is not None:
            self.name = name
        if bday is not None:
            self.bday = birthday
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email
        if address is not None:
            self.address = address

    def delete_patient(PHN):
        # input: PHN
        for patient in patients:
            if patient.PHN == PHN:
                patients.remove(patient)

    def list_patients():
        # input: none
        print(patients)

    def set_current_patient(PHN):
        for patient in patients:
            if patient.PHN == PHN:
                current_patient = patient

    def get_current_patient():
        # input: PHN
        return current_patient 

    
