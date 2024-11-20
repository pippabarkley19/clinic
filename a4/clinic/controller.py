from clinic.patient import Patient
from clinic.note import Note
from clinic.dao.patient_dao_json import PatientDAOJSON
#from clinic.dao.note_dao_pickle import NoteDAOPickle


from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.no_current_patient_exception import NoCurrentPatientException

class Controller():
	''' controller class that receives the system's operations '''

	def __init__(self, autosave=False):
		self.autosave = autosave 
		self.patient_dao = PatientDAOJSON(autosave=False)
		#self.note_dao = NoteDAOPickle()
		self.users = {"user" : "123456","ali" : "@G00dPassw0rd"}
		self.username = None
		self.password = None
		self.logged = False
	
	def login(self, username, password):
		''' user logs in the system '''
		if self.logged:
			raise DuplicateLoginException
		if username in self.users:
			if password == self.users[username]:
				self.username = username
				self.password = password
				self.logged = True
				return True
			else:
				raise InvalidLoginException
		else:
			raise InvalidLoginException

	def logout(self):
		''' user logs out from the system '''
		if not self.logged:
			raise InvalidLogoutException
		else:
			self.username = None
			self.password = None
			self.logged = False
			self.current_patient = None
			return True

	def search_patient(self, phn):
		self.patient_dao.search_patient(phn)

	def create_patient(self, phn, name, birth_date, phone, email, address):
		self.patient_dao.create_patient(phn, name, birth_date, phone, email, address)

	def retrieve_patients(self, name):
		self.patient_dao.retrieve_patients(name)

	def update_patient(self, original_phn, phn, name, birth_date, phone, email, address):
		return self.patient_dao.update_patient(original_phn, phn, name, birth_date, phone, email, address)
			
	def delete_patient(self, phn):
		return self.patient_dao.delete_patient(phn)

	def list_patients(self):
		return self.patient_dao.list_patients()

	def set_current_patient(self, phn):
		self.patient_dao.set_current_patient(phn)

	def get_current_patient(self):
		return self.patient_dao.get_current_patient()

	def unset_current_patient(self):
		self.patient_dao.unset_current_patient()

	def search_note(self, code):
		return self.patient_dao.search_note(code)

	def create_note(self, text):
		return self.patient_dao.create_note(text)

	def retrieve_notes(self, search_string):
		return self.patient_dao.retrieve_notes(search_string)

	def update_note(self, code, new_text):
		return self.patient_dao.update_note(code, new_text)

	def delete_note(self, code):
		return self.patient_dao.delete_note(code)

	def list_notes(self):
		return self.patient_dao.list_notes()
