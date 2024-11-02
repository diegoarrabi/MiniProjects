import sys
import random

from os import path

from PySide6.QtCore import QEvent, Qt
from PySide6.QtGui import QIcon, QKeyEvent, QScreen, QPainter, QColor

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QPushButton,
    QLabel,
    QLineEdit
)


class PaintCanvas (QWidget):
    def __init__(self):
        super().__init__()

    def _trigger_refresh(self):
        self.update()

    def paintEvent(self, event):
        qPaint = QPainter()
        qPaint.begin(self)
        self.drawPoints(qPaint)
        qPaint.end()

    def drawPoints(self, qPaint):
        line_len = 10

        vector_x = (self.parent().current_vector[0]-3)
        vector_y = (self.parent().current_vector[1]-48)

        line_y1 = vector_y - line_len
        line_y2 = vector_y + line_len
        
        line_x1 = vector_x - line_len
        line_x2 = vector_x + line_len
        
        print(vector_x, vector_y)
        qPaint.setPen(QColor('red'))
        qPaint.drawLine(vector_x, line_y1, vector_x, line_y2)
        qPaint.drawLine(line_x1, vector_y, line_x2, vector_y)


class MainWindow (QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # WINDOW SETTINGS ###########################################################################
        HEIGHT = screen_height
        WIDTH = screen_width
        WIN_X_POS = 0
        WIN_Y_POS = 0
        self.previous_vector = (0, 0)
        self.current_vector = (0, 0)

        self.setWindowTitle("Measure")
        self.setMinimumHeight(HEIGHT)
        self.setMinimumWidth(WIDTH)
        self.setMaximumHeight(HEIGHT)
        self.setMaximumWidth(WIDTH)
        self.setGeometry(WIN_X_POS, WIN_Y_POS, WIDTH, HEIGHT)

        self.setWindowFlag(Qt.WindowType.NoDropShadowWindowHint, True)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setWindowOpacity(0.8)

        self.setMouseTracking(True)

        # LABELS ####################################################################################

        self.x_pos = 10
        self.y_pos = 10

        self.x_pos_str = QLabel()
        self.x_pos_str.setText(f"X: [ {self.x_pos} ]")
        self.y_pos_str = QLabel()
        self.y_pos_str.setText(f"Y: [ {self.y_pos} ]")
        self.main_widget = PaintCanvas()
        self.setCentralWidget(self.main_widget)

    def mousePressEvent(self, event):
        self.x_pos = int(event.globalPosition().x())
        self.y_pos = int(event.globalPosition().y())
        self.x_pos_str.setText(f"X: [ {self.x_pos} ]")
        self.y_pos_str.setText(f"Y: [ {self.y_pos} ]")
        self.current_vector = (self.x_pos, self.y_pos)
        self.getDistance(self.previous_vector, self.current_vector)
        self.previous_vector = self.current_vector

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Escape:
            app.quit()
        return super().keyPressEvent(event)

    def getDistance(self, previous_vector, current_vector):
        '''
        print("\x1b[2J")
        print("\x1b[2H")
        print(previous_vector)
        print(current_vector)
        print(f"X: {abs(previous_vector[0]-current_vector[0])}")
        print(f"Y: {abs(previous_vector[1]-current_vector[1])}")
        '''
        self.main_widget._trigger_refresh()


# APPLICATION RUNTIME ####################################################################################
app = QApplication(sys.argv)

my_screen_size = QScreen.availableGeometry(app.primaryScreen())
screen_width = my_screen_size.width()
screen_height = my_screen_size.height()


window = MainWindow()
window.show()

# window = PaintCanvas()
app.exec()
print("\x1b[2J")
print("\x1b[2H")

sys.exit()
