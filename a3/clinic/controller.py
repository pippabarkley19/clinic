from clinic.patient import Patient
from clinic.patient_record import PatientRecord
from clinic.note import Note
 
class Controller():

    def __init__(self):
        self.patients = [] # List of Patient instances
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
        return False 


    # input: none
    def logout(self):
        if self.loggedIn:
            self.loggedIn = False
            return True
        else:
            return False

    def create_note(self,text):
        #check login 
        #check current_patient 
            #self.current_patient.create_note(text)
        if self.loggedIn and self.current_patient:
            self.current_patient.record.create_note(text)
            return True
        return None
    
    

    
