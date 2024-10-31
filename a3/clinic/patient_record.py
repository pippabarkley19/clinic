from clinic.note import Note
#from controller import loggedIn

class PatientRecord:
    
    def __init__(self):
        self.notes = []
        self.counter = 1
    
    def create_note(self, text):
        note = Note(self.counter, text)  # Removed `index` parameter as it wasn't needed
        self.notes.append(note)
        self.counter += 1  # Increment counter for unique note indices
        return note

    """
    def create_note(self, index, text):
        #if self.loggedIn:
        note = Note(text, indexs)
        self.notes.append(note)
        #else:
           #return None
    """


