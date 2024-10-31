from datetime import datetime
#from controller import loggedIn

class Note:
    def __init__(self, index, description):
        # defines the initialization of a note, and collects the timestamp of when it was called
        self.index = index
        self.description = description
        self.timestamp = datetime.now()

    def __eq__(self, other):
        # defines how equality is judged for instances of note objects
        # returns false if given objects don't exist
        if isinstance(other, Note):
            return self.index == other.index and self.description == other.description
        return False
