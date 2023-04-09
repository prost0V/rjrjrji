from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle
#a = окно
#b = vopros
#c = кнопка
#d = радиокнопка
#app = приложение
#layout = линия
#RadioGroupBox = группа

class Question():
    def __init__(self, question, right_answer, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3

question_list = []
question_list.append(Question("вопрос 1?", "да" , "нет", "на вряд ли" , "люлякебаб"))
question_list.append(Question("вопрос 2?", "да" , "нет", "ленин" , "ми-8мт 1/48 звисда"))
question_list.append(Question("хто круче?", "АНДВА" , "панзеркампфваген чытыри ауст джы", "да" , "сусембэ)"))

shuffle(question_list)

app = QApplication([])
a1 = QWidget()
a1.setWindowTitle('Memory Card')
b1 = QLabel('Какой национальности не существует?')
c1 = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответов')
d1 = QRadioButton('Энцы')
d2 = QRadioButton('Смурфы')
d3 = QRadioButton('Чулымцы')
d4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(d1)
RadioGroup.addButton(d2)
RadioGroup.addButton(d3)
RadioGroup.addButton(d4)

layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()
layout4 = QHBoxLayout()
layout5 = QHBoxLayout()
layout6 = QVBoxLayout()

layout2.addWidget(d1)
layout2.addWidget(d2)
layout3.addWidget(d3)
layout3.addWidget(d4)
layout4.addWidget(b1)
layout5.addWidget(c1)

layout1.addLayout(layout2)
layout1.addLayout(layout3)

RadioGroupBox.setLayout(layout1)

AnswerGroup = QGroupBox("Результат Теста")
lb_result = QLabel("Правильно/Неправильно")
lb_current = QLabel("Правильный ответ")
answer_line = QVBoxLayout()

answer_line.addWidget(lb_result)
answer_line.addWidget(lb_current)

AnswerGroup.setLayout(answer_line)

layout6.addLayout(layout4)
layout6.addWidget(RadioGroupBox)
layout6.addWidget(AnswerGroup)
layout6.addWidget(c1)
AnswerGroup.hide()
layout6.addLayout(layout5)


a1.setLayout(layout6)

def show_result():
    RadioGroupBox.hide()
    AnswerGroup.show()
    c1.setText("Следующий вопрос")

def show_question():
    AnswerGroup.hide()
    RadioGroupBox.show()
    c1.setText('Oтветить')
    RadioGroup.setExclusive(False)
    d1.setChecked(False)
    d2.setChecked(False)
    d3.setChecked(False)
    d4.setChecked(False)
    RadioGroup.setExclusive(True)

def start():
    if c1.text() == 'Oтветить':
        check_answer()
    else:
        next_question()

answers = [d1, d2, d3, d4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    b1.setText(q.question)
    lb_current.setText(q.right_answer)
    show_question()

def next_question():
    a1.num_of_question += 1
    if a1.num_of_question == len(question_list):
        a1.num_of_question = 0
    q = question_list[a1.num_of_question]
    ask(q)

def check_answer():
    if answers[0].isChecked() == True:
        lb_result.setText('Правильно!')
    else:
        lb_result.setText('Неверно!')
    show_result()
a1.num_of_question = -1
next_question()
c1.clicked.connect(start)

a1.show()
app.exec_()