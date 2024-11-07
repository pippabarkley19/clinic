from abc import ABC, abstractmethod

class PatientDAO(ABC):
    @abstractmethod
    def login(self, username, password):
        ''' user logs in the system '''
        pass
    @abstractmethod
    def logout(self):
        ''' user logs out from the system '''
        pass
	
    @abstractmethod
    def search_patient(self, phn):
        ''' user searches a patient '''
        pass
	
    @abstractmethod
    def create_patient(self, phn, name, birth_date, phone, email, address):
        ''' user creates a patient '''
        pass
    @abstractmethod
    def retrieve_patients(self, name):
        ''' user retrieves the patients that satisfy a search criterion '''
        pass

    @abstractmethod
    def update_patient(self, original_phn, phn, name, birth_date, phone, email, address):
        ''' user updates a patient '''
        pass

    @abstractmethod	
    def delete_patient(self, phn):
        ''' user deletes a patient '''
        pass

    @abstractmethod
    def list_patients(self):
        ''' user lists all patients '''
        pass
    
    @abstractmethod
    def set_current_patient(self, phn):
        ''' user sets the current patient '''
        pass

    @abstractmethod
    def get_current_patient(self):
        ''' get the current patient '''
        pass

    @abstractmethod
    def unset_current_patient(self):
        ''' unset the current patient '''
        pass

    @abstractmethod
    def search_note(self, code):
        ''' user searches a note from the current patient's record '''
        pass

    @abstractmethod
    def create_note(self, text):
        ''' user creates a note in the current patient's record '''
        pass
    @abstractmethod
    def retrieve_notes(self, search_string):
        ''' user retrieves the notes from the current patient's record
			that satisfy a search string '''
        pass
    @abstractmethod
    def update_note(self, code, new_text):
        ''' user updates a note from the current patient's record '''
        pass
    @abstractmethod
    def delete_note(self, code):
        ''' user deletes a note from the current patient's record '''
        pass

    @abstractmethod
    def list_notes(self):
        ''' user lists all notes from the current patient's record '''
        pass
