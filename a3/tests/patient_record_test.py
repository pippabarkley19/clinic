from unittest import TestCase
from unittest import main
from clinic.controller import Controller
from clinic.patient import Patient
from clinic.patient_record import PatientRecord
from clinic.note import Note

class PatientRecordTests(TestCase):
    
    def test_patient_record_create_note(self):
        record = PatientRecord()   
             
        note1 = record.create_note("Patient comes with headache and high blood pressure.")
        note_expected = Note(1, "Patient comes with headache and high blood pressure.")
        note_not_expected = Note(2, "Patient comes with headache and high blood pressure")
        
        # test properly created
        self.assertEqual(note1, note_expected)
        # test inequality
        self.assertNotEqual(note1, note_not_expected)

if __name__ == '__main__':
    main()