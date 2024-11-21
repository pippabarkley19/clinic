
from clinic.patient import Patient
from clinic.patient_record import PatientRecord
from clinic.dao.patient_dao import PatientDAO
from clinic.dao.note_dao_pickle import NoteDAOPickle
#from clinic.note import Note

class PatientDAOJSON(PatientDAO):

	def __init__(self, autosave):
		''' construct a controller class '''
		self.users = {"user" : "123456","ali" : "@G00dPassw0rd"}
		self.username = None
		self.password = None
		self.autosave = autosave 
		self.patients = {}
		self.current_patient = None
		self.note_dao = NoteDAOPickle(self.autosave)

	def search_patient(self, phn):
		''' user searches a patient '''
		return self.patients.get(phn)

	def create_patient(self, phn, name, birth_date, phone, email, address):
		''' user creates a patient '''
		patient = Patient(phn, name, birth_date, phone, email, address, self.autosave)
		self.patients[phn] = patient
		return patient

	def retrieve_patients(self, name):
		''' user retrieves the patients that satisfy a search criterion '''
		retrieved_patients = []
		for patient in self.patients.values():
			if name in patient.name:
				retrieved_patients.append(patient)
		return retrieved_patients

	def update_patient(self, original_phn, phn, name, birth_date, phone, email, address):
		''' user updates a patient '''

		# patient exists, update fields
		patient = self.patients.get(original_phn)
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
		# patient exists, delete patient
		self.patients.pop(phn)
		return True

	def list_patients(self):
		''' user lists all patients '''
		patients_list = []
		for patient in self.patients.values():
			patients_list.append(patient)
		return patients_list



	