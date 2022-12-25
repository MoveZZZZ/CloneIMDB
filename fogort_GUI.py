# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nikitos\PycharmProjects\TMTB_GUI\fogort_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Fogort_page(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 500)
        Form.setMinimumSize(QtCore.QSize(300, 500))
        Form.setMaximumSize(QtCore.QSize(300, 500))
        Form.setStyleSheet("*{\n"
"    border:none;\n"
"    background-color: transparent;\n"
"    background: transparent;\n"
"    padding: 0 ; \n"
"    margin:0;\n"
"    color:#fff;\n"
"}\n"
"#Central_widget{\n"
"    background-color:rgb(42, 54, 63);\n"
"    \n"
"}\n"
"#widget{\n"
"\n"
"border-radius: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"\n"
"padding: 5px 3px;\n"
"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton{\n"
"\n"
"padding: 10px 5px;\n"
"\n"
"opacity: 1;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"background-color: rgb(144, 206, 161);\n"
"color:white;\n"
"}      \n"
"\n"
"")
        self.Central_widget = QtWidgets.QWidget(Form)
        self.Central_widget.setGeometry(QtCore.QRect(0, 0, 300, 500))
        self.Central_widget.setMinimumSize(QtCore.QSize(300, 500))
        self.Central_widget.setMaximumSize(QtCore.QSize(300, 500))
        self.Central_widget.setObjectName("Central_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Central_widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(self.Central_widget)
        self.widget.setMinimumSize(QtCore.QSize(200, 300))
        self.widget.setMaximumSize(QtCore.QSize(200, 300))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMaximumSize(QtCore.QSize(35, 35))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icon/door-key-access-svgrepo-com.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_5.addItem(spacerItem)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setEnabled(True)
        self.label_2.setMinimumSize(QtCore.QSize(0, 13))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:red;\n"
"")
        self.label_2.setLineWidth(1)
        self.label_2.setMidLineWidth(13)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_5.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_5.addItem(spacerItem2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_5.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setEnabled(True)
        self.label_3.setMinimumSize(QtCore.QSize(0, 13))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:red;\n"
"")
        self.label_3.setLineWidth(1)
        self.label_3.setMidLineWidth(13)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_5.addItem(spacerItem3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_5.addWidget(self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setEnabled(True)
        self.label_4.setMinimumSize(QtCore.QSize(0, 13))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:red;\n"
"")
        self.label_4.setLineWidth(1)
        self.label_4.setMidLineWidth(13)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_5.addItem(spacerItem4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_5.addWidget(self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setEnabled(True)
        self.label_5.setMinimumSize(QtCore.QSize(0, 13))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:red;\n"
"")
        self.label_5.setLineWidth(1)
        self.label_5.setMidLineWidth(13)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.verticalLayout_4.addWidget(self.widget, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Email"))
        self.label_2.setText(_translate("Form", "Wrong email"))
        self.pushButton.setText(_translate("Form", "Sent"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Code"))
        self.label_3.setText(_translate("Form", "Wrong code"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "New Password"))
        self.label_4.setText(_translate("Form", "nie podchody po pravilam"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Confirm Password"))
        self.label_5.setText(_translate("Form", "nie podchody po pravilam"))
import res
