# HW2_67011352_Theepakorn.py



# TeskAssignmentPage.py



import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtWebEngineWidgets import *
import markdown as md

class TeskAssignmentPage(QWidget):
    def __init__(self) -> None:
        QWidget.__init__(self, None)
        v_box = QVBoxLayout()
        nav_bar = QHBoxLayout()

        self.cur_mode_label = QLabel(self)
        self.current_mode_text = "Sync"
        self.cur_mode_label.setText(f"Mode: {self.current_mode_text}")
        nav_w = QWidget()
        nav_w.setLayout(nav_bar)
        nav_bar.addWidget(self.cur_mode_label)
        nav_w.setFixedHeight(50)
        nav_w.setStyleSheet("""
            background-color: #7ec9ed;
        """)
        self.setWindowTitle("Task Assignment Page")
        self.resize(1280, 720)
        self.show()
        self.tab_stack = QStackedWidget()
        self.setStyleSheet("""
            background-color: #ffd77f;
        """)

        self.text = "Type Here..."


        toggle_mode_btn = QPushButton()
        toggle_mode_btn.setText("Toggle mode")
        toggle_mode_btn.setFixedWidth(100)
        toggle_mode_btn.clicked.connect(self.toggle_mode)
        nav_bar.addWidget(toggle_mode_btn)

        # Sync Mode: Sync with file and re-render after saved

        sync_tab = QWidget()
        sync_layout = QVBoxLayout(sync_tab)
        sync_preview_label = QLabel()
        sync_preview_label.setText("Preview: ")
        sync_preview_label.setFixedHeight(50)
        sync_preview_label.setStyleSheet("""
            font-size: 32px;
        """)
        self.sync_preview_html = QWebEngineView()
        self.sync_preview_html.setHtml(self.text)
        self.sync_preview_html.setStyleSheet("""
            background-color: #ffffff
        """)
        sync_layout.addWidget(sync_preview_label)
        sync_layout.addWidget(self.sync_preview_html)

        # Manual Mode: Type inside the TextArea on the LHS of the screen

        manual_tab = QWidget()
        manual_layout = QHBoxLayout(manual_tab)
        manual_code_w = QWidget()
        manual_code = QVBoxLayout(manual_code_w)
        manual_code_label = QLabel()
        manual_code_label.setText("Code:")
        manual_code_label.setStyleSheet("""
            font-size: 32px;
        """)
        self.manual_code_editor = QTextEdit()
        self.manual_code_editor.setPlaceholderText(self.text)
        self.manual_code_editor.setUndoRedoEnabled(True)
        self.manual_code_editor.setStyleSheet("""
            background-color: #ffffff
        """)
        manual_code_btn = QPushButton()
        manual_code_btn.clicked.connect(self.convert)
        manual_code_btn.setText("Convert")
        manual_code.addWidget(manual_code_label)
        manual_code.addWidget(self.manual_code_editor)
        manual_code.addWidget(manual_code_btn)

        manual_code.addWidget(self.manual_code_editor)
        manual_code_w.setLayout(manual_code)
        self.manual_preview_html = QWebEngineView()
        self.manual_preview_html.setHtml(self.text)
        self.manual_preview_html.setStyleSheet("""
            background-color: #ffffff
        """)
        manual_layout.addWidget(manual_code_w)
        manual_layout.addWidget(self.manual_preview_html)

        self.tab_stack.addWidget(sync_tab)
        self.tab_stack.addWidget(manual_tab)
        self.sync_preview_html.setHtml(self.text)
        self.manual_preview_html.setHtml(self.text)

        v_box.addWidget(nav_w)
        v_box.addWidget(self.tab_stack)
        self.setLayout(v_box)

    def toggle_mode(self) -> None:
        if self.current_mode_text == "Sync":
            self.current_mode_text = "Manual"
            self.tab_stack.setCurrentIndex(1)
            self.cur_mode_label.setText(f"Mode: {self.current_mode_text}")
        else:
            self.current_mode_text = "Sync"
            self.tab_stack.setCurrentIndex(0)
            self.cur_mode_label.setText(f"Mode: {self.current_mode_text}")

    def convert(self) -> None:
        self.text = self.manual_code_editor.toPlainText()
        self.sync_preview_html.setHtml(md.markdown(self.text))
        self.manual_preview_html.setHtml(md.markdown(self.text))


def main() -> None:
    app = QApplication(sys.argv)
    _ = TeskAssignmentPage()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
