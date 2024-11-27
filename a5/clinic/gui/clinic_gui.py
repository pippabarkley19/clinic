import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QScrollArea, QVBoxLayout, QWidget

from clinic.controller import Controller  # Assuming this is where your Controller class is
from clinic.gui.login_window import LoginWindow
from clinic.gui.patient_window import PatientWindow
from clinic.gui.appointment_window import AppointmentWindow

class ClinicGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.controller = Controller()

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.login_window = LoginWindow(self.controller, self.show_patient_window)
        self.patient_window = PatientWindow(self.show_appointment_window, self.show_login_window, self.controller)
        self.appointment_window = AppointmentWindow(self.show_patient_window, self.controller)


        self.central_widget.addWidget(self.login_window)
        self.central_widget.addWidget(self.patient_window)
        self.central_widget.addWidget(self.appointment_window)

        self.central_widget.setCurrentWidget(self.login_window)

        self.setWindowTitle("Clinic System")

    def show_patient_window(self):
        self.central_widget.setCurrentWidget(self.patient_window)

    def show_appointment_window(self):
        self.central_widget.setCurrentWidget(self.appointment_window)

    def show_login_window(self):
        self.central_widget.setCurrentWidget(self.login_window)


def main():
    app = QApplication(sys.argv)
    window = ClinicGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
