# not sure which imports we should do here, so delete unnecessary ones when we find out
#from clinic.patient_record import PatientRecord
#from clinic.patient import Patient
#from clinic.controller import Controller

#going to need to import date time library
import datetime 
from clinic.controller import records
from clinic.patient import current_patient

class Note:
    def __init__(self, index, description, timestamp):
        self.index = index
        self.description = description
        self.timestamp = timestamp
        
    def create_note(self, description):
        # input: current patient
        if current_patient != None:
            new_note = cls(index, description, timestamp)
            current_patient.record.notes.appened(new_note)

    #def search_note():
        # input: current patient, desired text
     
    #def update_note():
        # input: current patient, note code

    #def delete_note():
        # input: current patient, note code