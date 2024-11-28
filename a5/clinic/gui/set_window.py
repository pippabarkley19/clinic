from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QPlainTextEdit
from PyQt6.QtCore import Qt
from clinic.controller import Controller

class SetWindow(QWidget):
    def __init__(self, switch_to_patient_window, switch_to_appointment_window, controller):
        super().__init__()
        self.setWindowTitle("Set Current Patient")
        self.controller = controller
        self.switch_to_patient_window = switch_to_patient_window
        self.switch_to_appointment_window = switch_to_appointment_window

        layout = QVBoxLayout()

        self.return_to_patient_window_button = QPushButton("Back")
        layout.addWidget(self.return_to_patient_window_button)
        self.return_to_patient_window_button.clicked.connect(self.back_button)
        self.phn_input_label = QLabel("Enter patient PHN")
        self.phn_input = QLineEdit()
        self.phn_input_button = QPushButton("Start Appointment")
        self.phn_input_button.clicked.connect(self.enter_button)
        layout.addWidget(self.phn_input_label)
        layout.addWidget(self.phn_input)
        layout.addWidget(self.phn_input_button)
    
    def back_button(self):
        self.switch_to_patient_window()

    def enter_button(self):
        phn = self.phn_input.text()
        if not phn:
            QMessageBox.warning(self, "Error", "Enter a PHN")
            return
        
        patient = self.controller.search_patient(phn)
        self.controller.set_current_patient(patient)
        self.switch_to_appointment_window()