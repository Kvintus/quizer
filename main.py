from PyQt5 import QtCore, QtGui, QtWidgets
import quizer


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(425, 215)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.mainMenu = QtWidgets.QWidget()
        self.mainMenu.setObjectName("mainMenu")
        self.gridLayout = QtWidgets.QGridLayout(self.mainMenu)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.menubtn_Maker = QtWidgets.QPushButton(self.mainMenu)
        self.menubtn_Maker.setObjectName("menubtn_Maker")
        self.gridLayout_3.addWidget(self.menubtn_Maker, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 4, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 0, 1, 1)
        self.menubtn_Quiz = QtWidgets.QPushButton(self.mainMenu)
        self.menubtn_Quiz.setObjectName("menubtn_Quiz")
        self.gridLayout_4.addWidget(self.menubtn_Quiz, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 3, 0, 1, 1)
        self.stackedWidget.addWidget(self.mainMenu)
        self.Make = QtWidgets.QWidget()
        self.Make.setObjectName("Make")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Make)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.questionLbl = QtWidgets.QLabel(self.Make)
        self.questionLbl.setObjectName("questionLbl")
        self.horizontalLayout_3.addWidget(self.questionLbl)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.qstNumLbl = QtWidgets.QLabel(self.Make)
        self.qstNumLbl.setObjectName("qstNumLbl")
        self.horizontalLayout_3.addWidget(self.qstNumLbl)
        self.quesNumLbl = QtWidgets.QLabel(self.Make)
        self.quesNumLbl.setText("")
        self.quesNumLbl.setObjectName("quesNumLbl")
        self.horizontalLayout_3.addWidget(self.quesNumLbl)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.zadOtazka = QtWidgets.QLineEdit(self.Make)
        self.zadOtazka.setObjectName("zadOtazka")
        self.verticalLayout.addWidget(self.zadOtazka)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.r1 = QtWidgets.QRadioButton(self.Make)
        self.r1.setText("")
        self.r1.setObjectName("r1")
        self.gridLayout_2.addWidget(self.r1, 0, 0, 1, 1)
        self.r3 = QtWidgets.QRadioButton(self.Make)
        self.r3.setText("")
        self.r3.setObjectName("r3")
        self.gridLayout_2.addWidget(self.r3, 0, 2, 1, 1)
        self.r4 = QtWidgets.QRadioButton(self.Make)
        self.r4.setText("")
        self.r4.setObjectName("r4")
        self.gridLayout_2.addWidget(self.r4, 1, 2, 1, 1)
        self.r2 = QtWidgets.QRadioButton(self.Make)
        self.r2.setText("")
        self.r2.setObjectName("r2")
        self.gridLayout_2.addWidget(self.r2, 1, 0, 1, 1)
        self.zad4 = QtWidgets.QLineEdit(self.Make)
        self.zad4.setObjectName("zad4")
        self.gridLayout_2.addWidget(self.zad4, 1, 4, 1, 1)
        self.zad2 = QtWidgets.QLineEdit(self.Make)
        self.zad2.setObjectName("zad2")
        self.gridLayout_2.addWidget(self.zad2, 1, 1, 1, 1)
        self.zad3 = QtWidgets.QLineEdit(self.Make)
        self.zad3.setObjectName("zad3")
        self.gridLayout_2.addWidget(self.zad3, 0, 4, 1, 1)
        self.zad1 = QtWidgets.QLineEdit(self.Make)
        self.zad1.setObjectName("zad1")
        self.gridLayout_2.addWidget(self.zad1, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.endBtn = QtWidgets.QPushButton(self.Make)
        self.endBtn.setObjectName("endBtn")
        self.horizontalLayout_2.addWidget(self.endBtn)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.nextBtn = QtWidgets.QPushButton(self.Make)
        self.nextBtn.setObjectName("nextBtn")
        self.horizontalLayout_2.addWidget(self.nextBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.stackedWidget.addWidget(self.Make)
        self.Quiz = QtWidgets.QWidget()
        self.Quiz.setObjectName("Quiz")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Quiz)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.q_quesLbl = QtWidgets.QLabel(self.Quiz)
        self.q_quesLbl.setObjectName("q_quesLbl")
        self.horizontalLayout_9.addWidget(self.q_quesLbl)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.q_quesCnt = QtWidgets.QLabel(self.Quiz)
        self.q_quesCnt.setText("")
        self.q_quesCnt.setObjectName("q_quesCnt")
        self.horizontalLayout_9.addWidget(self.q_quesCnt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.q_mainQues = QtWidgets.QLabel(self.Quiz)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.q_mainQues.setFont(font)
        self.q_mainQues.setObjectName("q_mainQues")
        self.verticalLayout_2.addWidget(self.q_mainQues)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.o1 = QtWidgets.QRadioButton(self.Quiz)
        self.o1.setText("")
        self.o1.setObjectName("o1")
        self.gridLayout_7.addWidget(self.o1, 0, 0, 1, 1)
        self.o3 = QtWidgets.QRadioButton(self.Quiz)
        self.o3.setText("")
        self.o3.setObjectName("o3")
        self.gridLayout_7.addWidget(self.o3, 0, 1, 1, 1)
        self.o4 = QtWidgets.QRadioButton(self.Quiz)
        self.o4.setText("")
        self.o4.setObjectName("o4")
        self.gridLayout_7.addWidget(self.o4, 1, 1, 1, 1)
        self.o2 = QtWidgets.QRadioButton(self.Quiz)
        self.o2.setText("")
        self.o2.setObjectName("o2")
        self.gridLayout_7.addWidget(self.o2, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_7)
        self.progressBar = QtWidgets.QProgressBar(self.Quiz)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.q_endBtn = QtWidgets.QPushButton(self.Quiz)
        self.q_endBtn.setObjectName("q_endBtn")
        self.horizontalLayout_8.addWidget(self.q_endBtn)
        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.q_nextBtn = QtWidgets.QPushButton(self.Quiz)
        self.q_nextBtn.setObjectName("q_nextBtn")
        self.horizontalLayout_8.addWidget(self.q_nextBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.stackedWidget.addWidget(self.Quiz)
        self.vys = QtWidgets.QWidget()
        self.vys.setObjectName("vys")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.vys)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.vysLbl = QtWidgets.QLabel(self.vys)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.vysLbl.setFont(font)
        self.vysLbl.setText("")
        self.vysLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.vysLbl.setObjectName("vysLbl")
        self.verticalLayout_3.addWidget(self.vysLbl)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.anotherBtn = QtWidgets.QPushButton(self.vys)
        self.anotherBtn.setObjectName("anotherBtn")
        self.horizontalLayout_4.addWidget(self.anotherBtn)
        self.doneBtn = QtWidgets.QPushButton(self.vys)
        self.doneBtn.setObjectName("doneBtn")
        self.horizontalLayout_4.addWidget(self.doneBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.stackedWidget.addWidget(self.vys)
        self.horizontalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.quizer = quizer.Quizer_obj()
        self.quesNumLbl.setText(str(1))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Quizer"))
        self.menubtn_Maker.setText(_translate("Form", "Maker"))
        self.menubtn_Quiz.setText(_translate("Form", "Quiz"))
        self.questionLbl.setText(_translate("Form", "Question:"))
        self.qstNumLbl.setText(_translate("Form", "Question num:"))
        self.endBtn.setText(_translate("Form", "End"))
        self.nextBtn.setText(_translate("Form", "Next"))
        self.q_quesLbl.setText(_translate("Form", "Question:"))
        self.q_mainQues.setText(_translate("Form", ""))
        self.q_endBtn.setText(_translate("Form", "End"))
        self.q_nextBtn.setText(_translate("Form", "Next"))
        self.anotherBtn.setText(_translate("Form", "Take another Quiz"))
        self.doneBtn.setText(_translate("Form", "I\'m done for now"))

        # nastavenie buttonov
        self.menubtn_Quiz.clicked.connect(self.chooseInput)
        self.menubtn_Maker.clicked.connect(lambda: self.setPage(1))
        # MakerPage
        self.nextBtn.clicked.connect(self.getInputPage)
        self.endBtn.clicked.connect(self.saveQuiz)
        # QuizPage
        self.q_nextBtn.clicked.connect(self.q_nextBtnClicked)
        #VysPage
        self.doneBtn.clicked.connect(self.endThisSuffering)
        self.anotherBtn.clicked.connect(self.continueThisTorure)

    # universal
    def setPage(self, pageNum):
        self.stackedWidget.setCurrentIndex(pageNum)

    def clearPage(self):
        # clearovanie lineEditov
        self.zadOtazka.setText("")
        self.zad1.setText("")
        self.zad2.setText("")
        self.zad3.setText("")
        self.zad4.setText("")
        # setovanie radio buttonov
        self.r1.setChecked(True)
        self.r2.setChecked(False)
        self.r3.setChecked(False)
        self.r4.setChecked(False)

    # vytavaranie
    def saveQuiz(self):
        if self.isPageFull():
            self.getInputPage()
        if not len(self.quizer.giveLoadedSave()):
            self.setPage(0)
            self.clearPage()
        else:
            buttonReply = QtWidgets.QMessageBox.question(None, 'Save ?', "Do you want to save this quizer file?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if buttonReply == QtWidgets.QMessageBox.Yes:
                self.realSave()
            else:
                self.setPage(0)

            

    def realSave(self):
            file = QtWidgets.QFileDialog.getSaveFileName(
                None, "Save file", "", ".quizer")
            self.quizer.writeToFile(file)
            self.setPage(0)

    def isPageFull(self):
        if self.zadOtazka.text() and self.zad1.text() and self.zad2.text() and self.zad3.text() and self.zad4.text():
            return True
        else:
            return False

    def getInputPage(self):
        page = ["o:" + str(self.zadOtazka.text()), "", "", "", ""]
        if self.r1.isChecked():
            page[1] = "spr:" + self.zad1.text()
            page[2] = self.zad2.text()
            page[3] = self.zad3.text()
            page[4] = self.zad4.text()

        if self.r2.isChecked():
            page[1] = self.zad1.text()
            page[2] = "spr:" + self.zad2.text()
            page[3] = self.zad3.text()
            page[4] = self.zad4.text()

        if self.r3.isChecked():
            page[1] = self.zad1.text()
            page[2] = self.zad2.text()
            page[3] = "spr:" + self.zad3.text()
            page[4] = self.zad4.text()

        if self.r4.isChecked():
            page[1] = self.zad1.text()
            page[2] = self.zad2.text()
            page[3] = self.zad3.text()
            page[4] = "spr:" + self.zad4.text()

        self.quizer.addToList(page)
        self.clearPage()
        self.quesNumLbl.setText(str(int(self.quesNumLbl.text()) + 1))

    # Quizovanie
    def chooseInput(self):
        # dialogove okno
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("You have to pick your quizer file !")
        msg.setWindowTitle("Set file")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        if msg.exec_() == 1024:
            name_of_file = QtWidgets.QFileDialog.getOpenFileName(
                None, 'Open File')
            self.quizer.loadList(name_of_file)

        # pokracovanie
        self.setPage(2)
        self.loadOnToPage()

    def setProgressBarProgress(self, poradie):
        z = self.quizer.giveTotalQuesNum()
        percenta = float(poradie - 1) / z * 100
        self.progressBar.setValue(percenta)

    def loadOnToPage(self):
        chunkedQ = self.quizer.getPageList()

        # zbavenie sa mojho markuupu
        self.q_mainQues.setText(chunkedQ[0][2:]) #zabvenie sa markupu na otazke
        for item in range(len(chunkedQ)):
            if chunkedQ[item][:4] == "spr:":      #ak prve styri charaktery z itemu su 'spr:' tak je to spravne riesenie
                chunkedQ[item] = chunkedQ[item][4:]
                self.quizer.setCurrentAnswer(chunkedQ[item]) #automaticky nastavi aj ako odpoved na tejto strANE

        # loadovanie do radioButtonov
        self.o1.setChecked(True)
        self.o1.setText(chunkedQ[1])
        self.o2.setText(chunkedQ[2])
        self.o3.setText(chunkedQ[3])
        self.o4.setText(chunkedQ[4])
        self.setProgressBarProgress(
            int(self.quizer.giveCurrentPageNum()))  # sets progressbar
        # changes the page number
        self.q_quesCnt.setText(str(self.quizer.giveCurrentPageNum()))


    def chechIfLast(self): 
        if int(self.quizer.giveCurrentPageNum()) == int(self.quizer.giveTotalQuesNum()):    #ze ci tato strana je posledna zo vsetkych
            return True
        else:
            return False

    def findUsersAnswer(self):
        if self.o1.isChecked():
            self.quizer.compareAnswers(self.o1.text())
        if self.o2.isChecked():
            self.quizer.compareAnswers(self.o2.text())
        if self.o3.isChecked():
            self.quizer.compareAnswers(self.o3.text())
        if self.o4.isChecked():
            self.quizer.compareAnswers(self.o4.text())

    def q_nextBtnClicked(self):
        self.findUsersAnswer()
        if self.chechIfLast():
            self.endingScreen()
        else:
            self.loadOnToPage()

    def endingScreen(self):
        self.setPage(3)
        vysledok = self.quizer.giveQuesRightPoint() / self.quizer.giveTotalQuesNum() * 100
        self.vysLbl.setText(str(vysledok) + '%')

    def endThisSuffering(self):
        QtCore.QCoreApplication.instance().quit()

    def continueThisTorure(self):
        self.setPage(0)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
