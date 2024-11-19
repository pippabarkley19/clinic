
from clinic.patient import Patient
from clinic.patient_record import PatientRecord
from clinic.note import Note
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException

class PatientDAOJSON(PatientDAO):

	def __init__(self, autosave):
		''' construct a controller class '''
		self.users = {"user" : "123456","ali" : "@G00dPassw0rd"}
		self.username = None
		self.password = None
		self.logged = False
		self.autosave = False 
		self.patients = {}
		self.current_patient = None

	def search_patient(self, phn):
		''' user searches a patient '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		return self.patients.get(phn)

	def create_patient(self, phn, name, birth_date, phone, email, address):
		''' user creates a patient '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# patient already exists, do not create them
		if self.patients.get(phn):
			raise IllegalOperationException

		# finally, create a new patient
		patient = Patient(phn, name, birth_date, phone, email, address)
		self.patients[phn] = patient
		return patient

	def retrieve_patients(self, name):
		''' user retrieves the patients that satisfy a search criterion '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		retrieved_patients = []
		for patient in self.patients.values():
			if name in patient.name:
				retrieved_patients.append(patient)
		return retrieved_patients

	def update_patient(self, original_phn, phn, name, birth_date, phone, email, address):
		''' user updates a patient '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# first, search the patient by key
		patient = self.patients.get(original_phn)

		# patient does not exist, cannot update
		if not patient:
			raise IllegalOperationException
		
		# check if the new phn is taken by a different patient
		if phn != original_phn and self.patients.get(phn):
			raise IllegalOperationException
			
		# patient is current patient, cannot update
		if self.current_patient and patient == self.current_patient:
			raise IllegalOperationException

		# patient is current patient, cannot update
		if self.current_patient:
			if patient == self.current_patient:
				raise IllegalOperationException

		# patient exists, update fields
		patient.name = name
		patient.birth_date = birth_date
		patient.phone = phone
		patient.email = email
		patient.address = address

		# treat different keys as a separate case
		if original_phn != phn:
			if self.patients.get(phn):
				return False
			self.patients.pop(original_phn)
			patient.phn = phn
			self.patients[phn] = patient

		return True
			
	def delete_patient(self, phn):
		''' user deletes a patient '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# first, search the patient by key
		patient = self.patients.get(phn)

		# patient does not exist, cannot delete
		if not patient:
			raise IllegalOperationException

		# patient is current patient, cannot delete
		if self.current_patient:
			if patient == self.current_patient:
				raise IllegalOperationException

		# patient exists, delete patient
		self.patients.pop(phn)
		return True

	def list_patients(self):
		''' user lists all patients '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		patients_list = []
		for patient in self.patients.values():
			patients_list.append(patient)
		return patients_list

	def set_current_patient(self, phn):
		''' user sets the current patient '''

		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# first, search the patient by key
		patient = self.patients.get(phn)

		# patient does not exist
		if not patient:
			raise IllegalOperationException

		# patient exists, set them to be the current patient
		self.current_patient = patient


	def get_current_patient(self):
		''' get the current patient '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException
		
		if not isinstance(self.current_patient, Patient):
			return None

		# return current patient
		return self.current_patient

	def unset_current_patient(self):
		''' unset the current patient '''

		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# unset current patient
		self.current_patient = None


