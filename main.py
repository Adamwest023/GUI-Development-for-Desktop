# Importing the components we need
import sys
from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder
app = QApplication(sys.argv)

window = ButtonHolder()
window.show()
# Starts the event loop
app.exec()
