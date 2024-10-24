from clinic.patient import Patient
from clinic.patient_record import PatientRecord
from clinic.note import Note
 

class Controller():

    def __init__(self):
        self.patients = [] # List of Patient instances
        self.login = [] # List of Patient logins  
        self.current_patient = None 
        self.username = "user"
        self.password = "clinic2024"
        self.loggedIn = False

    # input: username, password
    def login(self, user, pword):
        if self.loggedIn:
             return False
        else:
            if user == self.username and pword == self.password:
                self.loggedIn = True
                return True


    # input: none
    def logout(self):
        if self.loggedIn:
            self.loggedIn = False
            return True
        else:
            return False
