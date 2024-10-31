from .note import Note
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
<<<<<<< HEAD
        #if self.loggedIn:
        note = Note(text, indexs)
        self.notes.append(note)
        #else:
           #return None
    """


=======
        if self.loggedIn:
            note = Note(text, index)
            self.notes.append(note)
        else:
           return None

    def list_notes(self):
        if self.loggedIn:
            notes_list = []
            for note in self.notes:
                notes_list.append(note)
            return notes_list
        else: 
            return None
>>>>>>> 20ccd6a6cecf21290714baeebd1cf15e16bbe5da
