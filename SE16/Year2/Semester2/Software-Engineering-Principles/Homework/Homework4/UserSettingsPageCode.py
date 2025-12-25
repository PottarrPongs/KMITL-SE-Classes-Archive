import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect
from UserSettingsPageUI import Ui_Form

class ProfileWidget(QWidget):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.pixmap = QPixmap(image_path)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        size = min(self.width(), self.height())
        rect = QRect(
            (self.width() - size) // 2,
            (self.height() - size) // 2,
            size,
            size
        )

        path = QPainterPath()
        path.addEllipse(rect)
        painter.setClipPath(path)

        painter.drawPixmap(
            rect,
            self.pixmap.scaled(
                rect.size(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )
        )


class Setting(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.saveData)
        self.saveSfx = QSoundEffect(self)
        self.saveSfx.setSource(QUrl.fromLocalFile("sounds\save_button.wav"))
        self.saveSfx.setVolume(0.5)
        self.hoverSfx = QSoundEffect(self)
        self.hoverSfx.setSource(QUrl.fromLocalFile("sounds\hover.wav"))
       
        self.ui.pushButton.installEventFilter(self)
        self.ui.pushButton.setAttribute(Qt.WA_Hover)

        self.profileWidget = ProfileWidget("./images/profile.jpg", self.ui.widget_2.parent())
        self.profileWidget.setGeometry(self.ui.widget_2.geometry())

        self.ui.widget_2.deleteLater()
        self.ui.widget_2 = self.profileWidget

    def saveData(self):
        self.saveSfx.play()
        new_username = self.ui.usernameInput.text().strip()
        new_email = self.ui.emailInput.text().strip()
        new_phone = self.ui.phoneInput.text().strip()

        if new_username:
            self.ui.username.setText(f"Username: {new_username}")

        if new_email:
            self.ui.gmail.setText(f"Email: {new_email}")

        if new_phone:
            self.ui.phone.setText(f"Phone: {new_phone}")

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
            if obj == self.ui.pushButton:
                self.hoverSfx.play()
        return super().eventFilter(obj, event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    w = Setting()
    w.show()
    sys.exit(app.exec())
