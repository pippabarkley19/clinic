from clinic.dao.note_dao import NoteDAO
from clinic.note import Note
import datetime

class NoteDAOPickle(NoteDAO):

	def __init__(self, autosave=False, phn=None):
		''' construct a patient record '''
		self.counter = 0
		self.notes = []
		self.autosave = autosave
		self.phn = phn

	def search_note(self, code):
		''' user searches a note from the current patient's record '''
		# search a new note with the given code and return  it 
		for note in self.notes:
			if note.code == code:
				return note
		return None

	def create_note(self, text):
		''' user creates a note in the current patient's record '''
		# create a new note and return it
		self.counter += 1
		current_time = datetime.datetime.now()
		new_note = Note(self.counter, text, current_time)
		self.notes.append(new_note)
		return new_note

	def retrieve_notes(self, search_string):
		''' user retrieves the notes from the current patient's record
			that satisfy a search string '''
		# create empty list
		retrieved_notes = []
		# for every note in notes check if the search string matches the note description, appent accordingly
		for note in self.notes:
			if search_string in note.text:
				retrieved_notes.append(note)
		return retrieved_notes

	def update_note(self, code, new_text):
		''' user updates a note from the current patient's record '''	
		# update note
		updated_note = None
		# first, search the note by code
		for note in self.notes:
			if note.code == code:
				updated_note = note
				break
		# note does not exist
		if not updated_note:
			return False
		# note exists, update fields
		updated_note.text = new_text
		updated_note.timestamp = datetime.datetime.now()
		return True

	def delete_note(self, code):
		''' user deletes a note from the current patient's record '''
		# delete note
		note_to_delete_index = -1
		# first, search the note by code
		for i in range(len(self.notes)):
			if self.notes[i].code == code:
				note_to_delete_index = i
				break
		# note does not exist
		if note_to_delete_index == -1:
			return False
		# note exists, delete note
		self.notes.pop(note_to_delete_index)
		return True

	def list_notes(self):
		''' user lists all notes from the current patient's record '''
		notes_list = []
		# for every note in the patient record, output it in a new list notes_list
		for i in range(-1, -len(self.notes)-1, -1):
			notes_list.append(self.notes[i])
		return notes_list