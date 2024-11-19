from clinic.dao.note_dao import NoteDAO
from clinic.note import Note
class NoteDAOPickle(NoteDAO):

	def __init__(self):
		''' construct a patient record '''
		self.counter = 0
		self.notes = []

	def search_note(self, code):
		''' user searches a note from the current patient's record '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# there must be a valid current patient
		if not self.current_patient:
			raise NoCurrentPatientException

		# search a new note with the given code and return it 
		return self.current_patient.search_note(code)

	def create_note(self, text):
		''' user creates a note in the current patient's record '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# there must be a valid current patient
		if not self.current_patient:
			raise NoCurrentPatientException

		# create a new note and return it
		return self.current_patient.create_note(text)

	def retrieve_notes(self, search_string):
		''' user retrieves the notes from the current patient's record
			that satisfy a search string '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# there must be a valid current patient
		if not self.current_patient:
			raise NoCurrentPatientException

		# return the found notes
		return self.current_patient.retrieve_notes(search_string)

	def update_note(self, code, new_text):
		''' user updates a note from the current patient's record '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# there must be a valid current patient
		if not self.current_patient:
			raise NoCurrentPatientException

		# update note
		return self.current_patient.update_note(code, new_text)

	def delete_note(self, code):
		''' user deletes a note from the current patient's record '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# there must be a valid current patient
		if not self.current_patient:
			raise NoCurrentPatientException

		# delete note
		return self.current_patient.delete_note(code)

	def list_notes(self):
		''' user lists all notes from the current patient's record '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# there must be a valid current patient
		if not self.current_patient:
			raise NoCurrentPatientException

		return self.current_patient.list_notes()
