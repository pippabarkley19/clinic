from .patient import Patient
from .patient_record import PatientRecord
from .note import Note

# note that almost everty method checks to ensure that the user is logged in, even though it is not part of the user story, is required.

class Controller():

    def __init__(self):
        # initializes the controller with necessary fields to handle controller operations
        self.patients = []
        self.current_patient = None 
        self.username = "user"
        self.password = "clinic2024"
        self.loggedIn = False


    def login(self, user, pword):
        # takes a user and password and checks against correct pair, logs in if match
        # returns true to indicate success, false otherwise
        if self.loggedIn:
             return False
        if user == self.username and pword == self.password:
            self.loggedIn = True
            return True
        return False 

    def logout(self):
        # takes no parameters: if logged in, logged out, if  not logged in, do nothing
        # returns true to indicate success, false otherwise
        if self.loggedIn:
            self.loggedIn = False
            return True
        return False

    def create_note(self, text):
        # takes a piece of text and passes the call to patient which will eventually create the note in patient_record
        # its necessary to do this because there are fields only accessible in controller that are involved in creating a note
        # returns the 'note' which is just another call to create_note in patient.py
        if self.loggedIn and self.current_patient:
            note = self.current_patient.record.create_note(text)
            return note
        return None

    def delete_patient(self,PHN):
       # checks if the instance exists and deletes it, if it doesn't exist, return false
       # returns true to indicate success
        if not self.loggedIn or (self.current_patient and self.current_patient.phn == PHN):
            return False
        patient = self.search_patient(PHN)
        if patient:
            self.patients.remove(patient)
            return True
        return False
            
    def update_patient(self, old_PHN, new_PHN, name, birthday, phone, email, address):
        #  checks if the patient (identified by PHN) already exists, then updates given parameters accordingly
        # returns true to indicate success
        if not self.loggedIn or (self.current_patient and self.current_patient.phn == old_PHN):
            return False
        if self.search_patient(new_PHN) and old_PHN != new_PHN:
            return False
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
     
    def update_note(self, index, description, timestamp=None):
        # first checks if there is a current patient, searches the note by index for the current patient, then updates the note at that index accordingly
        # returns true to indicate success
        if not self.loggedIn or not self.current_patient:
            return None
        note = self.search_note(index)
        if note:
            note.description = description
            note.timestamp = timestamp or note.timestamp
            return True
        return False

    def get_current_patient(self):
        # returns the object set as current patient given that there is a current_patient
        return self.current_patient if self.loggedIn and self.current_patient else None

    def retrieve_patients(self, name):
        # creates a new empty list holding the patient instances that match the name provided
        # returns the list of objects with the matching names
        if not self.loggedIn:
            return None
        # list of matches is populated with specific instance patient in collection patients if the name provided matches the patient namee
        matches = [patient for patient in self.patients if name in patient.name]
        return matches

    def list_patients(self):
        # returns the list of patients
        return self.patients if self.loggedIn else None
    

    def list_notes(self):
        # returns the reversed order of the current patients notes
        if not self.loggedIn or not self.current_patient:
            return None
        return list(reversed(self.current_patient.record.notes))  

    def search_patient(self, PHN):
        # iterates through list of patients and returns object with matching PHN
        for patient in self.patients:
            if patient.phn == PHN:
                return patient
        return None

    def delete_note(self, index):
        # if the note exists, remove the object from the current patient's collection of notes, return true if successful, otherwise return false
        if not self.loggedIn or not self.current_patient:
            return False
        note = self.search_note(index)
        if note:
            self.current_patient.record.notes.remove(note)
            return True
        return False

    def create_patient(self, PHN, name, birthday, phone, email, address):
        # check if the patient already exists via searching the PHN, if they dont exist, create a new object witht the parameters provided, and return true to indicate success
        if not self.loggedIn:
            return None
        if not self.search_patient(PHN):
            patient = Patient(PHN, name, birthday, phone, email, address)
            self.patients.append(patient)
            return patient
        return None


    def set_current_patient(self, PHN):
        # find the instance of the patient by searching by PHN, if it exists, set the object as current patient, return true to indicate success
        if not self.loggedIn:  # Check if logged in
            return None
        patient = self.search_patient(PHN)
        if patient:
            self.current_patient = patient
            return True
        return None

    def search_note(self, index):
        # if current_patient is set, traverse through that patients collection of notes, and return the note object with the matching index
        if self.current_patient:
            for note in self.current_patient.record.notes:  
                if index == note.index:
                    return note
        return None

    def retrieve_notes(self, description):
        # returns the instance of note that matches the note in the current patient's collection with the same description
        if not self.loggedIn or not self.current_patient:
            return None
        return [note for note in self.current_patient.record.notes if description in note.description]
        return matches
    
    def unset_current_patient(self):
        # sets current_patient to None
        self.current_patient = None