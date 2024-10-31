from datetime import datetime
#from controller import loggedIn

class Note:
    def __init__(self, index, description):
        self.index = index
        self.description = description
        self.timestamp = datetime.now()

    def __eq__(self, other):
        if isinstance(other, Note):
            return self.index == other.index and self.description == other.description
        return False


        