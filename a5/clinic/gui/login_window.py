from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QGridLayout

class LoginWindow(QWidget):
    def __init__(self, controller, switch_to_patient_window):
        super().__init__()
        self.setWindowTitle("Login")
        self.controller = controller
        self.setFixedSize(1000, 1000)
        self.switch_to_patient_window = switch_to_patient_window

        layout = QVBoxLayout()

        login_layout = QGridLayout()
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)  # Obscure password
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)
        login_layout.addWidget(self.username_label)
        login_layout.addWidget(self.username_input)
        login_layout.addWidget(self.password_label)
        login_layout.addWidget(self.password_input)
        login_layout.addWidget(self.login_button)

        layout.addLayout(login_layout)

    def handle_login(self):
        
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        try:
            users = self.controller.load_users()
            if username in users:
                hashed_password = self.controller.get_password_hash(password)
                if users[username] == hashed_password:
                    self.switch_to_patient_window()
                    self.controller.logged = True
                else:
                    QMessageBox.warning(self, "Login failed", "Invalid Password")
            else:
                QMessageBox.warning(self, "Login failed", "Username not found")
        except Exception as e:
            QMessageBox.critical(self, "login failed", str(e))
        self.username_input.clear()
        self.password_input.clear()
