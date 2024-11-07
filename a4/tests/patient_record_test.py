from unittest import TestCase
from unittest import main
from clinic.patient_record import PatientRecord
from clinic.note import Note

class PatientRecordTests(TestCase):
    
    def test_patient_record_create_note(self):
        
        # set up test items
        record = PatientRecord()
        note1_text = "Patient comes with headache and high blood pressure."     
        note1 = record.create_note(note1_text)
        note_expected = Note(1, note1_text)
        note_not_expected = Note(2, note1_text)
        
        # test properly created
        self.assertIsNotNone(record.create_note(note1_text))
        # test equality
        self.assertEqual(note1, note_expected)
        # test inequality
        self.assertNotEqual(note1, note_not_expected)

if __name__ == '__main__':
    main()