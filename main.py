import sys
import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
from CK import Ui_Form


class CK(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(CK, self).__init__()
        self.setupUi(self)
        self.init()
        self.setWindowTitle("先用串口测试一下")
        self.ser = serial.Serial()
        self.port_check()


    def init(self):
        # 串口检测按钮
        self.pushButton_4.clicked.connect(self.port_check)

        #打开串口
        self.pushButton.clicked.connect(self.port_open)

        #定时器接收数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.data_receive)





    def port_check(self):
        # 检测所有存在的串口，将信息存储在字典中
        self.Com_Dict = {}
        port_list = list(serial.tools.list_ports.comports())
        self.comboBox.clear()
        for port in port_list:
            self.Com_Dict["%s" % port[0]] = "%s" % port[1]
            self.comboBox.addItem(port[0])


    def port_imf(self):
       #显示选定的串口的详细信息
        imf_s = self.comboBox.currentText()



    def port_open(self):
        self.ser.port = self.comboBox.currentText()
        self.ser.baudrate = int(self.comboBox_2.currentText())

        try:
            self.ser.open()
        except:
            QMessageBox.critical(self, "Port Error", "没有串口？")
            return None

        # 打开串口接收定时器，周期为2ms
        self.timer.start(2)






    def data_receive(self):
        try:
            num = self.ser.inWaiting()
        except:
            self.port_close()
            return None
        if num > 0:
            data = self.ser.read(num)
            num = len(data)
            # hex显示
            if self.checkBox.checkState():
                out_s = ''
                for i in range(0, len(data)):
                    out_s = out_s + '{:02X}'.format(data[i]) + ' '
                self.textBrowser.insertPlainText(out_s)
            else:
                # 串口接收到的字符串为b'123',要转化成unicode字符串才能输出到窗口中去
                self.textBrowser.insertPlainText(data.decode('iso-8859-1'))



            # 获取到text光标
            textCursor = self.textBrowser.textCursor()
            # 滚动到底部
            textCursor.movePosition(textCursor.End)
            # 设置光标到text中去
            self.textBrowser.setTextCursor(textCursor)
        else:
            pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = CK()
    myshow.show()
    sys.exit(app.exec_())