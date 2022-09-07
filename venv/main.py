import requests
from bs4 import BeautifulSoup as bs

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
import NG_Window

form_class = NG_Window.Ui_Dialog

class NGValueFromInvesting():
    def GetNGValue(self):
        NG_price = []
        url = f'https://kr.investing.com/commodities/natural-gas'
        response = requests.get(url)
        soup = bs(response.text, 'html.parser')
        html_value = soup.select('td.datatable_cell__3gwri')

        for i in html_value:
            NG_price.append(i.get_text())
        return NG_price[180:181]

class WindowInterface(QMainWindow, form_class):
    DeviceConnected = False
    processing_done_flag = False
    NGValueFromInvesting().GetNGValue()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonFunction)

    def buttonFunction(self):
        self.pushButton.setText(str(NGValueFromInvesting().GetNGValue()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowInterface()
    myWindow.show()
    app.exec_()

