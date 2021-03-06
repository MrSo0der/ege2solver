from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 469)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txtb_instance = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtb_instance.sizePolicy().hasHeightForWidth())
        self.txtb_instance.setSizePolicy(sizePolicy)
        self.txtb_instance.setObjectName("txtb_instance")
        self.verticalLayout_2.addWidget(self.txtb_instance)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_br_open = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_br_open.sizePolicy().hasHeightForWidth())
        self.btn_br_open.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.btn_br_open.setMouseTracking(False)
        self.btn_br_open.setAutoDefault(False)
        self.btn_br_open.setDefault(False)
        self.btn_br_open.setFlat(False)
        self.btn_br_open.setObjectName("btn_br_open")
        self.gridLayout_2.addWidget(self.btn_br_open, 0, 0, 1, 1)
        self.btn_x = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_x.sizePolicy().hasHeightForWidth())
        self.btn_x.setSizePolicy(sizePolicy)
        self.btn_x.setObjectName("btn_x")
        self.gridLayout_2.addWidget(self.btn_x, 2, 1, 1, 1)
        self.btn_or = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_or.sizePolicy().hasHeightForWidth())
        self.btn_or.setSizePolicy(sizePolicy)
        self.btn_or.setObjectName("btn_or")
        self.gridLayout_2.addWidget(self.btn_or, 1, 1, 1, 1)
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout_2.addWidget(self.btn_back, 3, 0, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout_2.addWidget(self.btn_1, 0, 3, 1, 1)
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_equal.sizePolicy().hasHeightForWidth())
        self.btn_equal.setSizePolicy(sizePolicy)
        self.btn_equal.setObjectName("btn_equal")
        self.gridLayout_2.addWidget(self.btn_equal, 0, 2, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setObjectName("btn_0")
        self.gridLayout_2.addWidget(self.btn_0, 0, 4, 1, 1)
        self.btn_imp = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_imp.sizePolicy().hasHeightForWidth())
        self.btn_imp.setSizePolicy(sizePolicy)
        self.btn_imp.setObjectName("btn_imp")
        self.gridLayout_2.addWidget(self.btn_imp, 1, 3, 1, 1)
        self.btn_br_close = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_br_close.sizePolicy().hasHeightForWidth())
        self.btn_br_close.setSizePolicy(sizePolicy)
        self.btn_br_close.setObjectName("btn_br_close")
        self.gridLayout_2.addWidget(self.btn_br_close, 0, 1, 1, 1)
        self.btn_y = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_y.sizePolicy().hasHeightForWidth())
        self.btn_y.setSizePolicy(sizePolicy)
        self.btn_y.setObjectName("btn_y")
        self.gridLayout_2.addWidget(self.btn_y, 2, 2, 1, 1)
        self.btn_not = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_not.sizePolicy().hasHeightForWidth())
        self.btn_not.setSizePolicy(sizePolicy)
        self.btn_not.setObjectName("btn_not")
        self.gridLayout_2.addWidget(self.btn_not, 1, 0, 1, 1)
        self.btn_and = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_and.sizePolicy().hasHeightForWidth())
        self.btn_and.setSizePolicy(sizePolicy)
        self.btn_and.setObjectName("btn_and")
        self.gridLayout_2.addWidget(self.btn_and, 1, 2, 1, 1)
        self.btn_accord = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_accord.sizePolicy().hasHeightForWidth())
        self.btn_accord.setSizePolicy(sizePolicy)
        self.btn_accord.setObjectName("btn_accord")
        self.gridLayout_2.addWidget(self.btn_accord, 1, 4, 1, 1)
        self.btn_z = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_z.sizePolicy().hasHeightForWidth())
        self.btn_z.setSizePolicy(sizePolicy)
        self.btn_z.setObjectName("btn_z")
        self.gridLayout_2.addWidget(self.btn_z, 2, 3, 1, 1)
        self.btn_w = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_w.sizePolicy().hasHeightForWidth())
        self.btn_w.setSizePolicy(sizePolicy)
        self.btn_w.setObjectName("btn_w")
        self.gridLayout_2.addWidget(self.btn_w, 2, 0, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout_2.addWidget(self.btn_clear, 3, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_2.setStretch(0, 2160)
        self.verticalLayout_2.setStretch(1, 3000)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_str_value = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_str_value.sizePolicy().hasHeightForWidth())
        self.lbl_str_value.setSizePolicy(sizePolicy)
        self.lbl_str_value.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_str_value.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_str_value.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbl_str_value.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_str_value.setScaledContents(False)
        self.lbl_str_value.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_str_value.setWordWrap(False)
        self.lbl_str_value.setObjectName("lbl_str_value")
        self.horizontalLayout_3.addWidget(self.lbl_str_value)
        self.cbox_str_value = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbox_str_value.sizePolicy().hasHeightForWidth())
        self.cbox_str_value.setSizePolicy(sizePolicy)
        self.cbox_str_value.setEditable(False)
        self.cbox_str_value.setObjectName("cbox_str_value")
        self.cbox_str_value.addItem("")
        self.cbox_str_value.addItem("")
        self.cbox_str_value.addItem("")
        self.cbox_str_value.addItem("")
        self.cbox_str_value.addItem("")
        self.cbox_str_value.addItem("")
        self.cbox_str_value.addItem("")
        self.cbox_str_value.addItem("")
        self.horizontalLayout_3.addWidget(self.cbox_str_value)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_i_24 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_24.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_24.sizePolicy().hasHeightForWidth())
        self.btn_i_24.setSizePolicy(sizePolicy)
        self.btn_i_24.setObjectName("btn_i_24")
        self.gridLayout.addWidget(self.btn_i_24, 5, 3, 1, 1)
        self.btn_i_18 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_18.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_18.sizePolicy().hasHeightForWidth())
        self.btn_i_18.setSizePolicy(sizePolicy)
        self.btn_i_18.setObjectName("btn_i_18")
        self.gridLayout.addWidget(self.btn_i_18, 4, 1, 1, 1)
        self.btn_i_19 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_19.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_19.sizePolicy().hasHeightForWidth())
        self.btn_i_19.setSizePolicy(sizePolicy)
        self.btn_i_19.setObjectName("btn_i_19")
        self.gridLayout.addWidget(self.btn_i_19, 4, 2, 1, 1)
        self.btn_i_20 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_20.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_20.sizePolicy().hasHeightForWidth())
        self.btn_i_20.setSizePolicy(sizePolicy)
        self.btn_i_20.setObjectName("btn_i_20")
        self.gridLayout.addWidget(self.btn_i_20, 4, 3, 1, 1)
        self.btn_i_21 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_21.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_21.sizePolicy().hasHeightForWidth())
        self.btn_i_21.setSizePolicy(sizePolicy)
        self.btn_i_21.setObjectName("btn_i_21")
        self.gridLayout.addWidget(self.btn_i_21, 5, 0, 1, 1)
        self.btn_i_22 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_22.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_22.sizePolicy().hasHeightForWidth())
        self.btn_i_22.setSizePolicy(sizePolicy)
        self.btn_i_22.setObjectName("btn_i_22")
        self.gridLayout.addWidget(self.btn_i_22, 5, 1, 1, 1)
        self.btn_i_27 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_27.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_27.sizePolicy().hasHeightForWidth())
        self.btn_i_27.setSizePolicy(sizePolicy)
        self.btn_i_27.setObjectName("btn_i_27")
        self.gridLayout.addWidget(self.btn_i_27, 6, 2, 1, 1)
        self.btn_i_23 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_23.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_23.sizePolicy().hasHeightForWidth())
        self.btn_i_23.setSizePolicy(sizePolicy)
        self.btn_i_23.setObjectName("btn_i_23")
        self.gridLayout.addWidget(self.btn_i_23, 5, 2, 1, 1)
        self.btn_i_26 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_26.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_26.sizePolicy().hasHeightForWidth())
        self.btn_i_26.setSizePolicy(sizePolicy)
        self.btn_i_26.setObjectName("btn_i_26")
        self.gridLayout.addWidget(self.btn_i_26, 6, 1, 1, 1)
        self.btn_i_25 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_25.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_25.sizePolicy().hasHeightForWidth())
        self.btn_i_25.setSizePolicy(sizePolicy)
        self.btn_i_25.setObjectName("btn_i_25")
        self.gridLayout.addWidget(self.btn_i_25, 6, 0, 1, 1)
        self.btn_i_28 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_28.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_28.sizePolicy().hasHeightForWidth())
        self.btn_i_28.setSizePolicy(sizePolicy)
        self.btn_i_28.setObjectName("btn_i_28")
        self.gridLayout.addWidget(self.btn_i_28, 6, 3, 1, 1)
        self.btn_i_12 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_12.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_12.sizePolicy().hasHeightForWidth())
        self.btn_i_12.setSizePolicy(sizePolicy)
        self.btn_i_12.setObjectName("btn_i_12")
        self.gridLayout.addWidget(self.btn_i_12, 2, 3, 1, 1)
        self.btn_i_16 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_16.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_16.sizePolicy().hasHeightForWidth())
        self.btn_i_16.setSizePolicy(sizePolicy)
        self.btn_i_16.setObjectName("btn_i_16")
        self.gridLayout.addWidget(self.btn_i_16, 3, 3, 1, 1)
        self.btn_i_11 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_11.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_11.sizePolicy().hasHeightForWidth())
        self.btn_i_11.setSizePolicy(sizePolicy)
        self.btn_i_11.setObjectName("btn_i_11")
        self.gridLayout.addWidget(self.btn_i_11, 2, 2, 1, 1)
        self.btn_i_10 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_10.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_10.sizePolicy().hasHeightForWidth())
        self.btn_i_10.setSizePolicy(sizePolicy)
        self.btn_i_10.setObjectName("btn_i_10")
        self.gridLayout.addWidget(self.btn_i_10, 2, 1, 1, 1)
        self.btn_i_14 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_14.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_14.sizePolicy().hasHeightForWidth())
        self.btn_i_14.setSizePolicy(sizePolicy)
        self.btn_i_14.setObjectName("btn_i_14")
        self.gridLayout.addWidget(self.btn_i_14, 3, 1, 1, 1)
        self.btn_i_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_1.sizePolicy().hasHeightForWidth())
        self.btn_i_1.setSizePolicy(sizePolicy)
        self.btn_i_1.setObjectName("btn_i_1")
        self.gridLayout.addWidget(self.btn_i_1, 0, 0, 1, 1)
        self.btn_i_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_2.sizePolicy().hasHeightForWidth())
        self.btn_i_2.setSizePolicy(sizePolicy)
        self.btn_i_2.setObjectName("btn_i_2")
        self.gridLayout.addWidget(self.btn_i_2, 0, 1, 1, 1)
        self.btn_i_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_9.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_9.sizePolicy().hasHeightForWidth())
        self.btn_i_9.setSizePolicy(sizePolicy)
        self.btn_i_9.setObjectName("btn_i_9")
        self.gridLayout.addWidget(self.btn_i_9, 2, 0, 1, 1)
        self.btn_i_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_5.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_5.sizePolicy().hasHeightForWidth())
        self.btn_i_5.setSizePolicy(sizePolicy)
        self.btn_i_5.setAutoDefault(False)
        self.btn_i_5.setDefault(False)
        self.btn_i_5.setFlat(False)
        self.btn_i_5.setObjectName("btn_i_5")
        self.gridLayout.addWidget(self.btn_i_5, 1, 0, 1, 1)
        self.btn_i_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_4.sizePolicy().hasHeightForWidth())
        self.btn_i_4.setSizePolicy(sizePolicy)
        self.btn_i_4.setObjectName("btn_i_4")
        self.gridLayout.addWidget(self.btn_i_4, 0, 3, 1, 1)
        self.btn_i_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_6.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_6.sizePolicy().hasHeightForWidth())
        self.btn_i_6.setSizePolicy(sizePolicy)
        self.btn_i_6.setObjectName("btn_i_6")
        self.gridLayout.addWidget(self.btn_i_6, 1, 1, 1, 1)
        self.btn_i_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_7.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_7.sizePolicy().hasHeightForWidth())
        self.btn_i_7.setSizePolicy(sizePolicy)
        self.btn_i_7.setObjectName("btn_i_7")
        self.gridLayout.addWidget(self.btn_i_7, 1, 2, 1, 1)
        self.btn_i_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_3.sizePolicy().hasHeightForWidth())
        self.btn_i_3.setSizePolicy(sizePolicy)
        self.btn_i_3.setObjectName("btn_i_3")
        self.gridLayout.addWidget(self.btn_i_3, 0, 2, 1, 1)
        self.btn_i_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_8.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_8.sizePolicy().hasHeightForWidth())
        self.btn_i_8.setSizePolicy(sizePolicy)
        self.btn_i_8.setObjectName("btn_i_8")
        self.gridLayout.addWidget(self.btn_i_8, 1, 3, 1, 1)
        self.btn_i_13 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_13.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_13.sizePolicy().hasHeightForWidth())
        self.btn_i_13.setSizePolicy(sizePolicy)
        self.btn_i_13.setObjectName("btn_i_13")
        self.gridLayout.addWidget(self.btn_i_13, 3, 0, 1, 1)
        self.btn_i_17 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_17.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_17.sizePolicy().hasHeightForWidth())
        self.btn_i_17.setSizePolicy(sizePolicy)
        self.btn_i_17.setObjectName("btn_i_17")
        self.gridLayout.addWidget(self.btn_i_17, 4, 0, 1, 1)
        self.btn_i_15 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_15.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_15.sizePolicy().hasHeightForWidth())
        self.btn_i_15.setSizePolicy(sizePolicy)
        self.btn_i_15.setObjectName("btn_i_15")
        self.gridLayout.addWidget(self.btn_i_15, 3, 2, 1, 1)
        self.btn_i_29 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_29.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_29.sizePolicy().hasHeightForWidth())
        self.btn_i_29.setSizePolicy(sizePolicy)
        self.btn_i_29.setObjectName("btn_i_29")
        self.gridLayout.addWidget(self.btn_i_29, 7, 0, 1, 1)
        self.btn_i_30 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_30.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_30.sizePolicy().hasHeightForWidth())
        self.btn_i_30.setSizePolicy(sizePolicy)
        self.btn_i_30.setObjectName("btn_i_30")
        self.gridLayout.addWidget(self.btn_i_30, 7, 1, 1, 1)
        self.btn_i_31 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_31.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_31.sizePolicy().hasHeightForWidth())
        self.btn_i_31.setSizePolicy(sizePolicy)
        self.btn_i_31.setObjectName("btn_i_31")
        self.gridLayout.addWidget(self.btn_i_31, 7, 2, 1, 1)
        self.btn_i_32 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_i_32.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i_32.sizePolicy().hasHeightForWidth())
        self.btn_i_32.setSizePolicy(sizePolicy)
        self.btn_i_32.setObjectName("btn_i_32")
        self.gridLayout.addWidget(self.btn_i_32, 7, 3, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_3.setStretch(0, 10)
        self.verticalLayout_3.setStretch(1, 150)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_check = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_check.sizePolicy().hasHeightForWidth())
        self.btn_check.setSizePolicy(sizePolicy)
        self.btn_check.setObjectName("btn_check")
        self.horizontalLayout_2.addWidget(self.btn_check)
        self.btn_cross = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cross.sizePolicy().hasHeightForWidth())
        self.btn_cross.setSizePolicy(sizePolicy)
        self.btn_cross.setObjectName("btn_cross")
        self.horizontalLayout_2.addWidget(self.btn_cross)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lbl_main = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_main.sizePolicy().hasHeightForWidth())
        self.lbl_main.setSizePolicy(sizePolicy)
        self.lbl_main.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_main.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lbl_main.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_main.setScaledContents(False)
        self.lbl_main.setWordWrap(False)
        self.lbl_main.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.lbl_main.setObjectName("lbl_main")
        self.horizontalLayout_2.addWidget(self.lbl_main)
        self.horizontalLayout_2.setStretch(0, 90)
        self.horizontalLayout_2.setStretch(1, 90)
        self.horizontalLayout_2.setStretch(2, 90)
        self.horizontalLayout_2.setStretch(3, 650)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 200)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 15)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ege2solver"))
        self.txtb_instance.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI Semibold\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">?????????????????? (??????????????)</p></body></html>"))
        self.btn_br_open.setText(_translate("MainWindow", "("))
        self.btn_x.setText(_translate("MainWindow", "x"))
        self.btn_or.setText(_translate("MainWindow", "???"))
        self.btn_back.setText(_translate("MainWindow", "???"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_imp.setText(_translate("MainWindow", "???"))
        self.btn_br_close.setText(_translate("MainWindow", ")"))
        self.btn_y.setText(_translate("MainWindow", "y"))
        self.btn_not.setText(_translate("MainWindow", "??"))
        self.btn_and.setText(_translate("MainWindow", "???"))
        self.btn_accord.setText(_translate("MainWindow", "???"))
        self.btn_z.setText(_translate("MainWindow", "z"))
        self.btn_w.setText(_translate("MainWindow", "w"))
        self.btn_clear.setText(_translate("MainWindow", "C"))
        self.lbl_str_value.setText(_translate("MainWindow", "???????????????????? ??????????"))
        self.cbox_str_value.setItemText(0, _translate("MainWindow", "1"))
        self.cbox_str_value.setItemText(1, _translate("MainWindow", "2"))
        self.cbox_str_value.setItemText(2, _translate("MainWindow", "3"))
        self.cbox_str_value.setItemText(3, _translate("MainWindow", "4"))
        self.cbox_str_value.setItemText(4, _translate("MainWindow", "5"))
        self.cbox_str_value.setItemText(5, _translate("MainWindow", "6"))
        self.cbox_str_value.setItemText(6, _translate("MainWindow", "7"))
        self.cbox_str_value.setItemText(7, _translate("MainWindow", "8"))
        self.btn_i_24.setText(_translate("MainWindow", "0"))
        self.btn_i_18.setText(_translate("MainWindow", "0"))
        self.btn_i_19.setText(_translate("MainWindow", "0"))
        self.btn_i_20.setText(_translate("MainWindow", "0"))
        self.btn_i_21.setText(_translate("MainWindow", "0"))
        self.btn_i_22.setText(_translate("MainWindow", "0"))
        self.btn_i_27.setText(_translate("MainWindow", "0"))
        self.btn_i_23.setText(_translate("MainWindow", "0"))
        self.btn_i_26.setText(_translate("MainWindow", "0"))
        self.btn_i_25.setText(_translate("MainWindow", "0"))
        self.btn_i_28.setText(_translate("MainWindow", "0"))
        self.btn_i_12.setText(_translate("MainWindow", "0"))
        self.btn_i_16.setText(_translate("MainWindow", "0"))
        self.btn_i_11.setText(_translate("MainWindow", "0"))
        self.btn_i_10.setText(_translate("MainWindow", "0"))
        self.btn_i_14.setText(_translate("MainWindow", "0"))
        self.btn_i_1.setText(_translate("MainWindow", "0"))
        self.btn_i_2.setText(_translate("MainWindow", "0"))
        self.btn_i_9.setText(_translate("MainWindow", "0"))
        self.btn_i_5.setText(_translate("MainWindow", "0"))
        self.btn_i_4.setText(_translate("MainWindow", "0"))
        self.btn_i_6.setText(_translate("MainWindow", "0"))
        self.btn_i_7.setText(_translate("MainWindow", "0"))
        self.btn_i_3.setText(_translate("MainWindow", "0"))
        self.btn_i_8.setText(_translate("MainWindow", "0"))
        self.btn_i_13.setText(_translate("MainWindow", "0"))
        self.btn_i_17.setText(_translate("MainWindow", "0"))
        self.btn_i_15.setText(_translate("MainWindow", "0"))
        self.btn_i_29.setText(_translate("MainWindow", "0"))
        self.btn_i_30.setText(_translate("MainWindow", "0"))
        self.btn_i_31.setText(_translate("MainWindow", "0"))
        self.btn_i_32.setText(_translate("MainWindow", "0"))
        self.btn_check.setText(_translate("MainWindow", "???"))
        self.btn_cross.setText(_translate("MainWindow", "???"))
        self.lbl_main.setText(_translate("MainWindow", "????????????????..."))
