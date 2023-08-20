from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()

mainLine = QVBoxLayout()
menuButton = QPushButton("Меню")
restButton = QPushButton("Відпочити")
timeSpin = QSpinBox()
timeLbl = QLabel("хвилин")

extraLine1 = QHBoxLayout()
extraLine1.addWidget(menuButton)
extraLine1.addWidget(restButton)
extraLine1.addWidget(timeSpin)
extraLine1.addWidget(timeLbl)
mainLine.addLayout(extraLine1)

question = QLabel("Як буде 'яблуко' по-англійськи?")
mainLine.addWidget(question)

answersGroup = QGroupBox("Варіанти відповідей:")
answersLine = QVBoxLayout()
answer1 = QRadioButton("python")
answer2 = QRadioButton("race")
answer3 = QRadioButton("apple")
answer4 = QRadioButton("plane")

answersLine.addWidget(answer1)
answersLine.addWidget(answer2)
answersLine.addWidget(answer3)
answersLine.addWidget(answer4)
answersGroup.setLayout(answersLine)
mainLine.addWidget(answersGroup)


window.setLayout(mainLine)
window.show()
app.exec()