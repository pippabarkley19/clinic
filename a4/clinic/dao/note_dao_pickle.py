from clinic.dao.note_dao import NoteDAO
from clinic.note import Note

class NoteDAOPickle(NoteDAO):

	def __init__(self, autosave=False, phn=None):
		''' construct a patient record '''
		self.counter = 0
		self.notes = []
		self.autosave = autosave
		self.phn = phn

	def search_note(self, code):
		''' user searches a note from the current patient's record '''
		# search a new note with the given code and return it 
		return self.current_patient.search_note(code)

	def create_note(self, text):
		''' user creates a note in the current patient's record '''
		# create a new note and return it
		return self.current_patient.create_note(text)

	def retrieve_notes(self, search_string):
		''' user retrieves the notes from the current patient's record
			that satisfy a search string '''
		# return the found notes
		return self.current_patient.retrieve_notes(search_string)

	def update_note(self, code, new_text):
		''' user updates a note from the current patient's record '''	
		# update note
		return self.current_patient.update_note(code, new_text)

	def delete_note(self, code):
		''' user deletes a note from the current patient's record '''
		# delete note
		return self.current_patient.delete_note(code)

	def list_notes(self):
		''' user lists all notes from the current patient's record '''
		return self.current_patient.list_notes()
