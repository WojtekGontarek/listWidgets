import sys
from pathlib import Path

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.studentLW.itemClicked.connect(self.student_change)
        self.ui.auStudentLW.itemClicked.connect(self.august_change)
        self.ui.acceptButton.clicked.connect(self.save_clicked)
        self.ui.dodajButton.clicked.connect(self.add_student)
        self.load()
        self.show()

    def student_change(self):
        # students = self.ui.studentLW.selectedItems()
        # for student in students:
        #     self.ui.auStudentLW.addItem(student.text())

        student = self.ui.studentLW.takeItem(self.ui.studentLW.currentRow())
        self.ui.auStudentLW.addItem(student.text())

    def august_change(self):
        student = self.ui.auStudentLW.takeItem(self.ui.auStudentLW.currentRow())
        self.ui.studentLW.addItem(student.text())

    def save_clicked(self):
        file = open("wyrok.txt", "w")
        for index in range(self.ui.auStudentLW.count()):
            file.write(self.ui.auStudentLW.item(index).text() + "\n")
        file.close()

        file = open("bezpieczni.txt", "w")
        for index in range(self.ui.studentLW.count()):
            file.write(self.ui.studentLW.item(index).text() + "\n")
        file.close()

    def load(self):
        if Path("./wyrok.txt").exists() and Path("./bezpieczni.txt").exists():
            with open("wyrok.txt", "r") as file:
                au_students = file.read().splitlines()
            with open("bezpieczni.txt", "r") as file:
                students = file.read().splitlines()

            self.ui.studentLW.clear()
            self.ui.studentLW.addItems(students)
            self.ui.auStudentLW.addItems(au_students)

            for item in students:
                self.ui.removeStudentCBox.addItem(item)

            self.update_students()

    def update_students(self):
        students = [self.ui.studentLW.item(i).text() for i in range(self.ui.studentLW.count())]
        au_students = [self.ui.auStudentLW.item(i).text() for i in range(self.ui.auStudentLW.count())]

        self.ui.removeStudentCBox.clear()
        for student in students + au_students:
            self.ui.removeStudentCBox.addItem(student)

    def add_student(self):
        student = self.ui.addStudent.text()
        self.ui.studentLW.addItem(student)
        self.update_students()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyForm()
    sys.exit(app.exec())
