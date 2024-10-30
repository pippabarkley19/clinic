from datetime import datetime
#from controller import loggedIn

class Note:
    def __init__(self, index, description):
        self.index = index
        self.description = description
        self.timestamp = datetime.now()

    def search_note(self, index):
        #if self.loggedIn:
        patient =  self.search(self.current_patient.phn)
        for note in patient.notes:
            if (index == note.index):
                return note
            else:
                return None
        #else:
            #return None
     
    def update_note(self, index, description, timestamp):
        #if self.loggedIn:
        note = self.search_note(index)
        if note:
            note.index = index 
            note.description = description
            note.timestamp = timestamp
            return True
        else:
            return False
        #else:
            #return False

    def delete_note(self, index):
        #if self.loggedIn:
        note = self.search_note(index)
        if note:
            self.notes.remove(note)
            return True
        else:
            return False
        #else:
            #return False
        