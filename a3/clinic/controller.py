from .patient import Patient
from .patient_record import PatientRecord
from .note import Note

#loggedIn = False

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
        if user == self.username and pword == self.password:
            self.loggedIn = True
            return True
        return False 

    # input: none
    def logout(self):
        if self.loggedIn:
            self.loggedIn = False
            return True
        return False

    def create_note(self, text):
        if self.loggedIn and self.current_patient:
            note = self.current_patient.record.create_note(text)
            return note
        return None

    """
    def create_note(self,text):
        #check login 
        #check current_patient 
            #self.current_patient.create_note(text)
        if self.loggedIn and self.current_patient:
            self.current_patient.record.create_note(text)
            return True
        return None
    """

    def delete_patient(self,PHN):
       # if self.loggedIn:
        if not self.loggedIn or (self.current_patient and self.current_patient.phn == PHN):
            return False
        patient = self.search_patient(PHN)
        if patient:
            self.patients.remove(patient)
            return True
        return False
        #else:
            #return False
            
    def update_patient(self, old_PHN, new_PHN, name, birthday, phone, email, address):
        #if self.loggedIn:
        if not self.loggedIn or (self.current_patient and self.current_patient.phn == old_PHN):
            return False
        if self.search_patient(new_PHN) and old_PHN != new_PHN:
            return False  # Prevent update if the new PHN is already registered
        patient = self.search_patient(old_PHN)
        if patient:
            patient.phn = new_PHN
            patient.name = name
            patient.bday = birthday
            patient.phone = phone
            patient.email = email
            patient.address = address
            return True
        return None
    
    """
    def update_note(self, index, description, timestamp):
        #if self.loggedIn:
        note = self.search_note(index)
        if note:
            note.index = index 
            note.description = description
            note.timestamp = timestamp
            return True
        else:
            return False
        #else:
            #return False
    """
 
    def update_note(self, index, description, timestamp=None):
        if not self.loggedIn or not self.current_patient:
            return None
        note = self.search_note(index)
        if note:
            note.description = description
            note.timestamp = timestamp or note.timestamp
            return True
        return False

    def get_current_patient(self):
        return self.current_patient if self.loggedIn else None
    """
    def get_current_patient(self):
        #if self.loggedIn:
        if self.current_patient:
            return self.current_patient 
        return None
    """

    def retrieve_patients(self, name):
        if not self.loggedIn:
            return None
        matches = [patient for patient in self.patients if name in patient.name]
        return matches
    
    """
    def retrieve_patients(self,name):
        #if self.loggedIn:
        matches = [] 
        for patient in self.patients:
            if patient.name == name:
                matches.append(patient)
        return matches 
        #else:
            #return None
    """

    """
    def list_patients(self):
        #if self.loggedIn:
        patients_list = []
        for patient in self.patients:
            patients_list.append(patient)
        return patients_list
        #else:
            #return None
    """

    def list_patients(self):
        return self.patients if self.loggedIn else None
    

    """
    def list_notes(self):
        #if self.loggedIn:
        notes_list = []
        for note in self.notes:
            notes_list.append(note)
        return notes_list
        #else: 
            #return None
    """

    def list_notes(self):
        if not self.loggedIn or not self.current_patient:
            return None
        return list(reversed(self.current_patient.record.notes))  
        #return self.current_patient.record.notes

    def search_patient(self, PHN):
        #if self.loggedIn:
        for patient in self.patients:
            if patient.phn == PHN:
                return patient
        return None
        #else:
            #return None

    """
    def delete_note(self, index):
        #if self.loggedIn:
        note = self.search_note(index)
        if note:
            self.notes.remove(note)
            return True
        else:
            return False
        #else:
            #return False
    """

    def delete_note(self, index):
        if not self.loggedIn or not self.current_patient:
            return False
        note = self.search_note(index)
        if note:
            self.current_patient.record.notes.remove(note)
            return True
        return False

    def create_patient(self, PHN, name, birthday, phone, email, address):
        #if self.loggedIn:
        if not self.loggedIn:
            return None
        if not self.search_patient(PHN):
            patient = Patient(PHN, name, birthday, phone, email, address)
            self.patients.append(patient)
            return patient
        return None

    """
    def set_current_patient(self, PHN):
        #if self.loggedIn:
        patient = self.search_patient(PHN)
        if patient:
            for patient in self.patients:
                if patient.phn == PHN:
                    self.current_patient = patient
            return True
        else:
            return False
        #else:
            #return None
    """

    def set_current_patient(self, PHN):
        if not self.loggedIn:  # Check if logged in
            return None
        patient = self.search_patient(PHN)
        if patient:
            self.current_patient = patient
            return True
        return None
    
    """
    def search_note(self, index):
        #if self.loggedIn:
        patient =  self.search(self.current_patient.phn)
        for note in patient.notes:
            if (index == note.index):
                return note
            else:
                return None
        #else:
            #return None
    """

    def search_note(self, index):
        if self.current_patient:
            for note in self.current_patient.record.notes:  # Access notes from current patient's record
                if index == note.index:
                    return note
        return None

    def retrieve_notes(self, description):
        if not self.loggedIn or not self.current_patient:
            return None
        return [note for note in self.current_patient.record.notes if description in note.description]
        return matches
    
    def unset_current_patient(self):
        self.current_patient = None