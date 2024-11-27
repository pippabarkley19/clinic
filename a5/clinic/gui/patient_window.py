from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QTableView, QStandardItem, QStandardItemModel)
from clinic.patient import Patient 

from PyQt6.QtCore import Qt

class PatientWindow(QWidget):
    def __init__(self, switch_to_appointment_window, switch_to_login_window, controller):
        super().__init__
        self.switch_to_appointment_window = switch_to_appointment_window
        self.switch_to_login_window = switch_to_login_window
        self.controller = controller

        self.setWindowTitle("Patient Management")

        # Main layout
        layout = QVBoxLayout()

        #logout button
        logout_layout = QHBoxLayout()
        self.logout_button = QPushButton("Logout")
        self.logout_button.clicked.connect(self.logout)
        logout_layout.addWidget(self.logout_button, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addLayout(logout_layout)

        # fields for create patient
        self.phn_label = QLabel("PHN:")
        self.phn_input = QLineEdit()
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.birthday_label = QLabel("Birthday (YYYY-MM-DD):")
        self.birthday_input = QLineEdit()
        self.phone_label = QLabel("Phone Number:")
        self.phone_input = QLineEdit()
        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        self.address_label = QLabel("Address:")
        self.address_input = QLineEdit()

      # add create patient widgets to layout
        layout.addWidget(self.phn_label)
        layout.addWidget(self.phn_input)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.birthday_label)
        layout.addWidget(self.birthday_input)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)
        # add create patient button
        self.create_button = QPushButton("Create Patient")
        self.create_button.clicked.connect(self.create_patient)
        layout.addWidget(self.create_button)

        # search patient fields
        self.search_label = QLabel("Search Patient by PHN:")
        self.search_input = QLineEdit()
        #search patient button
        self.search_button = QPushButton("Search Patient")
        self.search_button.clicked.connect(self.search_patient)
        # add search patient widgets
        layout.addWidget(self.search_label)
        layout.addWidget(self.search_input)
        layout.addWidget(self.search_button)

        self.retrieve_label = QLabel("Enter a PHN to retreive a patient")
        self.retrieve_input = QLineEdit()
        self.retreive_button = QPushButton("Retreive a patient")
        self.retreive_button.clicked.connect(self.retrieve_patient)
        layout.addWidget(self.retrieve_label)
        layout.addWidget(self.retrieve_input)
        layout.addWidget(self.retreive_button)

        # table for retrieve 
        self.retrieve_table = QTableView()
        self.retrieve_table.setModel(QStandardItemModel())
        layout.addWidget(self.retrieve_table)

        # update patient
        self.update_phn_input = QLineEdit()
        self.update_name_label = QLabel("Name:")
        self.update_name_input = QLineEdit()
        self.update_birthday_label = QLabel("Birthday (YYYY-MM-DD):")
        self.update_birthday_input = QLineEdit()
        self.update_phone_label = QLabel("Phone Number:")
        self.update_phone_input = QLineEdit()
        self.update_email_label = QLabel("Email:")
        self.update_email_input = QLineEdit()
        self.update_address_label = QLabel("Address:")
        self.update_address_input = QLineEdit()
        # add create patient widgets to layout
        layout.addWidget(self.update_phn_label)
        layout.addWidget(self.update_phn_input)
        layout.addWidget(self.update_name_label)
        layout.addWidget(self.update_name_input)
        layout.addWidget(self.update_birthday_label)
        layout.addWidget(self.update_birthday_input)
        layout.addWidget(self.update_phone_label)
        layout.addWidget(self.update_phone_input)
        layout.addWidget(self.update_email_label)
        layout.addWidget(self.update_email_input)
        layout.addWidget(self.update_address_label)
        layout.addWidget(self.update_address_input)
        # add create patient button
        self.update_button = QPushButton("Update Patient")
        self.update_button.clicked.connect(self.update_patient)
        layout.addWidget(self.update_button)

        #delete patient content
        self.delete_label = QLabel("Delete Patient")
        self.delete_phn_label = QLabel("PHN:")
        self.delete_phn_input = QLineEdit()
        layout.addWidget(self.delete_label)
        layout.addWidget(self.delete_phn_label)
        layout.addWidget(self.delete_phn_input)
        self.delete_button = QPushButton("Delete Patient")
        self.delete_button.clicked.connect(self.delete_patient)
        layout.addWidget(self.delete_button)

        # list all patients content
        self.list_button = QPushButton("List All Patients")
        self.list_button.clicked.connect(self.list_patients)
        layout.addWidget(self.list_button)

        # QTableView for listing patients
        self.patient_table = QTableView()
        self.patient_table.setModel(QStandardItemModel())  # Empty model initially
        layout.addWidget(self.patient_table)

        # appointment window
        self.appointment_button = QPushButton("Create Appointment")
        self.appointment_button.clicked.connect(self.new_appointment)
        layout.addWidget(self.appointment_button)

        self.setLayout(layout)
    
    def logout(self):
        self.controller.logout()
        self.switch_to_login_window()
    

    def create_patient(self):
        # Collect inputs
        phn = self.phn_input.text()
        name = self.name_input.text()
        birthday = self.birthday_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        address = self.address_input.text()

        if not all([phn, name, birthday, phone, email, address]):
            QMessageBox.warning(self, "Input Error", "All fields must be filled!")
            return

        try:
            self.controller.create_patient(phn, name, birthday, phone, email, address)
            QMessageBox.information(self, "Success", f"Patient {name} created successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        self.clear_create_fields()

    def clear_create_fields(self):
        """Clear all input fields."""
        self.phn_input.clear()
        self.name_input.clear()
        self.birthday_input.clear()
        self.phone_input.clear()
        self.email_input.clear()
        self.address_input.clear()

    def search_patient(self):
        phn = self.search_input.text()

        if not phn:
            QMessageBox.warning(self, "Input Error", "PHN must be filled")
            return
        try:
            patient = self.controller.search_patient(phn)
            if patient:
                QMessageBox.information(
                    self,
                    "Patient Found",
                    f"Patient Details:\nPHN: {patient.phn}\n"
                    f"Name: {patient.name}")
            else:
                QMessageBox.warning(self, "Not Found", "No patient found with the given PHN.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        self.search_input.clear()

    def retrieve_patient(self):
        name = self.retrieve_input.text()
        patients = self.controller.retrieve_patients(name)

        if not name:
            QMessageBox.warning(self, "Input Error", "name must be filled!")
            return

        """Populate the QTableView with the retrieved patient data."""
        model = QStandardItemModel(len(patients), 6)  # 1 row, 6 columns for patient details
        model.setHorizontalHeaderLabels(["PHN", "Name", "Birthday", "Phone", "Email", "Address"])

        if patients: 
            for row, patient in enumerate(patients):
                model.setItem(row, 0, QStandardItem(str(patient.phn)))  # Use 'patient.phn'
                model.setItem(row, 1, QStandardItem(str(patient.name)))  # Use 'patient.name'
                model.setItem(row, 2, QStandardItem(str(patient.birth_date)))  # Use 'patient.birthday'
                model.setItem(row, 3, QStandardItem(str(patient.phone)))  # Use 'patient.phone'
                model.setItem(row, 4, QStandardItem(str(patient.email)))  # Use 'patient.email'
                model.setItem(row, 5, QStandardItem(str(patient.address))) #Use 'patient.address' 
        else:
            QMessageBox.warning(self, "Not Found", "No patient found with the given name.")
        self.retrieve_table.setModel(model)

    def update_patient(self):
        original_phn = self.original_phn.text()
        original_patient = self.controller.search_patient(original_phn)
        phn = self.update_phn_input.text()
        name = self.update_name_input.text()
        birthday = self.update_birthday_input.text()
        phone = self.update_phone_input.text()
        email = self.update_email_input.text()
        address = self.update_address_input.text()

        if not all([phn, name, birthday, phone, email, address]):
            QMessageBox.warning(self, "Input Error", "All fields must be filled!")
            return

        try:
            if original_patient:
                self.controller.update_patient(original_patient, phn, name, birthday, phone, email, address)
                QMessageBox.information(self, "Success", f"Patient {name} updated successfully!")
            else:
                QMessageBox.warning(self, "Patient with given PHN does not exist")
            self.clear_update_fields()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def clear_update_fields(self):
        self.update_phn_input.clear()
        self.update_name_input.clear()
        self.update_birthday_input.clear()
        self.update_phone_input.clear()
        self.update_email_input.clear()
        self.update_address_input.clear()

    def delete_patient(self):
        phn = self.delete_phn_input.text()
        if not phn:
            QMessageBox.warning(self, "Input Error", "PHN must be filled")
            return
        try:
            self.controller.delete_patient(phn)
            QMessageBox.information(self, "Patient successfully deleted")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        self.delete_phn_input.clear()

    def list_patients(self):
        try:
            patients = self.controller.list_patients()
            if not patients:
                QMessageBox.information(self, "No Patients", "There are no patients in the system.")
                return

            # Create a model for the table
            model = QStandardItemModel(len(patients), 6)  # Rows = number of patients, Columns = number of fields
            model.setHorizontalHeaderLabels(["PHN", "Name", "Birthday", "Phone", "Email", "Address"])

            # Populate the model with patient data
            for row, patient in enumerate(patients):
                model.setItem(row, 0, QStandardItem(patient.phn))
                model.setItem(row, 1, QStandardItem(patient.name))
                model.setItem(row, 2, QStandardItem(patient.birthday))
                model.setItem(row, 3, QStandardItem(patient.phone))
                model.setItem(row, 4, QStandardItem(patient.email))
                model.setItem(row, 5, QStandardItem(patient.address))

            # Set the model to the table view
            self.patient_table.setModel(model)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def new_appointment(self):
        self.switch_to_appointment_window()
