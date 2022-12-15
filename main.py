# Importing the components we need
import sys
from PySide6.QtWidgets import QApplication, QWidget
from rockwidget import RocWidget
app = QApplication(sys.argv)

# window = ButtonHolder()
window = RocWidget()
window.show()
# Starts the event loop
app.exec()
