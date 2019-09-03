from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from tornado.httpclient import HTTPClient
import json
import urllib

class CustomListItem(QWidget):
    def __init__(self, index, parent=None):
        super(CustomListItem, self).__init__(parent)
        self.index = index
        self.textVBox = QVBoxLayout()
        self.remove_button = QPushButton('X', self)
        self.remove_button.resize(5, 5)
        self.remove_button.clicked.connect(self.remove)
        self.titleQLabel = QLabel()

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.remove_button)
        self.hbox_layout.addWidget(self.titleQLabel)
        self.hbox_layout.setSpacing(5)
        self.setLayout(self.hbox_layout)

    def setTitle(self, text):
        self.titleQLabel.setText(text)
    
    def remove(self):
        http_client = HTTPClient()
        data = urllib.parse.urlencode({'index': self.index })
        res = http_client.fetch('http://localhost:8000/remove', method='POST', headers=None, body=data)
        content = res.body.decode("utf-8")
        print(content)