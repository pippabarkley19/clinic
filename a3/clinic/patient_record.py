from clinic.note import Note

class PatientRecord:
    
    def __init__(self):
        self.notes = []
        self.counter = 0

    def create_note(self, index, text):
        note = Note(text, indexs)
        self.notes.append(note)

    def list_record(self):
        notes_list = []
        for note in self.notes:
            notes_list.append(note)
        return notes_list
