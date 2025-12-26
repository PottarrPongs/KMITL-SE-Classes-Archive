import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from UserSettingsPageUI import Ui_Form

class Setting(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.saveData)
    
    def saveData(self):
        new_username = self.ui.usernameInput.text().strip()
        new_email = self.ui.emailInput.text().strip()
        new_phone = self.ui.phoneInput.text().strip()

        if new_username:
            self.ui.username.setText(f"Username: {new_username}")

        if new_email:
            self.ui.gmail.setText(f"Email: {new_email}")

        if new_phone:
            self.ui.phone.setText(f"Phone: {new_phone}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    w = Setting()
    w.show()
    sys.exit(app.exec())
