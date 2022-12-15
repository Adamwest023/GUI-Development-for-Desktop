"""
# Importing the components we need
import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
app = QApplication(sys.argv)

window = MainWindow(app)
window.show()
# Starts the event loop
app.exec()
"""

from PySide6.QtWidgets import QApplication
import sys
from widget import Widget

app = QApplication(sys.argv)

widget = Widget()
widget.show()

app.exec()
