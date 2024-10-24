# not sure which imports we should do here, so delete unnecessary ones when we find out
#from clinic.patient_record import PatientRecord
#from clinic.patient import Patient
#from clinic.controller import Controller

#going to need to import date time library
import datetime 
from controller import reocrds

class Note:
    def __init__(self, index, description, timestamp):
        self.index = index
        self.description = description
        self.timestamp = timestamp
        
    def create_note():
        # input: current patient
        new_note = cls(index, description, timestamp)
        my_record.appened(new_note)
        




    def search_note():
        # input: current patient, desired text
     
    def update_note():
        # input: current patient, note code

    def delete_note():
        # input: current patient, note code