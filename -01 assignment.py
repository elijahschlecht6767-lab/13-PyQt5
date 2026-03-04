# Try to make an application that is 600px tall and 800px wide, and put 3 labels and 3 pictures on it. 
# Make them all visible. 
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CMP 25-26 Year 1")
        self.setGeometry(00, 00, 600, 800)  # (x,y,width, height)
        # x: distance from the left edge of your screen
        # y: distance from the top of your screen
        self.setWindowIcon(QIcon("images/greg.png"))
        #self.setWindowIcon(QIcon("images/duck.png"))
        #self.setWindowIcon(QIcon("images/frog.png"))

        self.label1=QLabel("Greg", self)
        self.label2=QLabel("Duck", self)
        self.label3=QLabel("Frog", self)

        self.label1.setFont(QFont("Ariel", 30))
        self.label2.setFont(QFont("Ariel", 30))
        self.label3.setFont(QFont("Ariel", 30))
        #font, size

        self.label1.setGeometry(0, 0, 600, 80)
        self.label1.setStyleSheet(
            # This IS CSS!
            "color: rgb(0, 0, 255); "# Supports HEX and ColorNames
            "background-color: rgb(3, 252, 252);"# Supports HEX and ColorNames
            "border: 10px solid black;"
            "font-weight: bold;"
            "font-style: italic;"
            "text-decoration: underline;"
        )
        self.label1.setAlignment(Qt.AlignCenter)

        self.label2.setGeometry(0, 266, 600, 80)
        self.label2.setStyleSheet(
            # This IS CSS!
            "color: rgb(0, 0, 255); "# Supports HEX and ColorNames
            "background-color: rgb(255, 238, 0);"# Supports HEX and ColorNames
            "border: 10px solid black;"
            "font-weight: bold;"
            "font-style: italic;"
            "text-decoration: underline;"
        )
        self.label2.setAlignment(Qt.AlignCenter)

        self.label3.setGeometry(0, 532, 600, 80)
        self.label3.setStyleSheet(
            # This IS CSS!
            "color: rgb(0, 0, 255); "# Supports HEX and ColorNames
            "background-color: rgb(0, 255, 17);"# Supports HEX and ColorNames
            "border: 10px solid black;"
            "font-weight: bold;"
            "font-style: italic;"
            "text-decoration: underline;"
        )
        self.label3.setAlignment(Qt.AlignCenter)

        self.piclabel1=QLabel(self)
        self.pixmap1=QPixmap("images/greg.png")
        # put the image (pixmap) into the label
        self.piclabel1.setPixmap(self.pixmap1)
        # if image is too big or too small, we can make it fit our container.
        self.piclabel1.setScaledContents(True)
        self.piclabel1.setGeometry(0, 80, 600, 186)
        
        self.piclabel2=QLabel(self)
        self.pixmap2=QPixmap("images/duck.png")
        # put the image (pixmap) into the label
        self.piclabel2.setPixmap(self.pixmap2)
        # if image is too big or too small, we can make it fit our container.
        self.piclabel2.setScaledContents(True)
        self.piclabel2.setGeometry(0, 346, 600, 186)

        self.piclabel3=QLabel(self)
        self.pixmap3=QPixmap("images/frog.png")
        # put the image (pixmap) into the label
        self.piclabel3.setPixmap(self.pixmap3)
        # if image is too big or too small, we can make it fit our container.
        self.piclabel3.setScaledContents(True)
        self.piclabel3.setGeometry(0, 612, 600, 186)



def main():
    # Creates the main application and passes in an y command line arguments
    app = QApplication(sys.argv)
    window = MainWindow()  # Instatiate our main window
    window.show()  # Make the window visible

    # Starts the application loop. The program will keep running until you close the Window
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()