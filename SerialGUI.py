#coding: utf-8

__author__ = "Tony Chen"

'''
	This is a Serial Debugging Assistant
'''

import sys
import serial
import threading
import binascii 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import serial.tools.list_ports

class MyMainwindow(object):
    ser = serial.Serial()

    def initUI(self, MainWindow):
        MainWindow.resize(579, 369)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 141, 311))

        self.lblSerial = QtWidgets.QLabel(self.groupBox)
        self.lblSerial.setGeometry(QtCore.QRect(10, 20, 31, 16))

        self.lblBaud = QtWidgets.QLabel(self.groupBox)
        self.lblBaud.setGeometry(QtCore.QRect(10, 50, 41, 16))

        self.lblParity = QtWidgets.QLabel(self.groupBox)
        self.lblParity.setGeometry(QtCore.QRect(10, 110, 41, 16))

        self.lblData = QtWidgets.QLabel(self.groupBox)
        self.lblData.setGeometry(QtCore.QRect(10, 80, 41, 16))

        self.lblStop = QtWidgets.QLabel(self.groupBox)
        self.lblStop.setGeometry(QtCore.QRect(10, 140, 41, 16))

        self.comboCom = QtWidgets.QComboBox(self.groupBox)
        self.comboCom.setGeometry(QtCore.QRect(60, 20, 71, 22))
        self.comboCom.addItem("")
        self.comboCom.addItem("")
        self.comboCom.addItem("")
        self.comboCom.addItem("")
        self.comboCom.addItem("")
        self.comboCom.addItem("")
        self.comboCom.addItem("")
        self.comboCom.addItem("")
        self.comboCom.addItem("")
        self.comboCom.addItem("")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 50, 71, 20))

        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(60, 80, 71, 22))
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.comboParity = QtWidgets.QComboBox(self.groupBox)
        self.comboParity.setGeometry(QtCore.QRect(60, 110, 71, 22))
        self.comboParity.addItem("")
        self.comboParity.addItem("")
        self.comboParity.addItem("")
        self.comboParity.addItem("")
        self.comboParity.addItem("")

        self.comboStop = QtWidgets.QComboBox(self.groupBox)
        self.comboStop.setGeometry(QtCore.QRect(60, 140, 71, 22))
        self.comboStop.addItem("")
        self.comboStop.addItem("")
        self.comboStop.addItem("")

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 240, 51, 23))

        self.btnClose = QtWidgets.QPushButton(self.groupBox)
        self.btnClose.setGeometry(QtCore.QRect(80, 240, 51, 23))

        self.btnCheck = QtWidgets.QPushButton(self.groupBox)
        self.btnCheck.setGeometry(QtCore.QRect(40, 200, 61, 23))

        self.lblStaShow = QtWidgets.QLabel(self.groupBox)
        self.lblStaShow.setGeometry(QtCore.QRect(10, 170, 41, 16))

        self.lblStatus = QtWidgets.QLabel(self.groupBox)
        self.lblStatus.setGeometry(QtCore.QRect(70, 170, 54, 16))

        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus.setFont(font)
        self.groupReceive = QtWidgets.QGroupBox(self.centralwidget)
        self.groupReceive.setGeometry(QtCore.QRect(160, 10, 411, 181))
        self.textBrowser = QtWidgets.QTextBrowser(self.groupReceive)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 391, 151))
        self.groupTransmit = QtWidgets.QGroupBox(self.centralwidget)
        self.groupTransmit.setGeometry(QtCore.QRect(160, 200, 261, 121))
        self.textEdit = QtWidgets.QTextEdit(self.groupTransmit)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 241, 91))
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(430, 210, 61, 16))
        self.checkHexTrans = QtWidgets.QCheckBox(self.centralwidget)
        self.checkHexTrans.setGeometry(QtCore.QRect(500, 210, 61, 20))
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(430, 240, 61, 23))
        self.btnTrans = QtWidgets.QPushButton(self.centralwidget)
        self.btnTrans.setGeometry(QtCore.QRect(430, 280, 61, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 579, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height());  
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Serial_gui"))
        MainWindow.setWindowIcon(QIcon('favicon.ico'))
        self.groupBox.setTitle(_translate("MainWindow", "串口设置"))
        self.lblSerial.setText(_translate("MainWindow", "串 口"))
        self.lblBaud.setText(_translate("MainWindow", "波特率"))
        self.lblParity.setText(_translate("MainWindow", "校验位"))
        self.lblData.setText(_translate("MainWindow", "数据位"))
        self.lblStop.setText(_translate("MainWindow", "停止位"))
        self.lineEdit_3.setText(_translate("MainWindow", "9600"))
        self.comboBox.setItemText(0, _translate("MainWindow", "8"))
        self.comboBox.setItemText(1, _translate("MainWindow", "7"))
        self.comboBox.setItemText(2, _translate("MainWindow", "6"))
        self.comboBox.setItemText(3, _translate("MainWindow", "5"))
        self.comboParity.setItemText(0, _translate("MainWindow", "N"))
        self.comboParity.setItemText(1, _translate("MainWindow", "E"))
        self.comboParity.setItemText(2, _translate("MainWindow", "O"))
        self.comboParity.setItemText(3, _translate("MainWindow", "M"))
        self.comboParity.setItemText(4, _translate("MainWindow", "S"))
        self.comboStop.setItemText(0, _translate("MainWindow", "1"))
        self.comboStop.setItemText(1, _translate("MainWindow", "1.5"))
        self.comboStop.setItemText(2, _translate("MainWindow", "2"))
        self.comboCom.setItemText(0, _translate("MainWindow", "COM1"))
        self.comboCom.setItemText(1, _translate("MainWindow", "COM2"))
        self.comboCom.setItemText(2, _translate("MainWindow", "COM3"))
        self.comboCom.setItemText(3, _translate("MainWindow", "COM4"))
        self.comboCom.setItemText(4, _translate("MainWindow", "COM5"))
        self.comboCom.setItemText(5, _translate("MainWindow", "COM6"))
        self.comboCom.setItemText(6, _translate("MainWindow", "COM7"))
        self.comboCom.setItemText(7, _translate("MainWindow", "COM8"))
        self.comboCom.setItemText(8, _translate("MainWindow", "COM9"))
        self.comboCom.setItemText(9, _translate("MainWindow", "COM10"))
        self.pushButton.setText(_translate("MainWindow", "打开"))
        self.pushButton.clicked.connect(self.port_open)

        self.btnClose.setText(_translate("MainWindow", "关闭"))
        self.btnClose.clicked.connect(self.port_close)

        self.btnCheck.setText(_translate("MainWindow", "检测串口"))
        self.btnCheck.clicked.connect(self.port_cheak)

        self.lblStaShow.setText(_translate("MainWindow", "状 态："))
        self.lblStatus.setText(_translate("MainWindow", "串口状态"))
        self.groupReceive.setTitle(_translate("MainWindow", "接收区"))
        self.groupTransmit.setTitle(_translate("MainWindow", "发送区"))
        self.checkBox.setText(_translate("MainWindow", "Hex显示"))
        self.checkHexTrans.setText(_translate("MainWindow", "Hex发送"))
        self.btnClear.setText(_translate("MainWindow", "清除"))
        self.btnClear.clicked.connect(self.clean_data)

        self.btnTrans.setText(_translate("MainWindow", "发送"))
        self.btnTrans.clicked.connect(self.send_data)

    def port_open(self):

        self.ser.port = self.comboCom.currentText()
        self.ser.baudrate = int(self.lineEdit_3.text())
        self.ser.bytesize = int(self.comboBox.currentText()) 
        self.ser.stopbits = int(self.comboStop.currentText())
        self.ser.parity = self.comboParity.currentText()
        self.ser.open()
        if(self.ser.isOpen()):
            self.pushButton.setEnabled(False)
            self.lblStatus.setText("打开成功")
            self.t1 = threading.Thread(target = self.receive_data)
            self.t1.setDaemon(True)
            self.t1.start()
        else:
            self.lblStatus.setText("打开失败")

    def port_close(self):
        self.ser.close()
        if(self.ser.isOpen()):
            self.lblStatus.setText("关闭失败")
        else:
            self.pushButton.setEnabled(True)
            self.lblStatus.setText("关闭成功")


    def send_data(self):
        if(self.ser.isOpen()):
            if(self.checkHexTrans.isChecked()):
                 self.ser.write(binascii.a2b_hex(self.textEdit.toPlainText()))
            else:
                self.ser.write(self.textEdit.toPlainText().encode('utf-8'))
            self.lblStatus.setText("发送成功")
        else:
            self.lblStatus.setText("发送失败")

    def receive_data(self):
        print("The receive_data threading is start")
        res_data = '' 
        num = 0
        while (self.ser.isOpen()):
            size = self.ser.inWaiting()
            if size:
                res_data = self.ser.read_all()
                if(self.checkBox.isChecked()):
                    self.textBrowser.append(binascii.b2a_hex(res_data).decode())
                else:
                    self.textBrowser.append(res_data.decode())
                self.textBrowser.moveCursor(QtGui.QTextCursor.End)
                self.ser.flushInput()               
                num += 1
                self.lblStatus.setText("接收：" + str(num))

    def clean_data(self):
        self.textBrowser.setText("")
        self.lblStatus.setText("接收清空")

    def port_cheak(self):
        Com_List=[]
        port_list = list(serial.tools.list_ports.comports())
        self.comboCom.clear()
        for port in port_list:
            Com_List.append(port[0])
            self.comboCom.addItem(port[0])
        if(len(Com_List) == 0):
            self.lblStatus.setText("没有搜索到串口")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyMainwindow()
    ui.initUI(MainWindow) 
    MainWindow.show()
    sys.exit(app.exec_()) 