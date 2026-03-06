"""
Layout Managers
a layout manager is a class that arranges widgets automatially in a certain pattern. 
3 common LM types on PyQt5 are:
- QVBoxLayout - Stacks widgets vertically (top to bottom)
- QHBoxLayout - Places widgets horizontally
- QGridLayout - Arranges widgets in a grid of rows and columns
"""
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QMainWindow
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Layout Example")
        self.setGeometry(00, 00, 1500, 1000)
        # up to this point, we did all our widget creation in the init.
        # eventually, that gets super messy.
        # Lets create some functions to pull that stuff out.
        self.initUI()

    def initUI(self):
        # Layout managers.
        # The QMainWindow already has its own layout manager that cannot be overwritten
        # So we must create a single widget to put our layout manager in.
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        # the central widget will act as a container for all other widgets.

        # create a bunch of labels:
        self.backgroundText=QLabel("Choose Character")
        self.backgroundText.setFont(QFont("Ariel", 100))
        self.backgroundText.setAlignment(Qt.AlignCenter)

        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)
        self.label5 = QLabel(self)
        self.label6 = QLabel(self)
        self.label7 = QLabel(self)
        self.label8 = QLabel(self)

        self.pixmap1=QPixmap("images/subzero.png").scaled(
                self.label1.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        
        self.pixmap2=QPixmap("images/erron.png").scaled(
                self.label2.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        
        self.pixmap3=QPixmap("images/jax.png").scaled(
                self.label3.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        
        self.pixmap4=QPixmap("images/johnny.png").scaled(
                self.label4.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        
        self.pixmap5=QPixmap("images/kung_lao.png").scaled(
                self.label5.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        
        self.pixmap6=QPixmap("images/liu_kang.png").scaled(
                self.label6.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        
        self.pixmap7=QPixmap("images/sonya.png").scaled(
                self.label7.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        
        self.pixmap8=QPixmap("images/mr t.png").scaled(
                self.label8.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

        #self.pixmap1=QPixmap("images/subzero.png")
        #self.pixmap2=QPixmap("images/erron.png")
        #self.pixmap3=QPixmap("images/jax.png")
        #self.pixmap4=QPixmap("images/johnny.png")
        #self.pixmap5=QPixmap("images/kung_lao.png")
        #self.pixmap6=QPixmap("images/liu_kang.png")
        #self.pixmap7=QPixmap("images/sonya.png")
        #self.pixmap8=QPixmap("images/mr t.png")

        self.label1.setPixmap(self.pixmap1)
        self.label2.setPixmap(self.pixmap2)
        self.label3.setPixmap(self.pixmap3)
        self.label4.setPixmap(self.pixmap4)
        self.label5.setPixmap(self.pixmap5)
        self.label6.setPixmap(self.pixmap6)
        self.label7.setPixmap(self.pixmap7)
        self.label8.setPixmap(self.pixmap8)

        self.label1.setScaledContents(True)
        self.label2.setScaledContents(True)
        self.label3.setScaledContents(True)
        self.label4.setScaledContents(True)
        self.label5.setScaledContents(True)
        self.label6.setScaledContents(True)
        self.label7.setScaledContents(True)
        self.label8.setScaledContents(True)

        print(self.label1.geometry)

        # Give our labels some color:
        self.backgroundText.setStyleSheet("background-color: grey")
        #label1.setStyleSheet("background-color: red")
        #label2.setStyleSheet("background-color: blue")
        #label3.setStyleSheet("background-color: yellow")
        #label4.setStyleSheet("background-color: green")
        #label5.setStyleSheet("background-color: purple")
        #label6.setStyleSheet("background-color: pink")
        #label7.setStyleSheet("background-color: brown")
        #label8.setStyleSheet("background-color: orange")

        grid=QGridLayout()
        grid = QGridLayout()

        grid.addWidget(self.backgroundText,0,0,1,4)
        grid.addWidget(self.label1,1,0)
        grid.addWidget(self.label2,1,1)
        grid.addWidget(self.label3,1,2)
        grid.addWidget(self.label4,1,3)
        grid.addWidget(self.label5,2,0)
        grid.addWidget(self.label6,2,1)
        grid.addWidget(self.label7,2,2)
        grid.addWidget(self.label8,2,3)

        self.central_widget.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()  # Instatiate our main window
    window.show()  # Make the window visible

    # Starts the application loop. The program will keep running until you close the Window
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()