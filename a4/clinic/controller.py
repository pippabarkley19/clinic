from clinic.patient import Patient
from clinic.dao.patient_dao_json import PatientDAOJSON

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
		# crucially creates the link to the PatientDAOJSON object to allow self.patient_dao to transfer control to DAO
		self.patient_dao = PatientDAOJSON(self.autosave)
		self.users = {"user" : "123456","ali" : "@G00dPassw0rd"}
		self.username = None
		self.password = None
		# current patient is initialized here and set/get/unset methods are in controller too
		self.current_patient = None
	
	def login(self, username, password):
		''' user logs in the system '''
		# no changes to this method from A3
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
		# no changes to this method from A3
		if not self.logged:
			raise InvalidLogoutException
		else:
			self.username = None
			self.password = None
			self.logged = False
			self.current_patient = None
			return True

	def search_patient(self, phn):
		# all methods from here forward will check exception conditions and throw them accordingly
		# if the exceptions are not thrown, return the call passing control to DAO
		if not self.logged:
			raise IllegalAccessException
		return self.patient_dao.search_patient(phn)


	def create_patient(self, phn, name, birth_date, phone, email, address):
		if not self.logged:
			raise IllegalAccessException
		if self.search_patient(phn):
			raise IllegalOperationException
		return self.patient_dao.create_patient(phn, name, birth_date, phone, email, address)

	def retrieve_patients(self, name):
		if not self.logged:
			raise IllegalAccessException
		return self.patient_dao.retrieve_patients(name)

	def update_patient(self, original_phn, phn, name, birth_date, phone, email, address):
		patient = self.search_patient(original_phn)
		if not patient:
			raise IllegalOperationException
		if phn != original_phn and self.search_patient(phn):
			raise IllegalOperationException
		if self.current_patient and patient == self.current_patient:
			raise IllegalOperationException
		if self.current_patient:
			if patient == self.current_patient:
				raise IllegalOperationException
		return self.patient_dao.update_patient(original_phn, phn, name, birth_date, phone, email, address)

	def delete_patient(self, phn):
		if not self.logged:
			raise IllegalAccessException
		if not self.search_patient(phn):
			raise IllegalOperationException
		if self.current_patient:
			if self.search_patient(phn) == self.current_patient:
				raise IllegalOperationException
		return self.patient_dao.delete_patient(phn)

	def list_patients(self):
		if not self.logged:
			raise IllegalAccessException
		return self.patient_dao.list_patients()

	def set_current_patient(self, phn):
		if not self.logged:
			raise IllegalAccessException
		if not self.search_patient(phn):
			raise IllegalOperationException
		patient = self.search_patient(phn)

		self.current_patient = patient
	
	def get_current_patient(self):
		if not self.logged:
			raise IllegalAccessException
		if not isinstance(self.current_patient, Patient):
			return None
		return self.current_patient

	def unset_current_patient(self):
		''' unset the current patient '''
		if not self.logged:
			raise IllegalAccessException
		self.current_patient = None
		self.current_patient = None

	def search_note(self, code):
		if not self.logged:
			raise IllegalAccessException
		if not self.current_patient:
			raise NoCurrentPatientException
		# crucial: all note methods pass current_patient.get_patient_record() to the call to note methods in order to pass current_patient
		return self.current_patient.get_patient_record().search_note(code)

	def create_note(self, text):
		if not self.logged:
			raise IllegalAccessException
		if not self.current_patient:
			raise NoCurrentPatientException
		return self.current_patient.get_patient_record().create_note(text)
		

	def retrieve_notes(self, search_string):
		if not self.logged:
			raise IllegalAccessException
		if not self.current_patient:
			raise NoCurrentPatientException
		return self.current_patient.get_patient_record().retrieve_notes(search_string)
		

	def update_note(self, code, new_text):
		if not self.logged:
			raise IllegalAccessException
		if not self.current_patient:
			raise NoCurrentPatientException
		return self.current_patient.get_patient_record().update_note(code, new_text)

	def delete_note(self, code):
		if not self.logged:
			raise IllegalAccessException
		if not self.current_patient:
			raise NoCurrentPatientException
		return self.current_patient.get_patient_record().delete_note(code)
		

	def list_notes(self):
		if not self.logged:
			raise IllegalAccessException
		if not self.current_patient:
			raise NoCurrentPatientException
		return self.current_patient.get_patient_record().list_notes()
