
'''
>>>>>>>>>>>>>SoundWave, play my favorite song <<<<<<<<<<<<<<

===============My Little Pony, My Little Pony===============
====================Ahh, ahh, ahh, ahhhh====================
=========I used to wonder what friendship could be~=========
===========Until you all shared its magic with me===========
=======================Big adventure~=======================
========================Tons of fun~========================
=====================A beautiful heart~=====================
====================Faithful and strong~====================
=====================Sharing kindness~======================
=====================It's an easy feat~=====================
==============And magic makes it all complete~==============
=================You have my little ponies =================
========Do you know you're all my very best friends~========
'''


import numpy as np
import math
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import sys
import timeit
import os
import webbrowser
import re
from PyQt5 import QtCore, QtGui, uic, QtWidgets

def getDirectory():
    current = str(os.path.abspath(__file__))
    for itera in range(len(current) - 1, 0, -1):
        if current[itera] == '\\':
            dir = current[0: itera]#Get current directory
            return dir

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(584, 549)
        MainWindow.setAcceptDrops(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Generate = QtWidgets.QPushButton(self.centralwidget)
        self.Generate.setGeometry(QtCore.QRect(20, 480, 171, 46))
        self.Generate.setObjectName("Generate")
        self.EnablePlot = QtWidgets.QCheckBox(self.centralwidget)
        self.EnablePlot.setGeometry(QtCore.QRect(40, 20, 132, 29))
        self.EnablePlot.setObjectName("EnablePlot")
        self.enableParameter = QtWidgets.QCheckBox(self.centralwidget)
        self.enableParameter.setEnabled(False)
        self.enableParameter.setGeometry(QtCore.QRect(190, 20, 151, 29))
        self.enableParameter.setObjectName("enableParameter")
        self.enableLinearRegression = QtWidgets.QCheckBox(self.centralwidget)
        self.enableLinearRegression.setEnabled(False)
        self.enableLinearRegression.setGeometry(QtCore.QRect(340, 20, 181, 29))
        self.enableLinearRegression.setObjectName("enableLinearRegression")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setEnabled(True)
        self.toolBox.setGeometry(QtCore.QRect(20, 60, 551, 411))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 551, 321))
        self.page.setObjectName("page")
        self.groupBoxTwo = QtWidgets.QGroupBox(self.page)
        self.groupBoxTwo.setEnabled(False)
        self.groupBoxTwo.setGeometry(QtCore.QRect(10, 120, 531, 211))
        self.groupBoxTwo.setObjectName("groupBoxTwo")
        self.inputY = QtWidgets.QLineEdit(self.groupBoxTwo)
        self.inputY.setEnabled(False)
        self.inputY.setGeometry(QtCore.QRect(10, 30, 491, 31))
        self.inputY.setObjectName("inputY")
        self.yC = QtWidgets.QLineEdit(self.groupBoxTwo)
        self.yC.setEnabled(False)
        self.yC.setGeometry(QtCore.QRect(360, 80, 113, 31))
        self.yC.setObjectName("yC")
        self.yDelta = QtWidgets.QLineEdit(self.groupBoxTwo)
        self.yDelta.setEnabled(False)
        self.yDelta.setGeometry(QtCore.QRect(110, 80, 113, 31))
        self.yDelta.setObjectName("yDelta")
        self.checkCy = QtWidgets.QCheckBox(self.groupBoxTwo)
        self.checkCy.setGeometry(QtCore.QRect(300, 80, 61, 29))
        self.checkCy.setObjectName("checkCy")
        self.checkDeltay = QtWidgets.QCheckBox(self.groupBoxTwo)
        self.checkDeltay.setGeometry(QtCore.QRect(20, 80, 91, 29))
        self.checkDeltay.setObjectName("checkDeltay")
        self.radioOne = QtWidgets.QRadioButton(self.groupBoxTwo)
        self.radioOne.setGeometry(QtCore.QRect(170, 120, 81, 29))
        self.radioOne.setAutoFillBackground(False)
        self.radioOne.setChecked(False)
        self.radioOne.setObjectName("radioOne")
        self.radioThree = QtWidgets.QRadioButton(self.groupBoxTwo)
        self.radioThree.setGeometry(QtCore.QRect(420, 120, 101, 29))
        self.radioThree.setChecked(True)
        self.radioThree.setObjectName("radioThree")
        self.radioTwo = QtWidgets.QRadioButton(self.groupBoxTwo)
        self.radioTwo.setGeometry(QtCore.QRect(290, 120, 101, 29))
        self.radioTwo.setObjectName("radioTwo")
        self.label_4 = QtWidgets.QLabel(self.groupBoxTwo)
        self.label_4.setGeometry(QtCore.QRect(40, 120, 111, 25))
        self.label_4.setObjectName("label_4")
        self.PointColorDecide = QtWidgets.QWidget(self.groupBoxTwo)
        self.PointColorDecide.setGeometry(QtCore.QRect(30, 160, 491, 41))
        self.PointColorDecide.setObjectName("PointColorDecide")
        self.pointTwo = QtWidgets.QRadioButton(self.PointColorDecide)
        self.pointTwo.setGeometry(QtCore.QRect(260, 10, 91, 29))
        self.pointTwo.setChecked(True)
        self.pointTwo.setObjectName("pointTwo")
        self.pointThree = QtWidgets.QRadioButton(self.PointColorDecide)
        self.pointThree.setGeometry(QtCore.QRect(390, 10, 101, 29))
        self.pointThree.setObjectName("pointThree")
        self.label_5 = QtWidgets.QLabel(self.PointColorDecide)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 121, 25))
        self.label_5.setObjectName("label_5")
        self.pointOne = QtWidgets.QRadioButton(self.PointColorDecide)
        self.pointOne.setGeometry(QtCore.QRect(140, 10, 101, 29))
        self.pointOne.setObjectName("pointOne")
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 531, 121))
        self.groupBox.setObjectName("groupBox")
        self.inputX = QtWidgets.QLineEdit(self.groupBox)
        self.inputX.setGeometry(QtCore.QRect(10, 30, 491, 31))
        self.inputX.setObjectName("inputX")
        self.xDelta = QtWidgets.QLineEdit(self.groupBox)
        self.xDelta.setEnabled(False)
        self.xDelta.setGeometry(QtCore.QRect(110, 80, 113, 31))
        self.xDelta.setObjectName("xDelta")
        self.xC = QtWidgets.QLineEdit(self.groupBox)
        self.xC.setEnabled(False)
        self.xC.setGeometry(QtCore.QRect(360, 80, 113, 31))
        self.xC.setObjectName("xC")
        self.checkCx = QtWidgets.QCheckBox(self.groupBox)
        self.checkCx.setGeometry(QtCore.QRect(300, 80, 61, 29))
        self.checkCx.setObjectName("checkCx")
        self.checkDeltax = QtWidgets.QCheckBox(self.groupBox)
        self.checkDeltax.setGeometry(QtCore.QRect(20, 80, 91, 29))
        self.checkDeltax.setObjectName("checkDeltax")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 551, 321))
        self.page_2.setObjectName("page_2")
        self.enableCustom = QtWidgets.QCheckBox(self.page_2)
        self.enableCustom.setEnabled(False)
        self.enableCustom.setGeometry(QtCore.QRect(20, 0, 191, 29))
        self.enableCustom.setObjectName("enableCustom")
        self.customSize = QtWidgets.QGroupBox(self.page_2)
        self.customSize.setEnabled(False)
        self.customSize.setGeometry(QtCore.QRect(10, 30, 541, 71))
        self.customSize.setObjectName("customSize")
        self.xSize = QtWidgets.QLineEdit(self.customSize)
        self.xSize.setGeometry(QtCore.QRect(100, 30, 113, 31))
        self.xSize.setInputMask("")
        self.xSize.setObjectName("xSize")
        self.ySize = QtWidgets.QLineEdit(self.customSize)
        self.ySize.setGeometry(QtCore.QRect(390, 30, 113, 31))
        self.ySize.setObjectName("ySize")
        self.xLengthDis = QtWidgets.QLabel(self.customSize)
        self.xLengthDis.setGeometry(QtCore.QRect(10, 30, 89, 25))
        self.xLengthDis.setObjectName("xLengthDis")
        self.yLengthDis_2 = QtWidgets.QLabel(self.customSize)
        self.yLengthDis_2.setGeometry(QtCore.QRect(310, 30, 89, 25))
        self.yLengthDis_2.setObjectName("yLengthDis_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 100, 251, 191))
        self.groupBox_2.setObjectName("groupBox_2")
        self.xStart = QtWidgets.QLineEdit(self.groupBox_2)
        self.xStart.setGeometry(QtCore.QRect(100, 30, 113, 31))
        self.xStart.setObjectName("xStart")
        self.xEnd = QtWidgets.QLineEdit(self.groupBox_2)
        self.xEnd.setGeometry(QtCore.QRect(100, 70, 113, 31))
        self.xEnd.setObjectName("xEnd")
        self.xDivision = QtWidgets.QLineEdit(self.groupBox_2)
        self.xDivision.setGeometry(QtCore.QRect(100, 110, 113, 31))
        self.xDivision.setObjectName("xDivision")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 30, 89, 25))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 89, 25))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 89, 25))
        self.label_3.setObjectName("label_3")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(20, 150, 89, 25))
        self.label_14.setObjectName("label_14")
        self.xSubstep = QtWidgets.QLineEdit(self.groupBox_2)
        self.xSubstep.setGeometry(QtCore.QRect(100, 150, 113, 31))
        self.xSubstep.setObjectName("xSubstep")
        self.groupBox_3 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setGeometry(QtCore.QRect(280, 100, 271, 191))
        self.groupBox_3.setObjectName("groupBox_3")
        self.yStart = QtWidgets.QLineEdit(self.groupBox_3)
        self.yStart.setGeometry(QtCore.QRect(120, 30, 113, 31))
        self.yStart.setObjectName("yStart")
        self.yEnd = QtWidgets.QLineEdit(self.groupBox_3)
        self.yEnd.setGeometry(QtCore.QRect(120, 70, 113, 31))
        self.yEnd.setObjectName("yEnd")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(40, 30, 89, 25))
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(40, 110, 89, 25))
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(40, 70, 89, 25))
        self.label_12.setObjectName("label_12")
        self.yDivision = QtWidgets.QLineEdit(self.groupBox_3)
        self.yDivision.setGeometry(QtCore.QRect(120, 110, 113, 31))
        self.yDivision.setObjectName("yDivision")
        self.ySubstep = QtWidgets.QLineEdit(self.groupBox_3)
        self.ySubstep.setGeometry(QtCore.QRect(120, 150, 113, 31))
        self.ySubstep.setObjectName("ySubstep")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(40, 150, 89, 25))
        self.label_13.setObjectName("label_13")
        self.Samplex = QtWidgets.QLineEdit(self.page_2)
        self.Samplex.setEnabled(False)
        self.Samplex.setGeometry(QtCore.QRect(220, 300, 113, 31))
        self.Samplex.setText("")
        self.Samplex.setObjectName("Samplex")
        self.Sampley = QtWidgets.QLineEdit(self.page_2)
        self.Sampley.setEnabled(False)
        self.Sampley.setGeometry(QtCore.QRect(410, 300, 113, 31))
        self.Sampley.setText("")
        self.Sampley.setObjectName("Sampley")
        self.enableSamplex = QtWidgets.QCheckBox(self.page_2)
        self.enableSamplex.setEnabled(False)
        self.enableSamplex.setGeometry(QtCore.QRect(10, 300, 201, 29))
        self.enableSamplex.setObjectName("enableSamplex")
        self.toolBox.addItem(self.page_2, "")
        self.shutDown = QtWidgets.QPushButton(self.centralwidget)
        self.shutDown.setGeometry(QtCore.QRect(390, 480, 181, 46))
        self.shutDown.setObjectName("shutDown")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(211, 480, 161, 46))
        self.help.setObjectName("help")
        self.regressValue = QtWidgets.QLineEdit(self.centralwidget)
        self.regressValue.setEnabled(False)
        self.regressValue.setGeometry(QtCore.QRect(530, 20, 41, 31))
        self.regressValue.setInputMask("")
        self.regressValue.setObjectName("regressValue")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setCheckable(False)
        self.actionHelp.setEnabled(True)
        self.actionHelp.setObjectName("actionHelp")
        self.actionDeveloper = QtWidgets.QAction(MainWindow)
        self.actionDeveloper.setObjectName("actionDeveloper")

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.EnablePlot.clicked['bool'].connect(self.groupBoxTwo.setEnabled)
        self.checkCx.clicked['bool'].connect(self.xC.setEnabled)
        self.checkDeltax.clicked['bool'].connect(self.xDelta.setEnabled)
        self.checkDeltay.clicked['bool'].connect(self.yDelta.setEnabled)
        self.checkCy.clicked['bool'].connect(self.yC.setEnabled)
        self.EnablePlot.clicked['bool'].connect(self.enableParameter.setEnabled)
        self.EnablePlot.clicked['bool'].connect(self.enableLinearRegression.setEnabled)
        self.EnablePlot.clicked['bool'].connect(self.enableCustom.setEnabled)
        self.enableCustom.clicked['bool'].connect(self.customSize.setEnabled)
        self.enableCustom.clicked['bool'].connect(self.groupBox_2.setEnabled)
        self.enableCustom.clicked['bool'].connect(self.groupBox_3.setEnabled)
        self.enableSamplex.clicked['bool'].connect(self.Samplex.setEnabled)
        self.enableSamplex.clicked['bool'].connect(self.Sampley.setEnabled)
        self.EnablePlot.clicked['bool'].connect(self.enableSamplex.setEnabled)
        self.enableLinearRegression.clicked['bool'].connect(self.regressValue.setEnabled)
        self.EnablePlot.clicked['bool'].connect(self.groupBoxTwo.setEnabled)
        self.EnablePlot.clicked['bool'].connect(self.inputY.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sunburst Leisure"))
        self.Generate.setText(_translate("MainWindow", "Generate"))
        self.EnablePlot.setText(_translate("MainWindow", "2D Array"))
        self.enableParameter.setText(_translate("MainWindow", "Parameter"))
        self.enableLinearRegression.setText(_translate("MainWindow", "Regress  Value"))
        self.groupBoxTwo.setTitle(_translate("MainWindow", "yValue"))
        self.yC.setText(_translate("MainWindow", "1.46"))
        self.yDelta.setText(_translate("MainWindow", "0.01"))
        self.checkCy.setText(_translate("MainWindow", "C"))
        self.checkDeltay.setText(_translate("MainWindow", "Delta"))
        self.radioOne.setText(_translate("MainWindow", "Red"))
        self.radioThree.setText(_translate("MainWindow", "Black"))
        self.radioTwo.setText(_translate("MainWindow", "Blue"))
        self.label_4.setText(_translate("MainWindow", "GridColor:"))
        self.pointTwo.setText(_translate("MainWindow", "Cross"))
        self.pointThree.setText(_translate("MainWindow", "Plus"))
        self.label_5.setText(_translate("MainWindow", "PointType:"))
        self.pointOne.setText(_translate("MainWindow", "Point"))
        self.groupBox.setTitle(_translate("MainWindow", "xValue"))
        self.xDelta.setText(_translate("MainWindow", "0.01"))
        self.xC.setText(_translate("MainWindow", "1.46"))
        self.checkCx.setText(_translate("MainWindow", "C"))
        self.checkDeltax.setText(_translate("MainWindow", "Delta"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Base"))
        self.enableCustom.setText(_translate("MainWindow", "CustomPlotSize"))
        self.customSize.setTitle(_translate("MainWindow", "Gernal"))
        self.xSize.setText(_translate("MainWindow", "7"))
        self.ySize.setText(_translate("MainWindow", "7"))
        self.xLengthDis.setText(_translate("MainWindow", "Length:"))
        self.yLengthDis_2.setText(_translate("MainWindow", "Height:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "xTicks"))
        self.xStart.setText(_translate("MainWindow", "0"))
        self.xEnd.setText(_translate("MainWindow", "10"))
        self.xDivision.setText(_translate("MainWindow", "11"))
        self.label.setText(_translate("MainWindow", "Start"))
        self.label_2.setText(_translate("MainWindow", "End"))
        self.label_3.setText(_translate("MainWindow", "Division"))
        self.label_14.setText(_translate("MainWindow", "Substep"))
        self.xSubstep.setText(_translate("MainWindow", "10"))
        self.groupBox_3.setTitle(_translate("MainWindow", "yTicks"))
        self.yStart.setText(_translate("MainWindow", "0"))
        self.yEnd.setText(_translate("MainWindow", "10"))
        self.label_11.setText(_translate("MainWindow", "Start"))
        self.label_10.setText(_translate("MainWindow", "Division"))
        self.label_12.setText(_translate("MainWindow", "End"))
        self.yDivision.setText(_translate("MainWindow", "11"))
        self.ySubstep.setText(_translate("MainWindow", "10"))
        self.label_13.setText(_translate("MainWindow", "Substep"))
        self.enableSamplex.setText(_translate("MainWindow", "Sample"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Advanced"))
        self.shutDown.setText(_translate("MainWindow", "ShutDown"))
        self.help.setText(_translate("MainWindow", "Help"))
        self.regressValue.setText(_translate("MainWindow", "1"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setToolTip(_translate("MainWindow", "Show Manual"))
        self.actionHelp.setStatusTip(_translate("MainWindow", "Show Manual"))
        self.actionDeveloper.setText(_translate("MainWindow", "Developer"))

class phylist():
    def __init__(self, value, delta = 0.01, C = 1.46):
        self.value = value
        self.delta = delta
        self.C = C
        self.summing = sum(self.value)
        self.squre = self.singleSqure(self.value)
        self.average = self.summing / len(self.value)
        self.uncerA = self.getUncerA()
        self.uncerB = self.getUncerB()
        self.uncertainty = self.getUncertainty()
        self.reTolera = self.getUncertainty() / self.average  #percentage
        self.ln = self.toln(self.value)
        self.biggest = np.max(self.value)
        self.smallest = np.min(self.value)
        self.distance = self.biggest - self.smallest
        self.maxRange = self.toEven(math.ceil(self.biggest + self.distance / 20))
        self.minRange = 0 if (math.floor(self.smallest - self.distance / 20) < 0) else math.floor(self.smallest - self.distance / 20)
        self.tickDistance = self.tickDistan(self.value)
    
    def getUncerA(self):
        return self.evalUncerA(self.value, self.average)
    def getUncerB(self):
        return self.delta / self.C
    def getUncertainty(self):
        return math.sqrt(self.getUncerA() ** 2 + self.getUncerB() ** 2)
    def evalUncerA(self, inList, average):
        for itera in range(len(inList)):
            squrMinu = (inList[itera] - average) ** 2
        squrMinu /= ((len(inList) - 1) * len(inList))
        return np.sqrt(squrMinu)
    def singleSqure(self, inList): #return the sum of all the elements' squre
        sumup = 0
        for itera in range(len(inList)):
            sumup += inList[itera] ** 2 
        return sumup
    def toln(self, inlist):
        outlist = []
        for itera in range(len(inlist)):
            if inlist[itera] <= 0:
                outlist.append(0)
            else:
                temp = math.log(inlist[itera], math.e)
                outlist.append(temp)
        return outlist
    def toEven(self, inNum):
        if inNum % 2:#=1, odd
            return inNum + 1
        else:
            return inNum
    def tickDistan(self, inlist):
        if self.maxRange <= 10:
            return self.toEven(self.maxRange)
        elif 10 < self.maxRange <= 20:
            return self.toEven(math.ceil(self.maxRange / 2))
        elif 20 < self.maxRange <= 50:
            return self.toEven(math.ceil(self.maxRange / 5))
        elif 50 < self.maxRange <= 100:
            return self.toEven(math.ceil(self.maxRange / 10))
        elif 100 < self.maxRange <= 200:
            return self.toEven(math.ceil(self.maxRange / 20))
        elif 200 < self.maxRange <= 500:
            return self.toEven(math.ceil(self.maxRange / 50))
        return 0


class PhysData():
    def __init__(self):
        self.Plot = True
        self.orthPlot = False
        self.linearRegression = False
        self.sample = False
        self.linOpacity = 0.5
        self.parameter = False
        self.cusSize = False
        self.size = 7
        self.ySize = self.size
        self.title = ''
        self.xlabel = ''
        self.ylabel = ''

    def OneDataCal(self, inlist, inC = 1.46, inDelta = 0.02):
        inlist = phylist(inlist)
        inlist.delta = inDelta; inlist.C = inC
        with open('data.txt', 'a+') as file :
            file.truncate(0)
            file.write('C:      ' + str(inlist.C) + '\n')
            file.write('Delta:  ' + str(inlist.delta) + '\n')
            file.write('Summing:' + str(inlist.summing) + '\n')
            file.write('Average:' + str(inlist.average) + '\n')
            file.write('S_A:    ' + str(inlist.getUncerA()) + '\n')
            file.write('U_B:    ' + str(inlist.getUncerB()) + '\n')
            file.write('U_x:    ' + str(inlist.getUncertainty()) + '\n')
            file.write('E_x:    %' + str(inlist.reTolera * 100) + '\n')
        os.startfile(r'data.txt')

#===================================================================
    def PhyExPlot(self, inX, inY, xDelta, xC, yDelta, yC, regValue):
        '''Produce a 2-d plot of the input data, avilable to aclculate
        linear regression and plot it'''
        title = self.title; alp = self.linOpacity
        size = self.size; ySize = self.ySize
        fontSize = self.size * 2

        xValue = phylist(inX); xValue.delta = xDelta; xValue.C = xC
        yValue = phylist(inY); yValue.delta = yDelta; yValue.C = yC
        if self.linearRegression:
            #---------------------LinearRegression----------------------------
            slope, intercept = np.polyfit(xValue.value, yValue.value, 1)
            gamma = (np.dot(xValue.value, yValue.value) / len(xValue.value) - xValue.average * yValue.average) /\
                np.sqrt( (xValue.squre / len(xValue.value) - xValue.average ** 2) *\
                (yValue.squre / len(yValue.value) - yValue.average ** 2) )
            sample = np.linspace(np.min(xValue.value), np.max(xValue.value), 50)
            regress = np.poly1d(np.polyfit(xValue.value, yValue.value, regValue))
            #------------------------------------------------------------------
        
        plt.style.use(u'ggplot')
        if self.parameter:
            plt.figure(figsize = (size + size / 2, ySize))
            ax = plt.axes([0.05, 0.05, 0.55, 0.9])
        else:
            plt.figure(figsize = (size, ySize))
            ax = plt.axes([0.075, 0.075, 0.85, 0.85])
        
        ax.plot(xValue.value, yValue.value, pointColor + pointType,\
            markersize = size * 1.5, markeredgewidth  = size / 4)#The most important part, plotting points

        if self.sample: #show sample
            simx, simy, intx = self.PointSampleLine( [xValue.value[SampleOne - 1], xValue.value[SampleTwo - 1]], \
                [yValue.value[SampleOne - 1], yValue.value[SampleTwo - 1]] )
            ax.plot(simx, simy);ax.text(intx, -1.25, str(intx)[0:7], fontsize = 2 * size)

        
        if self.linearRegression:#show Regression
            ax.plot(sample, regress(sample))
        if not self.cusSize: #default ticks and lims
            ax.xaxis.set_major_locator(plt.MultipleLocator(1.0 if xValue.maxRange < 10 else 10))
            ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1 if xValue.maxRange < 10 else 1))
            ax.yaxis.set_major_locator(plt.MultipleLocator(1.0 if yValue.maxRange < 10 else 10))
            ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1 if yValue.maxRange < 10 else 1))
            ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color = gridColor, alpha = alp)
            ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color = gridColor, alpha = alp)
            ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color = gridColor, alpha = alp)
            ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color = gridColor, alpha = alp)
            ax.set_xlim(0, xValue.maxRange); ax.set_ylim(0, yValue.maxRange)# Set Limits
            plt.xticks(np.linspace(0, xValue.maxRange, xValue.tickDistance + 1), \
                fontsize = 2 * size)
            plt.yticks(np.linspace(0, yValue.maxRange, yValue.tickDistance), \
                fontsize = 2 * size)
        elif self.cusSize: #custom ticks and lims
            ax.xaxis.set_major_locator(plt.MultipleLocator((xEnd - xStart) / xDivision))
            ax.xaxis.set_minor_locator(plt.MultipleLocator( (xEnd - xStart) / ((xDivision - 1) * xSubstep) ))
            ax.yaxis.set_major_locator(plt.MultipleLocator((yEnd - yStart) / yDivision))
            ax.yaxis.set_minor_locator(plt.MultipleLocator( (yEnd - yStart) / ((yDivision - 1) * ySubstep) ))
            ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color = gridColor, alpha = alp)
            ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color = gridColor, alpha = alp)
            ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color = gridColor, alpha = alp)
            ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color = gridColor, alpha = alp)
            ax.set_xlim(xStart, xEnd); ax.set_ylim(yStart, yEnd)# Set Limits
            plt.xticks(np.linspace(xStart, xEnd, xDivision), \
                fontsize = 2 * size)
            plt.yticks(np.linspace(yStart, yEnd, yDivision), \
                fontsize = 2 * size)
        plt.xlabel(self.xlabel, fontsize = 10)
        plt.ylabel(self.ylabel, fontsize = 10)
        plt.title(title, fontsize = 20)

        if self.parameter:
            space = fontSize / 3.5
            bx = plt.axes([0.65, 0.05, 0.3, 0.9])
            bx.set_xlim(0, 25);bx.set_ylim(0, 90); pos = 85

            bx.text(1, pos, '----------------x----------------', fontsize = fontSize); pos -= space
            bx.text(1, pos, '$Aver$='+str(xValue.average), fontsize = fontSize); pos -= space
            bx.text(1, pos, '$S_A$='+str(xValue.uncerA), fontsize = fontSize); pos -= space
            bx.text(1, pos, '$U_b$='+str(xValue.uncerB), fontsize = fontSize); pos -= space
            bx.text(1, pos, '$U_x$='+str(xValue.uncertainty), fontsize = fontSize); pos -= space
            bx.text(1, pos, '----------------y----------------', fontsize = fontSize); pos -= space
            bx.text(1, pos, '$Aver$='+str(yValue.average), fontsize = fontSize); pos -= space
            bx.text(1, pos, '$S_A$='+str(yValue.uncerA), fontsize = fontSize); pos -= space
            bx.text(1, pos, '$U_b$='+str(yValue.uncerB), fontsize = fontSize); pos -= space
            bx.text(1, pos, '$U_x$='+str(yValue.uncertainty), fontsize = fontSize); pos -= space
            if self.linearRegression:
                if regValue > 1:
                    para = np.polyfit(xValue.value, yValue.value, regValue)

                    regSpace = 40 / len(para)
                    bx.text(1, pos, '------------Regression------------', fontsize = fontSize); pos -= space
                    for num in para:
                        bx.text(1, pos, 'para:'+str(num),  fontsize = fontSize); pos -= regSpace

                else:
                    bx.text(1, pos, '--------LinearRegression---------', fontsize = fontSize); pos -= 5
                    bx.text(1, pos, '$Slope$='+str(slope), fontsize = fontSize); pos -= 5
                    bx.text(1, pos, '$intercept$='+str(intercept), fontsize = fontSize); pos -= 5
                    bx.text(1, pos, '$\gamma$='+str(gamma), fontsize = fontSize); pos -= 5
                plt.xticks([]);plt.yticks([]) #display parameters in plot

        if self.orthPlot:# Tiny plot
            orthPlotRange = max(xValue.maxRange, yValue.maxRange)           
            orth = plt.axes([0.7, 0, 0.3, 0.3], \
                alpha = 0.5)
            plt.alpha = 0.5
            print(plt.getp(orth.patch))
            orth.set_xlim(0, orthPlotRange); orth.set_ylim(0, orthPlotRange)
            orth.xaxis.set_major_locator(plt.MultipleLocator(1.0 if xValue.maxRange < 10 else 10))
            orth.xaxis.set_minor_locator(plt.MultipleLocator(0.1 if xValue.maxRange < 10 else 1))
            orth.yaxis.set_major_locator(plt.MultipleLocator(1.0 if yValue.maxRange < 10 else 10))
            orth.yaxis.set_minor_locator(plt.MultipleLocator(0.1 if yValue.maxRange < 10 else 1))
            orth.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color = alp)
            orth.grid(which='minor', axis='x', linewidth=0.0625, linestyle='-', color = alp)
            orth.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color = alp)
            orth.grid(which='minor', axis='y', linewidth=0.0625, linestyle='-', color = alp)
            orth.plot(xValue.value, yValue.value, 'rx',\
                markersize = size / 2, markeredgewidth  = size / 10)
            plt.xticks([]); plt.yticks([])
            
        plt.show()

#===================================================================
    def PointSampleLine(self, inlistx, inlisty, \
        inlistz = [0, 0], enable = False, sort = False, intcepx = True):
        '''This function mainly returns value for 2-d data, 
        and plot a plot for 3-d data, enable decides whether to plot,
        sort decides whether to sort the input array'''
        size = 10
        grid = True

        if inlistz == [0, 0]:
            if sort:
                inlistx.sort()
                inlisty.sort()
        slope = (inlisty[len(inlisty) - 1] - inlisty[0]) / \
            (inlistx[len(inlistx) - 1] - inlistx[0])
        intercept = inlisty[0] - slope * inlistx[0]
        sampleRatex = (inlistx[len(inlistx) - 1] - inlistx[0]) / 5 
        samplex = [( - sampleRatex),\
            (inlistx[len(inlistx) - 1] + sampleRatex)]
        sampley = [( - sampleRatex) * slope + intercept, \
            (inlistx[len(inlistx) - 1] + sampleRatex) * slope + intercept];
        interceptx = - intercept / slope
        if intcepx:
            interceptReturn = interceptx
        else:
            interceptReturn = intercept

        if enable:
            ax = plt.axes([0.05, 0.05, 0.9, 0.9])
            ax.plot(inlistx, inlisty, 'rx', markersize = size, markeredgewidth  = size / 5)
            ax.plot(samplex, sampley)
            if grid:
                ax.xaxis.set_major_locator(plt.MultipleLocator(1.0))
                ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
                ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))
                ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
                ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
                ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
                ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
                ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
            plt.show()
        return samplex, sampley, interceptReturn
        if False:
            if sort:
                inlistx.sort()
                inlisty.sort()
                inlistz.sort()
            ax = plt.axes([0.05, 0.05, 0.9, 0.9], projection = '3d')
            surface = ax.scatter(inlistx, inlisty, inlistz)
            plt.show()

    def UiRrial(self):
        #qtCreatorFile = getDirectory() + '\\PhyData.ui' 
        #Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
        class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
            def __init__(self):
                QtWidgets.QMainWindow.__init__(self)
                Ui_MainWindow.__init__(self)
                self.setupUi(self)
                self.Generate.clicked.connect(self.onClick)
                self.help.clicked.connect(self.Help)
                self.shutDown.clicked.connect(self.ShutDown)
                self.groupBoxTwo.setEnabled(True if self.EnablePlot.isChecked() else False)
            

            def closeEvent(self, event):
                reply = QtWidgets.QMessageBox.question(self, 'Derpy says', 'You sure quit?',\
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
                if reply == QtWidgets.QMessageBox.Yes:
                    event.ignore()
                else:
                    event.accept()
            def ShutDown(self):
                os.system('shutdown -s -t 1')  
            def Help(self):
                webbrowser.open(r'https://amarthgul.gitbooks.io/datahandlermanual/content/')
            def onClick(self):
                regValue = 1
                xValue = str(self.inputX.text())
                regex = '^(\s*\d+\.?\d*\s*,)*(\s*\d+\.?\d*\s*)$'
                if not re.match(regex, xValue):
                    QtWidgets.QMessageBox.critical(self,"Critical", \
                        self.tr("Something wrong with xValue"))
                    return False
                xValue = phylist( eval('([' + str(xValue) + '])') )
                xValue.C = 1.46; xValue.delta = 0.01              
                data = PhysData()
                if self.EnablePlot.isChecked():#2D Array
                    data.Plot = True
                    yValue = str(self.inputY.text())
                    regex = '^(\s*\d+\.?\d*\s*,)*(\s*\d+\.?\d*\s*)$'
                    if not re.match(regex, yValue):
                        QtWidgets.QMessageBox.critical(self,"Critical", \
                            self.tr("Something wrong with yValue"))
                        return False
                    yValue = phylist( eval('([' + str(yValue) + '])') )
                    yValue.C = 1.46; yValue.delta = 0.01
                    if self.enableCustom.isChecked():
                        data.cusSize = True
                        global xStart; global xEnd; global xDivision
                        global yStart; global yEnd; global yDivision
                        global xSubstep; global ySubstep
                        global SampleOne; global SampleTwo
                        global gridColor; global pointColor; global pointType
                        temp = str(self.xSize.text())
                        if not re.fullmatch(r'\d+(\.\d*)?', temp): 
                            QtWidgets.QMessageBox.critical(self,"Critical", self.tr("Something wrong with your input"))
                            return False
                        data.size = float(temp);
                        #============================================= 
                        temp = str(self.ySize.text())
                        if not re.fullmatch(r'\d+(\.\d*)?', temp): 
                            QtWidgets.QMessageBox.critical(self,"Critical", self.tr("Something wrong with your input"))
                            return False
                        data.ySize = float(temp)
                        #=============================================
                        temp = str(self.xStart.text())
                        if not re.fullmatch(r'\d+(\.\d*)?', temp): 
                            QtWidgets.QMessageBox.critical(self,"Critical", self.tr("Something wrong with xStart"))
                            return False
                        xStart = float(temp); 
                        #=============================================
                        temp = str(self.yStart.text())
                        if not re.fullmatch(r'\d+(\.\d*)?', temp): 
                            QtWidgets.QMessageBox.critical(self,"Critical", self.tr("Something wrong with yStart"))
                            return False
                        yStart = float(temp)
                        #=============================================
                        temp = str(self.xEnd.text())
                        if not re.fullmatch(r'\d+(\.\d*)?', temp): 
                            QtWidgets.QMessageBox.critical(self,"Critical", self.tr("Something wrong with xEnd"))
                            return False
                        xEnd = float(temp); 
                        #=============================================
                        temp = str(self.yEnd.text())
                        if not re.fullmatch(r'\d+(\.\d*)?', temp): 
                            QtWidgets.QMessageBox.critical(self,"Critical", self.tr("Something wrong with yEnd"))
                            return False
                        yEnd = float(temp)
                        #=============================================
                        temp = str(self.xDivision.text())
                        if not re.fullmatch(r'\d+', temp): 
                            QtWidgets.QMessageBox.critical(self,"ValueError", self.tr("xDivision must be integr"))
                            return False
                        xDivision = float(temp); 
                        #=============================================
                        temp = str(self.yDivision.text())
                        if not re.fullmatch(r'\d+', temp): 
                            QtWidgets.QMessageBox.critical(self,"ValueError", self.tr("yDivision must be integr"))
                            return False
                        yDivision = float(temp)
                        #=============================================
                        temp = str(self.xSubstep.text())
                        if not re.fullmatch(r'\d+', temp): 
                            QtWidgets.QMessageBox.critical(self,"ValueError", self.tr("xSubsteps must be integr"))
                            return False
                        xSubstep = float(temp); 
                        #=============================================
                        temp = str(self.ySubstep.text())
                        if not re.fullmatch(r'\d+', temp): 
                            QtWidgets.QMessageBox.critical(self,"ValueError", self.tr("ySubsteps must be integr"))
                            return False
                        ySubstep = float(temp)
                
                if self.enableParameter.isChecked():#Display Parameter
                    data.parameter = True
                if self.enableLinearRegression.isChecked():#LinearRegression
                    data.linearRegression = True
                    temp = self.regressValue.text()
                    if not re.fullmatch(r'\d+?', temp):
                        QtWidgets.QMessageBox.critical(self,"ValueError", self.tr("Regression time must be digit"))
                        return False
                    regValue = float(temp)
                    regValue = math.floor(regValue)
                    if regValue > 15:
                        QtWidgets.QMessageBox.critical(self,"ValueError", self.tr("Regression time too large"))
                        return False

                if self.enableSamplex.isChecked():#LinearRegression
                    data.sample = True;
                    temp = str(self.Samplex.text())
                    if not re.fullmatch(r'\d+?', temp):
                        QtWidgets.QMessageBox.critical(self,"ValueError", self.tr("Samplex must be digit"))
                        return False 
                    SampleOne = int( temp )
                    temp = str(self.Sampley.text())
                    if not re.fullmatch(r'\d+?', temp):
                        QtWidgets.QMessageBox.critical(self,"ValueError", self.tr("Sampley must be digit"))
                        return False 
                    SampleTwo = int( self.Sampley.text() )
                    if SampleOne > len(xValue.value) or SampleTwo > len(xValue.value) or SampleOne >= SampleTwo:
                        QtWidgets.QMessageBox.critical(self,"RangeError", self.tr("Sample out of range"))
                        return False
                    
                if self.checkDeltax.isChecked():#X's parameters
                    temp = str(self.xDelta.text())
                    if not re.fullmatch(r'\d+(\.\d*)?', temp):
                        QtWidgets.QMessageBox.critical(self,"ValueError", self.tr("xDelta must be digit"))
                        return False 
                    xValue.delta = float(temp)
                if self.checkCx.isChecked():
                    temp = str(self.xC.text())
                    if not re.fullmatch(r'\d+(\.\d*)?', temp):
                        QtWidgets.QMessageBox.critical(self,"ValueError", self.tr("xC must be digit"))
                        return False 
                    xValue.C = float(temp)
                
                if self.radioOne.isChecked():
                    gridColor = 'red'; pointColor = 'k'
                if self.radioTwo.isChecked():
                    gridColor = 'blue'; pointColor = 'r'
                if self.radioThree.isChecked():
                    gridColor = 'black'; pointColor = 'r'
                if self.pointOne.isChecked():
                    pointType = '.'
                if self.pointTwo.isChecked():
                    pointType = 'x'
                if self.pointThree.isChecked():
                    pointType = '+'
                if self.EnablePlot.isChecked():#if Y is enabled
                    if self.checkDeltay.isChecked():
                        temp = str(self.yDelta.text())
                        if not re.fullmatch(r'\d+(\.\d*)?', temp):
                            QtWidgets.QMessageBox.critical(self,"ValueError", self.tr("yDelta must be digit"))
                            return False
                        yValue.delta = float(temp)
                    if self.checkCy.isChecked():
                        temp = str(self.yC.text())
                        if not re.fullmatch(r'\d+(\.\d*)?', temp):
                            QtWidgets.QMessageBox.critical(self,"ValueError", self.tr("yC must be digit"))
                            return False
                        yValue.C = float(temp)
                    '''======================================='''
                    #=============================================
                    data.PhyExPlot(xValue.value, yValue.value, xValue.delta,\
                        xValue.C, yValue.delta, yValue.C, regValue = regValue)#Plotting
                else:
                    data.OneDataCal(xValue.value, xValue.C, xValue.delta)

        if True:#display the window
            app = QtWidgets.QApplication(sys.argv)
            window = MyApp()
            window.show()
            sys.exit(app.exec_())
      
    def timeConsume(self):
        ini = timeit.default_timer()
        while True:
            fin = timeit.default_timer()
            if(fin - ini > 0.1):
                break

def showWarn():

    class Ui_RaiseError(object):
        def setupUi(self, RaiseError):
            RaiseError.setObjectName("RaiseError")
            RaiseError.resize(452, 126)
            self.centralwidget = QtWidgets.QWidget(RaiseError)
            self.centralwidget.setObjectName("centralwidget")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(150, 10, 141, 25))
            self.label.setLineWidth(1)
            self.label.setTextFormat(QtCore.Qt.AutoText)
            self.label.setOpenExternalLinks(False)
            self.label.setObjectName("label")
            self.warnHelp = QtWidgets.QPushButton(self.centralwidget)
            self.warnHelp.setGeometry(QtCore.QRect(30, 50, 181, 46))
            self.warnHelp.setObjectName("warnHelp")
            self.warnShutDown = QtWidgets.QPushButton(self.centralwidget)
            self.warnShutDown.setGeometry(QtCore.QRect(240, 50, 181, 46))
            self.warnShutDown.setObjectName("warnShutDown")
            RaiseError.setCentralWidget(self.centralwidget)

            self.retranslateUi(RaiseError)
            QtCore.QMetaObject.connectSlotsByName(RaiseError)

        def retranslateUi(self, RaiseError):
            _translate = QtCore.QCoreApplication.translate
            RaiseError.setWindowTitle(_translate("RaiseError", "StarLight Warning"))
            self.label.setText(_translate("RaiseError", "Unknow Error!"))
            self.warnHelp.setText(_translate("RaiseError", "Help"))
            self.warnShutDown.setText(_translate("RaiseError", "ShutDown"))

    class WarningWindow(QtWidgets.QMainWindow, Ui_RaiseError):
        def __init__(self):
            QtWidgets.QMainWindow.__init__(self)
            Ui_RaiseError.__init__(self)
            self.setupUi(self)
            self.warnHelp.clicked.connect(self.warn_help)
            self.warnShutDown.clicked.connect(self.warn_ShutDown)

        def warn_ShutDown(self):
            os.system('shutdown -s -t 1') 
        def warn_help(self):
            webbrowser.open(r'https://amarthgul.gitbooks.io/datahandlermanual/content/')
    
    app = QtWidgets.QApplication(sys.argv)
    widget = WarningWindow()  
    widget.show()             
    sys.exit(app.exec_())     

def Main():
    try:
        #start = timeit.default_timer()
        #-----------------------------------------------------  
        phy = PhysData()
        phy.UiRrial()
        #-----------------------------------------------------
        #end = timeit.default_timer()
        #total = end - start #print('Time costed:',total)
    except (ValueError, AttributeError, SyntaxError, ZeroDivisionError) as err:
        showWarn()
    finally:
        pass
        #print('=========================================End========================================')

if __name__ == '__main__':
    Main() 

