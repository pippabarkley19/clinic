from unittest import TestCase
from unittest import main
from clinic.note import Note

class NoteTests(TestCase):

    def test_note_equality(self):

        #set up testing items
        note1 = Note(1, "Patient comes with headache and high blood pressure.")
        note2 = Note(2, "Patient complains of a strong headache on the back of neck.")
        note3 = Note(1, "Patient comes with headache and high blood pressure.")

        # test equality
        self.assertTrue(note1 == note3)
        # test inequality
        self.assertFalse(note1 == note2)

    def test_note_str(self):

        # set up testing items
        note1 = Note(1, "Patient comes with headache and high blood pressure.")
        note_expected = "Index: 1, Description: Patient comes with headache and high blood pressure."
        note_not_expected = "Index: 2, Description: Patient comes with headache and high blood pressure."

        # test str correct output
        self.assertEqual(str(note1), note_expected)
        # test str incorrect output
        self.assertNotEqual(str(note1), note_not_expected)

if __name__ == '__main__':
    main()