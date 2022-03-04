import sys
from PyQt5 import QtWidgets, QtCore

#创建了一个QWidget对象，并设置其大小为400*400，标题为“Hello World”。

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(400,400)
widget.setWindowTitle('Hello World')
widget.show()
sys.exit(app.exec_())




