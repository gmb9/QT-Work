import sys
from PySide2.QtUiTools import QUiLoader #allows us to import .ui files
from PySide2.QtWidgets import QApplication, QLineEdit, QPushButton
from PySide2.QtCore import QFile, QObject

class MainWindow(QObject):

    #class constructor
    def __init__(self, ui_file, parent=None):

        #call parent QObject constructor
        super(MainWindow, self).__init__(parent)

        #load the UI file into Python
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)

        #always remember to close files
        ui_file.close()

        button_0 = self.window.findChild(QPushButton, 'button_zero')
        button_0.clicked.connect(self.zero_button_clicked)

        button_1 = self.window.findChild(QPushButton, 'button_one')
        button_1.clicked.connect(self.one_button_clicked)

        button_2 = self.window.findChild(QPushButton, 'button_two')
        button_2.clicked.connect(self.two_button_clicked)

        button_3 = self.window.findChild(QPushButton, 'button_three')
        button_3.clicked.connect(self.three_button_clicked)
        
        button_4 = self.window.findChild(QPushButton, 'button_four')
        button_4.clicked.connect(self.four_button_clicked)

        button_5 = self.window.findChild(QPushButton, 'button_five')
        button_5.clicked.connect(self.five_button_clicked)

        button_6 = self.window.findChild(QPushButton, 'button_six')
        button_6.clicked.connect(self.six_button_clicked)

        button_7 = self.window.findChild(QPushButton, 'button_seven')
        button_7.clicked.connect(self.seven_button_clicked)

        button_8 = self.window.findChild(QPushButton, 'button_eight')
        button_8.clicked.connect(self.eight_button_clicked)

        button_9 = self.window.findChild(QPushButton, 'button_nine')
        button_9.clicked.connect(self.nine_button_clicked)
        
        """
        #add event listener to the 7 button
        sevenButton = self.window.findChild(QPushButton, 'button_seven')
        sevenButton.clicked.connect(self.seven_button_clicked)
        """

        #show window to user
        self.window.show()
    
    def zero_button_clicked(self):
        button_0 = self.window.findChild(QPushButton, 'button_zero')
        accumulator = self.window.findChild(QLineEdit, 'answer')
        accumulator.setText(self.label.text() + button_0.text())

    def one_button_clicked(self):
        button_1 = self.window.findChild(QPushButton, 'button_one')
        accumulator = self.window.findChild(QLineEdit, 'answer')
        accumulator.setText(self.label.text() + button_1.text())

    def two_button_clicked(self):
        button_2 = self.window.findChild(QPushButton, 'button_two')
        accumulator = self.window.findChild(QLineEdit, 'answer')
        accumulator.setText(self.label.text() + button_2.text())

    def three_button_clicked(self):
        button_3 = self.window.findChild(QPushButton, 'button_three')
        accumulator = self.window.findChild(QLineEdit, 'answer')
        accumulator.setText(self.label.text() + button_3.text())

    def four_button_clicked(self):
        button_4 = self.window.findChild(QPushButton, 'button_four')
        accumulator = self.window.findChild(QLineEdit, 'answer')
        accumulator.setText(self.label.text() + button_4.text())

    def five_button_clicked(self):
        button_5 = self.window.findChild(QPushButton, 'button_five')
        accumulator = self.window.findChild(QLineEdit, 'answer')
        accumulator.setText(self.label.text() + button_5.text())

    def six_button_clicked(self):
        button_6 = self.window.findChild(QPushButton, 'button_six')
        accumulator = self.window.findChild(QLineEdit, 'answer')
        accumulator.setText(self.label.text() + button_6.text())

    def seven_button_clicked(self):
        button_7 = self.window.findChild(QPushButton, 'button_seven')
        accumulator = self.window.findChild(QLineEdit, 'answer')
        accumulator.setText(self.label.text() + button_7.text())

    def eight_button_clicked(self):
        button_8 = self.window.findChild(QPushButton, 'button_eight')
        accumulator = self.window.findChild(QLineEdit, 'answer')
        accumulator.setText(self.label.text() + button_8.text())

    def nine_button_clicked(self):
        button_9 = self.window.findChild(QPushButton, 'button_nine')
        accumulator = self.window.findChild(QLineEdit, 'answer')
        accumulator.setText(self.label.text() + button_9.text())

    """
    def login_clicked(self):
        login_button = self.window.findChild(QPushButton, 'login')
        login_button.setEnabaled(False)

        self.window.statusBar().showMessage('Logging In...')
        
    def cancel_clicked(self):
        self.window.close()
    """
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow('calculator.ui')
    sys.exit(app.exec_())