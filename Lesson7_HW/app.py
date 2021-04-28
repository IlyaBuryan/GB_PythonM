from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import uic, QtSql
import sys


class Window(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        uic.loadUi('v1.ui', self)

        self.pushButton.clicked.connect(
            self.dialog
        )

    def dialog(self):
        fname = QFileDialog.getOpenFileName(self, 'title')
        self.textEdit.setText(f'{fname[0]}')

        conn = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        conn.setDatabaseName(f'{fname[0]}')

        if conn.open():
            query_model = QtSql.QSqlQueryModel()
            query_model.setQuery('SELECT * FROM categories')
            self.tableView.setModel(query_model)

        else:
            print(conn.lastError().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
