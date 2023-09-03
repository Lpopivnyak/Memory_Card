from PyQt5.QtWidgets import *
import questCode


def openWindow():
    window = QDialog()

    questLbl = QLabel("Питання")
    questEdit = QLineEdit()

    rightAnswerLbl = QLabel("Правильна відповідь")
    rightAnswerEdit = QLineEdit()

    mainLine = QVBoxLayout()

    addButton = QPushButton("Добавити")

    extraLine1 = QHBoxLayout()
    extraLine1.addWidget(questLbl)
    extraLine1.addWidget(questEdit)
    mainLine.addLayout(extraLine1)

    extraLine2 = QHBoxLayout()
    extraLine2.addWidget(rightAnswerLbl)
    mainLine.addLayout(extraLine2)

    def addFunc():
        questCode.quest.append(
            {
                "Питання": questEdit.text(),
                "Правильна відповідь": rightAnswerLbl.text(),
                "Неправильна відповідь1": "",
                "Неправильна відповідь2": "",
                "Неправильна відповідь3": "",
            }
        )

    mainLine.addWidget(addButton)
    addButton.clicked.connect(addFunc)


    window.setLayout(mainLine)

    window.show()
    window.exec()