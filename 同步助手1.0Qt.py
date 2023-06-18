import requests
import os
from bs4 import BeautifulSoup
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
class Stats:

    def __init__(self):
        self.ui = QUiLoader().load('main.ui')

        self.ui.sync_button.clicked.connect(self.sync)
        self.ui.about_button.clicked.connect(self.about)
        self.ui.update_button.clicked.connect(self.update)

    def sync(self):
        ip_address = self.ui.url_text.toPlainText()
        try:
            os.mkdir('sync')
        except FileExistsError:
            pass
        sync_list = []
        try:
            page_list = requests.get('http://'+ip_address).text
        except requests.exceptions.ConnectionError:
            QMessageBox.about(self.ui,
                              '报错',
                              'URL格式不正确，或无法访问此服务器')
        soup = BeautifulSoup(page_list, 'html.parser')
        for i in soup.find_all(name='a'):
            sync_list.append(i.string)
        for i in range(len(sync_list)):
            print('正在同步:'+sync_list[i])
            file_address = 'http://' + ip_address + '/' + sync_list[i]
            file = requests.get(file_address, stream = True)
            f = open('sync' + '/' +sync_list[i], "wb")
            for chunk in file.iter_content(chunk_size = 1024):
                if chunk:
                    f.write(chunk)
        QMessageBox.about(self.ui,
                          '同步结果',
                          '同步完成,文件同步在sync文件夹中')
        
    def about(self):
        QMessageBox.about(self.ui,
                          '关于',
                          'By:是鑫焮唉\nBiliBili主页:https://space.bilibili.com/1143915982\n'
                          )
    
    def update(self):
        QMessageBox.about(self.ui,
                          '更新日志',
                          '1.0\nQt版本'
                          )

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec()