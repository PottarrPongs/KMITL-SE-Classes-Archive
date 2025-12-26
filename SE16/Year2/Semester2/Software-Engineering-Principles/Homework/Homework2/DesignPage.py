import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Design(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Design Board")
        self.setMinimumSize(1280, 720)
        self.setStyleSheet("color: black; background-color: whitesmoke;")

        mainLayout = QVBoxLayout(self)

        navbar = QWidget()
        navbar.setFixedHeight(100)
        navbar.setStyleSheet("""
            background-color: #2f8ed2;
            color: white;
        """)
        navLayout = QHBoxLayout(navbar)
        navLayout.setContentsMargins(10, 0, 10, 0)

        btnClass = QPushButton("Class")
        btnInteraction = QPushButton("Interaction")
        btnGantt = QPushButton("Gantt Chart")

        navLayout.addStretch()

        for b in (btnClass, btnInteraction, btnGantt):
            b.setFixedWidth(200)
            b.setFixedHeight(100)
            b.setStyleSheet("""
                QPushButton {
                    font-size: 16px;
                    background: #2f8ed2;
                    color: white;
                }
                QPushButton:hover {
                    background: #fdd148;
                    color: black;
                }
            """)
            navLayout.addWidget(b, alignment=Qt.AlignCenter)

        navLayout.addStretch()

        mainLayout.addWidget(navbar)


        # ========= TOOL PANEL (LEFT SIDE OF BOARD) =========
        self.toolsPanel = QWidget()
        self.toolsPanel.setFixedWidth(150)
        self.toolsPanel.setStyleSheet("""
            background-color: #d9ecf7;
            border-right: 1px solid #b0cddd;
        """)
        toolsLayout = QVBoxLayout(self.toolsPanel)
        toolsLayout.setContentsMargins(10, 20, 10, 20)
        toolsLayout.setSpacing(10)

        toolsLayout.addWidget(QLabel("Tools"))
        toolsLayout.addWidget(QPushButton("Tool 1"))
        toolsLayout.addWidget(QPushButton("Tool 2"))
        toolsLayout.addWidget(QPushButton("Tool 3"))
        toolsLayout.addStretch()

        self.boardStack = QStackedWidget()

        # --- Class Board ---
        classBoard = QWidget()
        classLayout = QVBoxLayout(classBoard)
        classTitle = QLabel("CLASS DIAGRAM BOARD")
        classTitle.setAlignment(Qt.AlignCenter)
        classTitle.setStyleSheet("font-size: 22px; font-weight: bold;")
        classLayout.addWidget(classTitle)

        classImg = QLabel("Class Diagram")
        classImg.setMinimumHeight(450)
        classImg.setAlignment(Qt.AlignCenter)
        classImg.setStyleSheet("""
            background: #eeeeee;
            border: 2px dashed #999;
        """)
        classLayout.addWidget(classImg)
        classLayout.addStretch()

        # --- Interaction Board ---
        interactionBoard = QWidget()
        interactionLayout = QVBoxLayout(interactionBoard)
        interactionTitle = QLabel("INTERACTION DIAGRAM BOARD")
        interactionTitle.setAlignment(Qt.AlignCenter)
        interactionTitle.setStyleSheet("font-size: 22px; font-weight: bold;")
        interactionLayout.addWidget(interactionTitle)

        interactImg = QLabel("Interaction Diagram")
        interactImg.setMinimumHeight(450)
        interactImg.setAlignment(Qt.AlignCenter)
        interactImg.setStyleSheet("""
            background: #eeeeee;
            border: 2px dashed #999;
        """)
        interactionLayout.addWidget(interactImg)
        interactionLayout.addStretch()

        # --- Gantt Chart Board ---
        ganttBoard = QWidget()
        ganttLayout = QVBoxLayout(ganttBoard)
        ganttTitle = QLabel("GANTT CHART")
        ganttTitle.setAlignment(Qt.AlignCenter)
        ganttTitle.setStyleSheet("font-size: 22px; font-weight: bold;")
        ganttLayout.addWidget(ganttTitle)

        ganttImg = QLabel("Gantt Chart")
        ganttImg.setMinimumHeight(450)
        ganttImg.setAlignment(Qt.AlignCenter)
        ganttImg.setStyleSheet("""
            background: #eeeeee;
            border: 2px dashed #999;
        """)
        ganttLayout.addWidget(ganttImg)
        ganttLayout.addStretch()

        self.boardStack.addWidget(classBoard)       
        self.boardStack.addWidget(interactionBoard)  
        self.boardStack.addWidget(ganttBoard)      

        contentWrapper = QHBoxLayout()
        contentWrapper.addWidget(self.toolsPanel)
        contentWrapper.addWidget(self.boardStack)

        wrapperWidget = QWidget()
        wrapperWidget.setLayout(contentWrapper)
        mainLayout.addWidget(wrapperWidget)

        btnClass.clicked.connect(lambda: self.switchBoard(0))
        btnInteraction.clicked.connect(lambda: self.switchBoard(1))
        btnGantt.clicked.connect(lambda: self.switchBoard(2))

        self.show()

    def switchBoard(self, index):
        self.boardStack.setCurrentIndex(index)

        if index == 2: 
            self.toolsPanel.hide()
        else:
            self.toolsPanel.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    w = Design()

    sys.exit(app.exec())