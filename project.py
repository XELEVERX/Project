from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

app = QApplication([])

window = QWidget()
window.setWindowTitle('Испытай удачу, друг!')
window.resize(300, 300)

button1 = QPushButton('1')
button2 = QPushButton('2')
button3 = QPushButton('3')
button4 = QPushButton('4')
button5 = QPushButton('5')

layout = QGridLayout()

layout.addWidget(button1, 0, 0, alignment=Qt.AlignLeft | Qt.AlignTop)
layout.addWidget(button2, 0, 1, alignment=Qt.AlignRight | Qt.AlignTop)
layout.addWidget(button3, 1, 0, 1, 2, alignment=Qt.AlignCenter)
layout.addWidget(button4, 2, 0, alignment=Qt.AlignLeft | Qt.AlignBottom)
layout.addWidget(button5, 2, 1, alignment=Qt.AlignRight | Qt.AlignBottom)

window.setLayout(layout)

window.show()
app.exec_()