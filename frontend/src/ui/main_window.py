import sys
import PyQt5.QtWidgets
from PyQt5.QtGui import QFont, QIcon, QPixmap, QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
    QHBoxLayout, QFileDialog, \
    QCheckBox, QStackedWidget
from PyQt5.QtCore import Qt, QDateTime
from ui.welcome import WelcomePage
from ui.history import HistoryPage
from ui.login import LoginWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome")
        self.resize(900, 600)
        self.center()

        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-family: Arial;
            }
            QLineEdit {
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            QPushButton {
                padding: 10px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLabel#error_label {
                color: red;
                font-size: 12px;
            }
        """)
        self.central_widget = QWidget()
        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)

        # MARK: User Info
        logout_layout = QHBoxLayout()
        logout_layout.addStretch(1)

        self.user_info_label = QLabel()
        self.user_info_label.setFont(QFont('Arial', 13))
        logout_layout.addWidget(self.user_info_label)

        self.logout_button = QPushButton("Logout")
        self.logout_button.clicked.connect(self.switch_to_login_window)
        logout_layout.addWidget(self.logout_button)
        layout.addLayout(logout_layout)

        self.stacked_widget = QStackedWidget()
        self.welcome_page = WelcomePage()
        self.history_page = HistoryPage()
        self.stacked_widget.addWidget(self.welcome_page)
        self.stacked_widget.addWidget(self.history_page)
        layout.addWidget(self.stacked_widget)
        
        self.welcome_page.history_button.clicked.connect(self.switch_to_history_page)
        self.history_page.return_button.clicked.connect(self.switch_to_welcome_page)

    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def show(self, username):
        super().show()
        now = self.get_current_time()
        self.statusBar().showMessage(f'Login time: {now}')
        self.user_info_label.setText(f"Welcome, {username} ")
        self.welcome_page.get_uploaded_files()
    
    def get_current_time(self):
        datetime = QDateTime.currentDateTime()
        time = list(datetime.toString().split())[3]
        year = datetime.date().year()
        month = datetime.date().month()
        day = datetime.date().day()
        return str(year) + '-' + str(month) + '-' + str(day) + ' ' + time

    def switch_to_login_window(self):
        self.close()
        self.login_window = LoginWindow(MainWindow().show)
        self.login_window.show()

    def switch_to_history_page(self):
        self.welcome_page.task_name_label.setStyleSheet("color: black")
        self.welcome_page.file_label.setStyleSheet("color: black")
        self.welcome_page.mode_select_label.setStyleSheet("color: black")
        self.welcome_page.target_file_label.setStyleSheet("color: black")
        self.welcome_page.error_label.clear()
        self.stacked_widget.setCurrentIndex(1)
        # update history page

    def switch_to_welcome_page(self):
        self.stacked_widget.setCurrentIndex(0)

if __name__ == "__main__":
    PyQt5.QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    app = QApplication(sys.argv)

    welcome_page = MainWindow()
    welcome_page.show()

    exit(app.exec_())
