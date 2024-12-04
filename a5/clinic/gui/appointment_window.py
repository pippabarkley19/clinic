from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QPlainTextEdit
from PyQt6.QtCore import Qt

class AppointmentWindow(QWidget):
    def __init__(self, switch_to_set_window, controller):
        super().__init__()

        self.switch_to_set_window = switch_to_set_window
        self.controller = controller
        self.setWindowTitle("Appointment Management")

        # Main layout
        layout = QVBoxLayout()

        # who is the current patient
        #self.current_patient_label = QLabel(f"Current patient is: {self.current_patient.name} ")
        #end appt content
        end_appt_layout = QHBoxLayout()
        self.back_button = QPushButton("End Appointment")
        self.back_button.clicked.connect(self.end_appointment)
        end_appt_layout.addWidget(self.back_button, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.back_button)

        #create note content
        self.create_label = QLabel("Create Note")
        self.note_input_label = QLabel("Enter note text:")
        self.note_input = QLineEdit()
        self.create_note_button = QPushButton("Create Note")
        self.create_note_button.clicked.connect(self.create_note)
        layout.addWidget(self.create_label)
        layout.addWidget(self.note_input_label)
        layout.addWidget(self.note_input)
        layout.addWidget(self.create_note_button)

        #retrieve notes content
        self.ret_label = QLabel("Retrieve Note")
        self.text_input_label = QLabel("Enter note text:")
        self.text_input = QLineEdit()
        self.ret_note_button = QPushButton("Retrieve Note")
        self.ret_note_button.clicked.connect(self.retrieve_note)
        layout.addWidget(self.ret_label)
        layout.addWidget(self.text_input_label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.ret_note_button)
         # PlainTextEdit for displaying patient details
        self.note_display = QPlainTextEdit()
        self.note_display.setReadOnly(True) # not sure if this is necessary 
        layout.addWidget(self.note_display)

        # update note content
        self.update_label = QLabel("Update Note")
        self.note_key_label = QLabel("Note Key:")
        self.note_key_input = QLineEdit()
        self.new_text_label = QLabel("New text:")
        self.new_text_input = QLineEdit()
        self.update_button = QPushButton("Update Note")
        layout.addWidget(self.update_label)
        layout.addWidget(self.note_key_label)
        layout.addWidget(self.note_key_input)
        layout.addWidget(self.new_text_label)
        layout.addWidget(self.new_text_input)
        layout.addWidget(self.update_button)
        self.update_button.clicked.connect(self.update_note)

        # delete note content
        self.delete_label = QLabel("Delete Note")
        self.note_index_label = QLabel("Note index:")
        self.note_index_input = QLineEdit()
        self.delete_button = QPushButton("Delete Note")
        layout.addWidget(self.delete_label)
        layout.addWidget(self.note_index_label)
        layout.addWidget(self.note_index_input)
        layout.addWidget(self.delete_button)
        self.delete_button.clicked.connect(self.delete_note)

        # list full patient record content
        self.notes_display = QPlainTextEdit(self)
        self.notes_display.setReadOnly(True)  
        self.list_notes_button = QPushButton("List All Notes", self)
        layout.addWidget(self.notes_display)
        layout.addWidget(self.list_notes_button)
        self.list_notes_button.clicked.connect(self.list_all_notes)

        self.setLayout(layout)

    def end_appointment(self):
        self.controller.unset_current_patient()
        self.switch_to_set_window()
    
    def create_note(self):
        text = self.note_input.text()

        if not text:
            QMessageBox.warning(self,"Error", "The note cannot be empty")
            return
        try:
            self.controller.create_note(text)
            QMessageBox.information(self, "Success", "Note Created")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        self.note_input.clear()

    def retrieve_note(self):
        #self.note_display.clear()
        text = self.text_input.text()

        if not text:
            QMessageBox.warning(self, "Input Error", "Text cannot be empty")
            return

        try:
            matching_notes = self.controller.retrieve_notes(text)

            if not matching_notes:
                QMessageBox.information(self, "No Results", "No notes match the search string.")
                return
            result_text = ""
            for index, note in enumerate(matching_notes):
                result_text += (
                f"Index: {index}\n"
                f"Description: {note.text}\n"
                f"Date: {note.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            )
        
            self.note_display.setPlainText(result_text)

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        self.text_input.clear()

    def update_note(self):
        index = self.note_key_input.text()
        new_text = self.new_text_input.text()

        if not all([index, new_text]):
            QMessageBox.warning(self, "Input Error", "Must fill out all fields")
            return
        
        try:
            self.controller.update_note(index, new_text)
            QMessageBox.information(self, "Success", "Succesfully updated the note")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
        self.note_key_input.clear()

    def delete_note(self):
        index = self.note_index_input.text()

        if not index:
            QMessageBox.warning(self, "Input Error", "Missing index")
            return
        
        try:
            self.controller.delete_note(int(index))
            self.refresh_notes()
            QMessageBox.information(self, "Success", "Note successfully deleted")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
        self.note_index_input.clear()

    def refresh_notes(self):
        self.note_display.clear()
        self.notes_display.clear()

        updated_notes = self.controller.list_notes()

        if updated_notes:
            formatted_notes = ""
            for index, note in enumerate(updated_notes):
                formatted_notes += (
                    f"Index: {index}\n"
                    f"Description: {note.text}\n"
                    f"Date: {note.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                )
            self.notes_display.setPlainText(formatted_notes)
        else:
            self.notes_display.setPlainText("No notes available.")

    def list_all_notes(self):
        #self.notes_display.clear()
        try:
            notes = self.controller.list_notes()
            if not notes:
                self.notes_display.setPlainText("No notes available.")
                return
            formatted_notes = ""
            for index, note in enumerate(notes):
                formatted_notes += (
                    f"Index: {index}\n"
                    f"Description: {note.text}\n"
                    f"Date: {note.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                )
            self.notes_display.setPlainText(formatted_notes)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
