# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OutputAnalysis.ui'
#
# Created: Fri Jan  2 21:57:23 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import	sys
from	PyQt4		import	QtCore, QtGui
import  DSSAT_LIBRARY	as	DSSAT

# Basic settings
dims            = {}
dims['nlat']    = 1
dims['nlon']    = 1
dims['res']     = 1
dims['minlat']  = 10
dims['minlon']  = 10
dims['tStep']   = 1

baseDir         = '/Users/hexg/Dropbox/Study/Princeton_2014-2015_Fall/APC524/APC_Project_HEXG/Data'
CDEFileName     = 'SUMMARYOUT.CDE'
inFileName      = 'Summary.OUT'
outFileName     = 'Summary.nc'
varName         = 'HWAM'

out     = DSSAT.postProcess(baseDir, CDEFileName)
#out.drawTimeSeries(inFileName,varName)
#out.getVarValues(inFileName)[0]
#out.Create_NETCDF_File(dims, inFileName, outFileName)

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

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
	    QtGui.QMainWindow.__init__(self)
	    self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(1035, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 89, 281, 461))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.textBrowser = QtGui.QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(290, 0, 20, 551))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 281, 72))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.line_2 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(320, 20, 681, 41))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.verticalLayoutWidget_3)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.spinBox = QtGui.QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout.addWidget(self.spinBox)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.spinBox_2 = QtGui.QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.horizontalLayout.addWidget(self.spinBox_2)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(320, 70, 681, 71))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 1, 2, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_2, 0, 1, 1, 1)
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(320, 160, 501, 381))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.graphicsView = QtGui.QGraphicsView(self.verticalLayoutWidget_4)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout_3.addWidget(self.graphicsView)
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(840, 160, 160, 381))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem)
        self.pushButton_6 = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.verticalLayout_4.addWidget(self.pushButton_6)
        self.pushButton_5 = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout_4.addWidget(self.pushButton_5)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(320, 140, 681, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1035, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuData_Format_Convert = QtGui.QMenu(self.menuTools)
        self.menuData_Format_Convert.setObjectName(_fromUtf8("menuData_Format_Convert"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Summary_out = QtGui.QAction(MainWindow)
        self.actionLoad_Summary_out.setObjectName(_fromUtf8("actionLoad_Summary_out"))
        self.actionLoad_NetCDF_File = QtGui.QAction(MainWindow)
        self.actionLoad_NetCDF_File.setObjectName(_fromUtf8("actionLoad_NetCDF_File"))
        self.actionRecent_Files = QtGui.QAction(MainWindow)
        self.actionRecent_Files.setObjectName(_fromUtf8("actionRecent_Files"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.action_out_to_netCDF = QtGui.QAction(MainWindow)
        self.action_out_to_netCDF.setObjectName(_fromUtf8("action_out_to_netCDF"))
        self.action_netCDF_to_out = QtGui.QAction(MainWindow)
        self.action_netCDF_to_out.setObjectName(_fromUtf8("action_netCDF_to_out"))
        self.menuFile.addAction(self.actionLoad_Summary_out)
        self.menuFile.addAction(self.actionLoad_NetCDF_File)
        self.menuFile.addAction(self.actionRecent_Files)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuData_Format_Convert.addAction(self.action_out_to_netCDF)
        self.menuData_Format_Convert.addAction(self.action_netCDF_to_out)
        self.menuTools.addAction(self.menuData_Format_Convert.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "DSSAT Crop Model", None))
        self.label.setText(_translate("MainWindow", "Model Input Information", None))
        self.pushButton.setText(_translate("MainWindow", "Open Original Files", None))
        self.label_3.setText(_translate("MainWindow", "From", None))
        self.label_2.setText(_translate("MainWindow", "year", None))
        self.label_5.setText(_translate("MainWindow", "to", None))
        self.label_6.setText(_translate("MainWindow", "year", None))
        self.label_4.setText(_translate("MainWindow", "Parameter", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "red", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "yellow", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "green", None))
        self.pushButton_3.setText(_translate("MainWindow", "Plot Time Series", None))
	#self.pushButton_3.clicked.connect(out.drawTimeSeries)
	self.pushButton_3.clicked.connect(self.plotTS)

	self.pushButton_4.setText(_translate("MainWindow", "Erase", None))
        self.pushButton_2.setText(_translate("MainWindow", "Display Data", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Yield", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Rain", None))
        self.pushButton_6.setText(_translate("MainWindow", "Save Figure", None))
        self.pushButton_5.setText(_translate("MainWindow", "Erase All", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuData_Format_Convert.setTitle(_translate("MainWindow", "Data Format Convert", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionLoad_Summary_out.setText(_translate("MainWindow", "Load Summary.out", None))
        self.actionLoad_NetCDF_File.setText(_translate("MainWindow", "Load NetCDF File", None))
        self.actionRecent_Files.setText(_translate("MainWindow", "Recent Files", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.action_out_to_netCDF.setText(_translate("MainWindow", ".out to .netCDF", None))
        self.action_netCDF_to_out.setText(_translate("MainWindow", ".netCDF to .out", None))

    def plotTS(self):
	out.drawTimeSeries(inFileName,varName)


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	ex = Ui_MainWindow()
	ex.show()
	sys.exit(app.exec_())