from unittest import TestCase
from unittest import main
from clinic.patient import Patient

class PatientTests(TestCase):
    
    def test_patient_eq(self):

        # set up test items
        patient1 = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        patient2 = Patient(9790014444, "Mary Doe", "1995-07-01", "250 203 2020", "mary.doe@gmail.com", "300 Moss St, Victoria")
        patient3 = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        patient4 = Patient(9790012000, "John Smith", "2000-11-10", "250 204 1010", "john.smith@gmail.com", "310 Moss St, Victoria")

        # test equality
        self.assertTrue(patient1 == patient3)

        # test inequality
        self.assertFalse(patient1 == patient2)
        self.assertFalse(patient1 == patient4)

    def test_patient_str(self):

        # set up test items
        patient1 = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        desired_output_1 = "Patient: John Doe, Birthday: 2000-10-10"
        patient2 = Patient(9790014444, "Mary Doe", "1995-07-01", "250 203 2020", "mary.doe@gmail.com", "300 Moss St, Victoria")
        desired_output_2 = "Patient: Mary Doe, Birthday: 1995-07-01"

        # test correct output
        self.assertEqual(str(patient1), desired_output_1)
        self.assertEqual(str(patient2), desired_output_2)

        # test incorrect output
        self.assertNotEqual(str(patient1), desired_output_2)
        self.assertNotEqual(str(patient2), desired_output_1)

if __name__ == '__main__':
    main()
    
    
