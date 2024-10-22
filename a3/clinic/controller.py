from clinic.patient import Patient
from clinic.patient_record import PatientRecord
from clinic.note import Note
 

class Controller():

    def __init__(self):
        self.patients = [] # List of Patient instances
        self.login = [] # List of Patient logins  
        self.current_patient = None 

    # not sure if this will need an init
    # input: username, password
    def login(self):

    # input: none
    def logout(self):

