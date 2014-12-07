# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\CMA_Interface.ui'
#
# Created: Sun Dec 07 12:42:43 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(544, 591)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.FreePartitionInfo = QtGui.QTextBrowser(self.centralwidget)
        self.FreePartitionInfo.setGeometry(QtCore.QRect(20, 270, 501, 131))
        self.FreePartitionInfo.setObjectName(_fromUtf8("FreePartitionInfo"))
        self.FirstButton = QtGui.QPushButton(self.centralwidget)
        self.FirstButton.setGeometry(QtCore.QRect(140, 10, 101, 31))
        self.FirstButton.setObjectName(_fromUtf8("FirstButton"))
        self.KbLabel = QtGui.QLabel(self.centralwidget)
        self.KbLabel.setGeometry(QtCore.QRect(110, 20, 56, 12))
        self.KbLabel.setObjectName(_fromUtf8("KbLabel"))
        self.releaseButton = QtGui.QPushButton(self.centralwidget)
        self.releaseButton.setGeometry(QtCore.QRect(140, 110, 101, 51))
        self.releaseButton.setObjectName(_fromUtf8("releaseButton"))
        self.MemoryInput = QtGui.QLineEdit(self.centralwidget)
        self.MemoryInput.setGeometry(QtCore.QRect(20, 9, 81, 31))
        self.MemoryInput.setObjectName(_fromUtf8("MemoryInput"))
        self.info = QtGui.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(20, 250, 291, 16))
        self.info.setObjectName(_fromUtf8("info"))
        self.BestButton = QtGui.QPushButton(self.centralwidget)
        self.BestButton.setGeometry(QtCore.QRect(20, 50, 101, 31))
        self.BestButton.setObjectName(_fromUtf8("BestButton"))
        self.WorstButton = QtGui.QPushButton(self.centralwidget)
        self.WorstButton.setGeometry(QtCore.QRect(140, 50, 101, 31))
        self.WorstButton.setObjectName(_fromUtf8("WorstButton"))
        self.CompactingButton = QtGui.QPushButton(self.centralwidget)
        self.CompactingButton.setGeometry(QtCore.QRect(20, 180, 221, 61))
        self.CompactingButton.setObjectName(_fromUtf8("CompactingButton"))
        self.ProcessNumberLabel = QtGui.QLabel(self.centralwidget)
        self.ProcessNumberLabel.setGeometry(QtCore.QRect(20, 110, 91, 21))
        self.ProcessNumberLabel.setObjectName(_fromUtf8("ProcessNumberLabel"))
        self.informationLabel = QtGui.QLabel(self.centralwidget)
        self.informationLabel.setGeometry(QtCore.QRect(270, 10, 151, 16))
        self.informationLabel.setObjectName(_fromUtf8("informationLabel"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 420, 511, 151))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 130, 81, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.ProcessListDisplay = QtGui.QTextBrowser(self.centralwidget)
        self.ProcessListDisplay.setGeometry(QtCore.QRect(270, 30, 251, 181))
        self.ProcessListDisplay.setObjectName(_fromUtf8("ProcessListDisplay"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.CompactingButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.compactingClicked)
        QtCore.QObject.connect(self.releaseButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.releasingClicked)
        QtCore.QObject.connect(self.WorstButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.worstClicked)
        QtCore.QObject.connect(self.FirstButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.firstClicked)
        QtCore.QObject.connect(self.BestButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.bestClicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.FirstButton.setText(_translate("MainWindow", "Frist Fit 할당", None))
        self.KbLabel.setText(_translate("MainWindow", "KB", None))
        self.releaseButton.setText(_translate("MainWindow", "프로세스 해제", None))
        self.info.setText(_translate("MainWindow", "빈공간 파티션 정보 및 기타 정보", None))
        self.BestButton.setText(_translate("MainWindow", "Best Fit 할당", None))
        self.WorstButton.setText(_translate("MainWindow", "Worst Fit 할당", None))
        self.CompactingButton.setText(_translate("MainWindow", "메모리 공간 통합", None))
        self.ProcessNumberLabel.setText(_translate("MainWindow", "프로세스 번호", None))
        self.informationLabel.setText(_translate("MainWindow", "프로세스 리스트/주소 정보", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">빈공간이 충분하나 프로세스가 할당되지 않는 경우 [메모리 공간 통합]을 누르십시오.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">이는 메모리의 빈 공간이 조각화되어 있는 경우</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">메모리에 위치한 프로세스의 위치를 정렬하고, 빈 공간을 합쳐 하나의 파티션으로 제공합니다.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">비어있는 메모리 파티션은 위 [빈공간 파티션 정보 및 기타 정보] 콘솔에서 확인할 수 있습니다.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[파티션의 주소: 파티션의 용량] 으로 나타내어 집니다.</p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

