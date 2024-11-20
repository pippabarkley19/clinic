from clinic.patient import Patient
from clinic.note import Note
from clinic.dao.patient_dao_json import PatientDAOJSON
from clinic.dao.note_dao_pickle import NoteDAOPickle


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
		self.logged = False
		self.patient_dao = PatientDAOJSON(self.logged, self.autosave)
		self.note_dao = NoteDAOPickle(self.logged, self.autosave)
		self.users = {"user" : "123456","ali" : "@G00dPassw0rd"}
		self.username = None
		self.password = None
	
	def login(self, username, password):
		''' user logs in the system '''
		if self.logged:
			raise DuplicateLoginException
		if username in self.users:
			if password == self.users[username]:
				self.username = username
				self.password = password
				self.logged = True
				self.patient_dao.logged = True  # Update DAO logged state
				self.note_dao.logged = True  # Update DAO logged state
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
			self.patient_dao.logged = False  # Update DAO logged state
			self.note_dao.logged = False  # Update DAO logged state
			return True

	def search_patient(self, phn):
		try:
			return self.patient_dao.search_patient(phn)
		except IllegalAccessException as e:
			pass


	def create_patient(self, phn, name, birth_date, phone, email, address):
		try:
			return self.patient_dao.create_patient(phn, name, birth_date, phone, email, address)
		except IllegalAccessException as e:
			pass
		except IllegalOperationException as e:
			pass

	def retrieve_patients(self, name):
		try:
			return self.patient_dao.retrieve_patients(name)
		except IllegalAccessException as e:
			pass

	def update_patient(self, original_phn, phn, name, birth_date, phone, email, address):
		try: 
			return self.patient_dao.update_patient(original_phn, phn, name, birth_date, phone, email, address)
		except IllegalAccessException as e:
			pass
		except IllegalOperationException as e:
			pass
			
	def delete_patient(self, phn):
		try:
			return self.patient_dao.delete_patient(phn)
		except IllegalOperationException as e:
			pass
		except IllegalAccessException as e:
			pass

	def list_patients(self):
		try: 
			return self.patient_dao.list_patients()
		except IllegalAccessException as e:
			pass

	def set_current_patient(self, phn):
		try:
			return self.patient_dao.set_current_patient(phn)
		except IllegalAccessException as e:
			pass
		except IllegalOperationException as e:
			pass

	def get_current_patient(self):
		try:
			return self.patient_dao.get_current_patient()
		except IllegalAccessException as e:
			pass

	def unset_current_patient(self):
		try:
			return self.patient_dao.unset_current_patient()
		except IllegalAccessException as e:
			pass

	def search_note(self, code):
		try:
			return self.note_dao.search_note(code)
		except IllegalAccessException as e:
			pass
		except NoCurrentPatientException as e:
			pass

	def create_note(self, text):
		try: 
			return self.note_dao.create_note(text)
		except IllegalAccessException as e:
			pass
		except NoCurrentPatientException as e:
			pass

	def retrieve_notes(self, search_string):
		try:
			return self.note_dao.retrieve_notes(search_string)
		except IllegalAccessException as e:
			pass
		except NoCurrentPatientException as e:
			pass

	def update_note(self, code, new_text):
		try:
			return self.note_dao.update_note(code, new_text)
		except IllegalAccessException as e:
			pass
		except NoCurrentPatientException as e:
			pass

	def delete_note(self, code):
		try:
			return self.note_dao.delete_note(code)
		except IllegalAccessException as e:
			pass
		except NoCurrentPatientException as e:
			pass

	def list_notes(self):
		try: 
			return self.note_dao.list_notes()
		except IllegalAccessException as e:
			pass
		except NoCurrentPatientException as e:
			pass
