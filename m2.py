from PyQt5.QtWidgets import  QWidget, QHBoxLayout, \
    QVBoxLayout, QGroupBox, \
   QButtonGroup, QRadioButton, QPushButton, \
    QLabel, QSpinBox, QApplication
from PyQt5.QtCore import  Qt \

window = QWidget()
btn_menu = QPushButton('Меню')
btn_rest = QPushButton('Відпочити')
btn_next = QPushButton('Відповісти')

rb_ans1 = QRadioButton('1')
rb_ans2 = QRadioButton('2')
rb_ans3 = QRadioButton('3')
rb_ans4 = QRadioButton('4')

lb_question = QLabel('Запитання')
lb_question.setStyleSheet("color:#03ecfc; font-size:20px")
window.setStyleSheet('background:gray')
lb_reset = QLabel('хвилин')
lb_result = QLabel('правильно')
lb_right_answer = QLabel('відповідь')

sp_rest = QSpinBox()
gb_qustion = QGroupBox('Варіанти відповідей')

rb_v1 = QVBoxLayout()
rb_v2 = QVBoxLayout()
rb_h1 = QHBoxLayout()

rb_v1.addWidget(rb_ans1)
rb_v1.addWidget(rb_ans2)
rb_v2.addWidget(rb_ans3)
rb_v2.addWidget(rb_ans4)

rb_h1.addLayout(rb_v1)
rb_h1.addLayout(rb_v2)
gb_qustion.setLayout(rb_h1)

gb_answer = QGroupBox()
v1 = QVBoxLayout()
v1.addWidget(lb_result)
v1.addWidget(lb_right_answer)
gb_answer.setLayout(v1)

h1_main = QHBoxLayout()
h2_main = QHBoxLayout()
h3_main = QHBoxLayout()
h4_main = QHBoxLayout()
v1_main = QVBoxLayout()

h1_main.addWidget(btn_menu)
h1_main.addStretch(1)
h1_main.addWidget(btn_rest)
h1_main.addWidget(sp_rest)
h1_main.addWidget(lb_reset)

h2_main.addWidget(lb_question, alignment=(Qt.AlignVCenter | Qt.AlignVCenter))
h3_main.addWidget(gb_qustion)
gb_answer.hide()

h4_main.addStretch(1)
h4_main.addWidget(btn_next, stretch=2)
h4_main.addStretch(1)

v1_main.addLayout(h1_main, stretch=1)
v1_main.addLayout(h2_main, stretch=2)
v1_main.addLayout(h3_main, stretch=8)
v1_main.addLayout(h1_main)
v1_main.setSpacing(5)
window.setLayout(v1_main)
window.resize(550, 450)
