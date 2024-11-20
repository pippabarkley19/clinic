import datetime
from clinic.note import Note
from clinic.dao.note_dao_pickle import NoteDAOPickle
#from clinic.dao.patient_dao_json import PatientDAOJSON

class PatientRecord():
	''' class that represents a patient's medical record '''

	def __init__(self, logged, autosave=False):
		self.logged = logged
		self.autosave = autosave
		self.note_dao = NoteDAOPickle(self.logged, self.autosave)
		#self.patient_dao = PatientDAOJSON()
	
	def search_note(self, code):
		return self.note_dao.search_note(code)

	def create_note(self, text):
		return self.note_dao.create_note(text)

	def retrieve_notes(self, search_string):
		return self.note_dao.retrieve_notes(search_string)

	def update_note(self, code, new_text):
		return self.note_dao.update_note(code, new_text)

	def delete_note(self, code):
		return self.note_dao.delete_note(code)

	def list_notes(self):
		return self.note_dao.list_notes()

	