"""
Created by: Taylor Denouden
Organization: Hakai Institute
Date: 2020-09-17
Description: 
"""

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog

from utils import resource_path


class DirectoryPath(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        uic.loadUi(resource_path('directory_path.ui'), self)
        self.show()

    @property
    def value(self) -> str:
        return self.textedit.text()

    @value.setter
    def value(self, path: str):
        self.textedit.setText(path)

    def dir_btn_clicked(self):
        self.value = QFileDialog.getExistingDirectory(
            self, 'Select directory', self.value, QFileDialog.ShowDirsOnly)