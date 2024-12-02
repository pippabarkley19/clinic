from PyQt6.QtWidgets import (
    QWidget, QScrollArea, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QGridLayout, QTableView)
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from clinic.patient import Patient 

from PyQt6.QtCore import Qt

class PatientWindow(QWidget):
    def __init__(self, switch_to_set_window, switch_to_login_window, controller, autosave):
        super().__init__()
        self.switch_to_set_window = switch_to_set_window
        self.switch_to_login_window = switch_to_login_window
        self.controller = controller
        self.autosave = autosave
        # commenting this out for now hoping that the box layout will fix this issue
        #self.setFixedSize(1000,2000)
        self.controller.logged = True

        self.setWindowTitle("Patient Management")

        # Main layout
        layout = QVBoxLayout()

        #Logout button
        logout_layout = QHBoxLayout()
        self.logout_button = QPushButton("Logout")
        self.logout_button.clicked.connect(self.logout)
        logout_layout.addWidget(self.logout_button, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addLayout(logout_layout)

        # fields for create patient
        create_layout = QGridLayout()
        self.phn_input, self.name_input = QLineEdit(), QLineEdit()
        self.birthday_input, self.phone_input = QLineEdit(), QLineEdit()
        self.email_input, self.address_input = QLineEdit(), QLineEdit()
        create_layout.addWidget(QLabel("PHN:"), 0, 0)
        create_layout.addWidget(self.phn_input, 0, 1)
        create_layout.addWidget(QLabel("Name:"), 1, 0)
        create_layout.addWidget(self.name_input, 1, 1)
        create_layout.addWidget(QLabel("Birthday (YYYY-MM-DD):"), 2, 0)
        create_layout.addWidget(self.birthday_input, 2, 1)
        create_layout.addWidget(QLabel("Phone Number:"), 3, 0)
        create_layout.addWidget(self.phone_input, 3, 1)
        create_layout.addWidget(QLabel("Email:"), 4, 0)
        create_layout.addWidget(self.email_input, 4, 1)
        create_layout.addWidget(QLabel("Address:"), 5, 0)
        create_layout.addWidget(self.address_input, 5, 1)
        # Create button
        self.create_button = QPushButton("Create Patient")
        self.create_button.clicked.connect(self.create_patient)
        create_layout.addWidget(self.create_button, 6, 0, 1, 2)
        layout.addLayout(create_layout)

        # Search Patient Section
        search_layout = QGridLayout()
        self.search_input = QLineEdit()
        search_layout.addWidget(QLabel("Search Patient by PHN:"), 0, 0)
        search_layout.addWidget(self.search_input, 0, 1)
        # Search button
        self.search_button = QPushButton("Search Patient")
        self.search_button.clicked.connect(self.search_patient)
        search_layout.addWidget(self.search_button, 0, 2)
        layout.addLayout(search_layout)

        # Retrieve Patient Section
        retrieve_layout = QGridLayout()
        self.retrieve_input = QLineEdit()
        retrieve_layout.addWidget(QLabel("Enter a name to retrieve a patient:"), 0, 0)
        retrieve_layout.addWidget(self.retrieve_input, 0, 1)
        # Retrieve button
        self.retrieve_button = QPushButton("Retrieve Patient")
        self.retrieve_button.clicked.connect(self.retrieve_patient)
        retrieve_layout.addWidget(self.retrieve_button, 0, 2)
        self.retrieve_table = QTableView()
        retrieve_layout.addWidget(self.retrieve_table, 1, 0, 1, 3)
        layout.addLayout(retrieve_layout)

        # Update Patient Section
        update_layout = QGridLayout()
        self.original_phn_input, self.update_phn_input = QLineEdit(), QLineEdit()
        self.update_name_input, self.update_birthday_input = QLineEdit(), QLineEdit()
        self.update_phone_input, self.update_email_input = QLineEdit(), QLineEdit()
        self.update_address_input = QLineEdit()
        update_layout.addWidget(QLabel("Original PHN:"), 0, 0)
        update_layout.addWidget(self.original_phn_input, 0, 1)
        update_layout.addWidget(QLabel("PHN:"), 1, 0)
        update_layout.addWidget(self.update_phn_input, 1, 1)
        update_layout.addWidget(QLabel("Name:"), 2, 0)
        update_layout.addWidget(self.update_name_input, 2, 1)
        update_layout.addWidget(QLabel("Birthday (YYYY-MM-DD):"), 3, 0)
        update_layout.addWidget(self.update_birthday_input, 3, 1)
        update_layout.addWidget(QLabel("Phone:"), 4, 0)
        update_layout.addWidget(self.update_phone_input, 4, 1)
        update_layout.addWidget(QLabel("Email:"), 5, 0)
        update_layout.addWidget(self.update_email_input, 5, 1)
        update_layout.addWidget(QLabel("Address:"), 6, 0)
        update_layout.addWidget(self.update_address_input, 6, 1)
        # Update button
        self.update_button = QPushButton("Update Patient")
        self.update_button.clicked.connect(self.update_patient)
        update_layout.addWidget(self.update_button, 7, 0, 1, 2)
        layout.addLayout(update_layout)

        # Delete Patient Section
        delete_layout = QGridLayout()
        self.delete_phn_input = QLineEdit()
        delete_layout.addWidget(QLabel("PHN:"), 0, 0)
        delete_layout.addWidget(self.delete_phn_input, 0, 1)
        # Delete button
        self.delete_button = QPushButton("Delete Patient")
        self.delete_button.clicked.connect(self.delete_patient)
        delete_layout.addWidget(self.delete_button, 1, 0, 1, 2)
        layout.addLayout(delete_layout)

        # List Patients Section
        # List Button
        self.list_button = QPushButton("List All Patients")
        self.list_button.clicked.connect(self.list_patients)
        layout.addWidget(self.list_button)
        self.patient_table = QTableView()
        self.patient_table.setModel(QStandardItemModel())
        layout.addWidget(self.patient_table)

        # Appointment Button
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
        original_phn = self.original_phn_input.text()
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
            if original_phn:
                self.controller.update_patient(original_phn, phn, name, birthday, phone, email, address)
                QMessageBox.information(self, "Success", f"Patient {name} updated successfully!")
            else:
                QMessageBox.warning(self, "Patient with given PHN does not exist")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        self.clear_update_fields()

    def clear_update_fields(self):
        self.original_phn_input.clear()
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
            QMessageBox.information(self,"Success", "Patient successfully deleted")
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
                model.setItem(row, 2, QStandardItem(patient.birth_date))
                model.setItem(row, 3, QStandardItem(patient.phone))
                model.setItem(row, 4, QStandardItem(patient.email))
                model.setItem(row, 5, QStandardItem(patient.address))

            # Set the model to the table view
            self.patient_table.setModel(model)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def new_appointment(self):
        self.switch_to_set_window()
