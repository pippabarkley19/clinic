from clinic.note import Note
#from controller import loggedIn

class PatientRecord:
    
    def __init__(self):
        self.notes = []
        self.counter = 0

    def create_note(self, index, text):
        #if self.loggedIn:
        note = Note(text, indexs)
        self.notes.append(note)
        #else:
           #return None

    def list_notes(self):
        #if self.loggedIn:
        notes_list = []
        for note in self.notes:
            notes_list.append(note)
        return notes_list
        #else: 
            #return None
