from .note import Note

class PatientRecord:
    
    def __init__(self):
        # initializes a collection of notes for every instance of patient record, as well as the counter which represents the index of each note
        self.notes = []
        self.counter = 1
    
    def create_note(self, text):
        # passed from controller > patient > here, and finally appends the note with the appropriate counter and text to the patient_record's collection of notes
        # returns a note object
        note = Note(self.counter, text) 
        self.notes.append(note)
        self.counter += 1 
        return note


