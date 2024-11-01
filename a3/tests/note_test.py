from unittest import TestCase
from unittest import main
from clinic.controller import Controller
from clinic.patient import Patient
from clinic.patient_record import PatientRecord
from clinic.note import Note

class NoteTests(TestCase):

    def test_note_equality(self):
        note1 = Note(1, "Patient comes with headache and high blood pressure.")
        note2 = Note(2, "Patient complains of a strong headache on the back of neck.")
        note3 = Note(1, "Patient comes with headache and high blood pressure.")

        # test equality
        self.assertTrue(note1 == note3)
        # test inequality
        self.assertFalse(note1 == note2)

    def test_note_str(self):
        note1 = Note(1, "Patient comes with headache and high blood pressure.")
        note_expected = "Index: 1, Description: Patient comes with headache and high blood pressure."

        # test str output
        self.assertEqual(str(note1), note_expected)

if __name__ == '__main__':
    main()