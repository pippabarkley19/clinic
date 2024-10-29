from clinic.patient_record import PatientRecord
from clinic.note import Note
from clinic.patient_record import PatientRecord

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
        record.create_note(text)
        
    def search_patient(self, PHN):
        for patient in self.patients:
            if (patient.phn == PHN):
                return patient
        return None
    
    def create_patient(self, PHN, name, birthday, phone, email, address):
        if self.loggedIn:
            if not self.search_patient(PHN):
                patient = Patient(PHN, name, birthday, phone, email, address)
                self.patients.append(patient)
                return True
            else:
                return False
        else:
            return False

    def retrieve_patients(self,name):
        matches = [] 
        for patient in patients:
            if patient.name == name:
                matches.apppend(patient)
        return matches 

    def update_patient(self, PHN, name, birthday, phone, email, address):
        patient = self.search_patient(PHN)
        if patient:
            patient.phn = PHN
            patient.name = name
            patient.bday = birthday
            patient.phone = phone
            patient.email = email
            patient.address = address
            return True
        else:
            return False

    def delete_patient(self,PHN):
        patient = self.search_patient(PHN)
        if patient:
            self.patient.remove(patient)
            return True
        else:
            return False

    def list_patients(self):
        patients_list = []
        for patient in self.patients:
            patients_list.append(patient)
        return patients_list

    def set_current_patient(self, PHN):
        patient = self.search_patient(PHN)
        if patient:
            for patient in self.patients:
                if patient.PHN == PHN:
                    self.current_patient = patient
            return True
        else:
            return False

    def get_current_patient(self):
        if self.current_pateint:
            return self.current_patient 
        else:
            return False

    
