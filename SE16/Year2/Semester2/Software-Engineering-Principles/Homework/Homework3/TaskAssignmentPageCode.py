import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtWebEngineWidgets import *
import markdown as md

from TaskAssignmentPageUI import Ui_Form

class TaskAssignmentPage(QWidget):
    def __init__(self) -> None:
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.sync_preview = QWebEngineView()
        self.manual_preview = QWebEngineView()
        self.ui.web_engine_hbox.addWidget(self.sync_preview,1)
        self.ui.preview_vbox_manual.addWidget(self.manual_preview,1)
        self.current_mode_text = "Manual"
        self.text = "Type Here..."
        self.ui.editor.setPlaceholderText(self.text)
        self.ui.toggle_btn.clicked.connect(self.toggle_mode)
        self.ui.manual_convert_btn.clicked.connect(self.convert)
        self.ui.sync_convert_btn.clicked.connect(self.convert)
        self.ui.current_mode_label.setText(f"Mode: {self.current_mode_text}")
        self.ui.manual_save_btn.clicked.connect(self.save)
        self.ui.sync_save_btn.clicked.connect(self.save)
        self.ui.manual_load_btn.clicked.connect(self.load)
        self.ui.sync_load_btn.clicked.connect(self.load)

    def toggle_mode(self) -> None:
        if self.current_mode_text == "Sync":
            self.current_mode_text = "Manual"
            self.ui.mode_tab.setCurrentIndex(0)
            self.ui.current_mode_label.setText(f"Mode: {self.current_mode_text}")
        else:
            self.current_mode_text = "Sync"
            self.ui.mode_tab.setCurrentIndex(1)
            self.ui.current_mode_label.setText(f"Mode: {self.current_mode_text}")

    def convert(self) -> None:
        self.text = self.ui.editor.toPlainText()
        self.sync_preview.setHtml(md.markdown(self.text))
        self.manual_preview.setHtml(md.markdown(self.text))


    def load(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(self,
            "Select a Markdown File",
            "",
            "Markdown Files (*.md)"
        )
        print(file_path)
        if not file_path:
            return None
        try:
            with open(file_path, "r+") as file:
                self.text = file.read()
                print(self.text)
                self.ui.editor.setPlainText(self.text)
        except Exception as e:
            d = QDialog(None)
            vbox = QVBoxLayout()
            label = QLabel()
            label.setText(str(e))
            vbox.addWidget(label)
            d.setLayout(vbox)


    def save(self) -> None:
        file_path, _ = QFileDialog.getSaveFileName(self,
                "Select a Markdown File",
                "",
                "Markdown Files (*.md)"
            )
        if not file_path:
            return None
        try:
            with open(file_path, "w+") as file:
                file.write(self.text)
        except Exception as e:
            d = QDialog(None)
            vbox = QVBoxLayout()
            label = QLabel()
            label.setText(str(e))
            vbox.addWidget(label)
            d.setLayout(vbox)


def main() -> None:
    app = QApplication(sys.argv)
    w = TaskAssignmentPage()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
