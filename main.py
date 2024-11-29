from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.studentLW.itemChanged.connect(self.student_change)
        self.show()

    def student_change(self):
        print("student changed")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()