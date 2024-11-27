from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QPlainTextEdit
from PyQt6.QtCore import Qt

class AppointmentWindow(QWidget):
    def __init__(self, switch_to_patient_window, controller):
        super().__init__()

        self.switch_to_patient_window = switch_to_patient_window
        self.controller = controller
        self.current_patient = None

        self.setWindowTitle("Appointment Management")

        # Main layout
        layout = QVBoxLayout()

        #end appt content
        end_appt_layout = QHBoxLayout()
        self.back_button = QPushButton("End Appointment")
        self.back_button.clicked.connect(self.end_appointment)
        end_appt_layout.addWidget(self.back_button, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.back_button)

        # set current patient content
        self.set_patient_label = QLabel("Enter a PHN to begin the appointment")
        self.set_patient_phn_label = QLabel("PHN:")
        self.set_patient_phn_input = QLineEdit()
        self.enter_phn_button = QPushButton("Start appointment")
        self.enter_phn_button.clicked.connect(self.start_appointment)
        layout.addWidget(self.set_patient_label)
        layout.addWidget(self.set_patient_phn_label)
        layout.addWidget(self.set_patient_phn_input)
        layout.addWidget(self.enter_phn_button)

        #create note content
        self.create_label = QLabel("Create Note")
        self.note_input_label = QLabel("Enter note text:")
        self.note_input = QLineEdit()
        self.create_note_button = QPushButton()
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
        self.patient_details_display = QPlainTextEdit()
        self.patient_details_display.setReadOnly(True) # not sure if this is necessary 
        layout.addWidget(self.patient_details_display)

        # update note content
        # delete note content
        # list full patient record content

        self.setLayout(layout)
    
    def start_appointment(self):
        phn = self.set_patient_phn_input.text()

        if not phn:
            QMessageBox.warning(self, "Input Error", "PHN must be filled")
            return
        
        patient = self.controller.search_patient(phn)

        if not patient:
            QMessageBox.warning(self, "Input Error", "Patient does not exist. End the appointment, create the patient, then come back to start an appointment.")
            return
        
        try:
            self.controler.set_current_patient(phn)
            self.current_patient = patient
            QMessageBox.information(self, "Appointment started")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        self.set_patient_phn_input.clear()

    def end_appointment(self):
        self.current_patient = None
        self.switch_to_patient_window()
    
    def create_note(self):
        text = self.note_input.text()

        if not text:
            QMessageBox.warning(self, "The note cannot be empty")
            return
        if self.current_patient == None:
            QMessageBox.warning(self, "Set the current patient to perform any appointment actions")
        try:
            self.controller.create_note(text)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def retrieve_note(self):
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
