from unittest import TestCase
from unittest import main
from clinic.controller import Controller
from clinic.patient import Patient
from clinic.patient_record import PatientRecord
from clinic.note import Note

class PatientTests(TestCase):
    
    def test_patient_eq(self):

        self.controller = Controller()

        patient1 = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        patient2 = Patient(9790014444, "Mary Doe", "1995-07-01", "250 203 2020", "mary.doe@gmail.com", "300 Moss St, Victoria")
        patient3 = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")

        # test equality
        self.assertTrue(patient1 == patient3)
        # test inequality
        self.assertFalse(patient1 == patient2)

    def test_patient_str(self):

        self.controller = Controller()

        patient1 = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        desired_output_1 = "Patient: John Doe, Birthday: 2000-10-10"

        # test output
        self.assertEqual(str(patient1), desired_output_1)

if __name__ == '__main__':
    main()
    
    
