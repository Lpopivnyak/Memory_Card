from PyQt5.QtWidgets import *
import random
import questCode

app = QApplication([])
window = QWidget()

mainLine = QVBoxLayout()
menuButton = QPushButton("Меню")
restButton = QPushButton("Відпочити")
timeSpin = QSpinBox()
timeLbl = QLabel("хвилин")
answerButton = QPushButton("Відповісти")
nextQuestButton = QPushButton("Наступне питання")

nextQuestButton.hide()

extraLine1 = QHBoxLayout()
extraLine1.addWidget(menuButton)
extraLine1.addWidget(restButton)
extraLine1.addWidget(timeSpin)
extraLine1.addWidget(timeLbl)
mainLine.addLayout(extraLine1)

question1 = QLabel("Як буде 'яблуко' по-англійськи?")
mainLine.addWidget(question1)

answersGroup = QGroupBox("Варіанти відповідей:")
answersLine = QVBoxLayout()
answer1 = QRadioButton("python")
answer2 = QRadioButton("banana")
answer3 = QRadioButton("apple")
answer4 = QRadioButton("grape")
answers = [answer1, answer2, answer3, answer4]

answersLine.addWidget(answer1)
answersLine.addWidget(answer2)
answersLine.addWidget(answer3)
answersLine.addWidget(answer4)
result = QLabel("Результат:")
answersLine.addWidget(result)
result.hide()
answersGroup.setLayout(answersLine)
mainLine.addWidget(answersGroup)


mainLine.addWidget(answerButton)
mainLine.addWidget(nextQuestButton)


def showQuest():
    random.shuffle(answers)
    question1.setText(questCode.quest[questCode.currentQuest]["Питання"])
    answers[0].setText(questCode.quest[questCode.currentQuest]["Неправильна відповідь1"])
    answers[1].setText(questCode.quest[questCode.currentQuest]["Неправильна відповідь2"])
    answers[2].setText(questCode.quest[questCode.currentQuest]["Правильна відповідь"])
    answers[3].setText(questCode.quest[questCode.currentQuest]["Неправильна відповідь3"])

showQuest()

def showResult():
    answers[0].hide()
    answers[1].hide()
    answers[2].hide()
    answers[3].hide()
    answerButton.hide()
    result.show()
    nextQuestButton.show()

    if answers[2].isChecked():
        result.setText("Правильно")
    else:
        result.setText("Неправильно")

answerButton.clicked.connect(showResult)


window.setLayout(mainLine)
window.show()
app.exec()