from unittest import TestCase
from unittest import main
from clinic.controller import Controller
from clinic.patient import Patient
from clinic.patient_record import PatientRecord
from clinic.note import Note

class PatientTests(TestCase):
    def setUp(self):
        self.controller = Controller()
    
    
