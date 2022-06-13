
import sys
import qdarkstyle
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from SQLer import *
from PyQt5.QtWidgets import *
from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class LoginWindow(QWidget):
    loadInfoSig=pyqtSignal(str,str)
    # loginSig=pyqtSignal()
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.initUI()
        self.setWindowTitle("Login")
    def initUI(self):
        self.welcomeLabel=QLabel("Welcome!")
        self.userLabel=QLabel("User:",self)
        self.passwordLabel=QLabel("Password",self)
        self.userText=QLineEdit(self)
        self.passwordText=QLineEdit(self)
        self.loginButton=QPushButton("Login",self)
        self.loginButton.clicked.connect(self.login)
        self.grid=QGridLayout()
        self.grid.addWidget(self.welcomeLabel,0,0)
        self.grid.addWidget(self.userLabel,1,0)
        self.grid.addWidget(self.userText,1,1)
        self.grid.addWidget(self.passwordLabel, 2, 0)
        self.grid.addWidget(self.passwordText, 2, 1)
        self.grid.addWidget(self.loginButton, 3, 2)
        self.setLayout(self.grid)
    def login(self):
        self.loadInfoSig.emit(self.userText.text(),self.passwordText.text())
    def showConnectError(self):
        QMessageBox.information(self, "Connect Error", "Fail to connect the server, check your Server and Internet", QMessageBox.Ok)
    def showLoginError(self):
        QMessageBox.information(self, "Login Error", "Fail to login, check your ID and password as well as the Internet connection", QMessageBox.Ok)
class MainWindow(QWidget):
    addManager_addSignal=pyqtSignal(str,str,str,str)
    addManager_delSignal=pyqtSignal(str)
    addRegion_addSignal=pyqtSignal(str,str,str)
    addRegion_delSignal=pyqtSignal(str)
    assignWorkSignal=pyqtSignal(str,str)
    substituteWorkSignal=pyqtSignal(str,str,str)
    revokeWorkSignal=pyqtSignal(str,str)
    newRoot_addSignal=pyqtSignal(str,str,str,str)
    newRoot_delSignal=pyqtSignal(str,str)
    newSpecies_addSignal=pyqtSignal(str,str,str,str)
    numberDist_speciesSignal=pyqtSignal(str)
    numberDist_genusSignal = pyqtSignal(str)
    numberDist_familySignal = pyqtSignal(str)
    heightDist_heightSignal =pyqtSignal(str)
    heightDist_numberSignal=pyqtSignal(str)
    inq_familySignal=pyqtSignal(str)
    inq_genusSignal=pyqtSignal(str)
    inq_speciesSignal=pyqtSignal(str)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.setWindowTitle("CPMS")
        self.funcTable={
            "Number Distribution":0,
            "Height Distribution":1,
            "Add Manager":2,
            "Add Region":3,
            "Arrange Work":4,
            "New Root":5,
            "New Species":6,
            "Inquiry":7
        }
        self.show()
    def initUI(self):
        self.wholeLayout=QHBoxLayout()
        self.splitter=QSplitter(Qt.Horizontal)
        self.initFunctionTree()
        # splitter.addWidget()
        self.splitter.addWidget(self.functionTree)
        self.initHostPart()
        self.splitter.addWidget(self.butler)
        self.wholeLayout.addWidget(self.splitter)
        self.setLayout(self.wholeLayout)

    def initHostPart(self):#整个右边界面
        self.butler=QStackedWidget()

        self.container_heightDist=QWidget()
        self.container_numberDist=QWidget()
        self.container_addManager=QWidget()
        self.container_addRegion=QWidget()
        self.container_arrangeWork=QWidget()
        self.container_newRoot=QWidget()
        self.container_newSpecies=QWidget()
        self.container_inquiry=QWidget()
        self.build_numberDist()#区域中植物数量的分布查询
        self.build_heightDist()#某种类植物的区域高度
        self.build_addManager()#整个添加人员功能界面生成
        self.build_addRegion()#整个地区管理模块
        self.build_arrangeWork()#分配管理
        self.build_newRoot()#新植株管理
        self.build_newSpecies()#新物种发现
        self.build_inquiry()#查询物种信息
        self.container_testone=QWidget()
        self.container_testtwo=QWidget()

        testLaytou1=QVBoxLayout()
        testLaytou2=QVBoxLayout()
        testButton1=QPushButton("Test1")
        testButton2=QPushButton("Test2")
        testLaytou1.addWidget(testButton1)
        testLaytou2.addWidget(testButton2)

        self.container_testone.setLayout(testLaytou1)
        self.container_testtwo.setLayout(testLaytou2)
        # self.butler.addWidget(self.container_testone)
        self.butler.addWidget(self.container_numberDist)
        self.butler.addWidget(self.container_heightDist)
        self.butler.addWidget(self.container_addManager)
        self.butler.addWidget(self.container_addRegion)
        self.butler.addWidget(self.container_arrangeWork)
        self.butler.addWidget(self.container_newRoot)
        self.butler.addWidget(self.container_newSpecies)
        self.butler.addWidget(self.container_inquiry)
        self.butler.setCurrentIndex(0)

    def build_inquiry(self):
        self.frame_inquiry=QFrame()

        self.frame_inquiry.setFrameShape(QFrame.StyledPanel)

        # self.operatePart_numberDist = QFrame()
        '''
        fill two parts
        '''
        # select part
        print("echo2")
        self.familyLabel_inq=QLabel("Family:")
        self.genusLabel_inq=QLabel("Genus:")
        self.speciesLabel_inq=QLabel("Species:")
        self.despLabel_inq=QLabel("Description:")
        self.familyCombox_inq=QComboBox()
        self.genusCombox_inq=QComboBox()
        self.speciesCombox_inq=QComboBox()
        self.despInfo_inq=QTextEdit()
        self.getDespButton_inq=QPushButton("Search")
        print("echo3")
        self.inquiryLayout=QGridLayout()
        self.inquiryLayout.addWidget(self.familyLabel_inq,0,0)
        self.inquiryLayout.addWidget(self.genusLabel_inq,1,0)
        self.inquiryLayout.addWidget(self.speciesLabel_inq,2,0)
        self.inquiryLayout.addWidget(self.despLabel_inq,3,0)


        self.inquiryLayout.addWidget(self.familyCombox_inq,0,1)
        self.inquiryLayout.addWidget(self.genusCombox_inq,1,1)
        self.inquiryLayout.addWidget(self.speciesCombox_inq,2,1)
        self.inquiryLayout.addWidget(self.despInfo_inq,3,1)
        self.inquiryLayout.addWidget(self.getDespButton_inq,4,0)
        print("echo4")
        # infomation part
        self.frame_inquiry.setLayout(self.inquiryLayout)
        self.inqGeneralLayout=QHBoxLayout()
        print("echo7")
        self.inqGeneralLayout.addWidget(self.frame_inquiry)
        print("echo8")
        self.familyCombox_inq.currentTextChanged.connect(self.emit_inq_family)
        self.genusCombox_inq.currentTextChanged.connect(self.emit_inq_genus)
        self.getDespButton_inq.clicked.connect(self.emit_inq_species)
        self.container_inquiry.setLayout(self.inqGeneralLayout)
    def emit_inq_family(self):
        self.inq_familySignal.emit(self.familyCombox_inq.currentText())
    def emit_inq_genus(self):
        self.inq_genusSignal.emit(self.genusCombox_inq.currentText())
    def emit_inq_species(self):
        self.inq_speciesSignal.emit(self.speciesCombox_inq.currentText())
    def build_numberDist(self):
        print("echo1")
        self.frame_numberDist = QFrame()
        self.frame_numberDist.setFrameShape(QFrame.StyledPanel)
        self.vbox_numberDist = QVBoxLayout()
        self.vSpliter_numberDist = QSplitter(Qt.Vertical)
        self.operatePart_numberDist = QFrame()
        '''
        fill two parts
        '''
        # select part
        print("echo2")
        self.oper_layout_numberDist = QGridLayout()
        self.oper_tips_numberDist = QLabel("In this part, \nyou can select an area to get the distribution of species in this area.")
        self.oper_regionLabel_numberDist=QLabel("Region: ")
        self.oper_regionCombox_numberDist = QComboBox()
        self.oper_inqSpeciesButton_numberDist=QPushButton("In Species")
        self.oper_inqGenusButton_numberDist=QPushButton("In Genus")
        self.oper_inqFamilyButton_numberDist=QPushButton("In Family")
        self.oper_changeViewButton_numberDist=QPushButton("Change View")
        print("echo3")
        self.oper_layout_numberDist.addWidget(self.oper_tips_numberDist,0,1)
        self.oper_layout_numberDist.addWidget(self.oper_regionLabel_numberDist,1,0)
        self.oper_layout_numberDist.addWidget(self.oper_regionCombox_numberDist,1,1)
        self.oper_layout_numberDist.addWidget(self.oper_inqSpeciesButton_numberDist,2,0)
        self.oper_layout_numberDist.addWidget(self.oper_inqGenusButton_numberDist,2,1)
        self.oper_layout_numberDist.addWidget(self.oper_inqFamilyButton_numberDist,2,2)
        self.oper_layout_numberDist.addWidget(self.oper_changeViewButton_numberDist,3,0)
        self.operatePart_numberDist.setLayout(self.oper_layout_numberDist)
        self.vSpliter_numberDist.addWidget(self.operatePart_numberDist)
        print("echo4")
        # infomation part
        self.hSpliter_numberDist = QSplitter(Qt.Horizontal)
        self.infomationTablePart_numberDist = QScrollArea()
        tempLayout_table = QHBoxLayout()

        # self.table_addManager = QTableWidget(1,4)
        tablelabel_numberDist = ["number","species"]
        # self.table_addManager.setHorizontalHeaderLabels(tablelabel_addManager)
        self.table_numberDist = QTableView()
        self.tableModel_numberDist = QStandardItemModel(0, 2)
        self.tableModel_numberDist.setHorizontalHeaderLabels(tablelabel_numberDist)
        self.table_numberDist.setModel(self.tableModel_numberDist)
        self.table_numberDist.setEditTriggers(QTableView.NoEditTriggers)
        print("echo5")
        tempLayout_table.addWidget(self.table_numberDist)

        self.infomationTablePart_numberDist.setWidget(self.table_numberDist)

        self.infomationTablePart_numberDist.setWidgetResizable(True)
        self.hSpliter_numberDist.addWidget(self.infomationTablePart_numberDist)
        print("echo5.1")
        self.pieChartView_numberDist=self.makePieChartView()
        self.barChartView_numberDist=self.makeBarChartView()
        print("echo 5.2")
        self.views_numberDist=QStackedWidget()
        self.views_numberDist.addWidget(self.pieChartView_numberDist)
        self.views_numberDist.addWidget(self.barChartView_numberDist)
        self.hSpliter_numberDist.addWidget(self.views_numberDist)#在这里加图！！！！！
        self.views_numberDist.setCurrentIndex(1)
        self.views_numberDist.currentIndex()
        print("echo6")
        self.vSpliter_numberDist.addWidget(self.hSpliter_numberDist)
        self.vbox_numberDist.addWidget(self.vSpliter_numberDist)
        self.frame_numberDist.setLayout(self.vbox_numberDist)
        self.numberDistLayout = QHBoxLayout()
        print("echo7")
        self.numberDistLayout.addWidget(self.frame_numberDist)
        self.oper_inqSpeciesButton_numberDist.clicked.connect(self.emit_numberDist_species)
        self.oper_inqGenusButton_numberDist.clicked.connect(self.emit_numberDist_genus)
        self.oper_inqFamilyButton_numberDist.clicked.connect(self.emit_numberDist_family)
        self.oper_changeViewButton_numberDist.clicked.connect(lambda :self.changeChartView(self.views_numberDist))
        # self.oper_delButton_newRoot.clicked.connect(self.emit_newRoot_del)
        self.container_numberDist.setLayout(self.numberDistLayout)
        print("echo8")
    def emit_numberDist_species(self):
        self.numberDist_speciesSignal.emit(self.oper_regionCombox_numberDist.currentText())
    def emit_numberDist_genus(self):
        self.numberDist_genusSignal.emit(self.oper_regionCombox_numberDist.currentText())
    def emit_numberDist_family(self):
        self.numberDist_familySignal.emit(self.oper_regionCombox_numberDist.currentText())

    def build_heightDist(self):
        print("echo1")
        self.frame_heightDist = QFrame()
        self.frame_heightDist.setFrameShape(QFrame.StyledPanel)
        self.vbox_heightDist = QVBoxLayout()
        self.vSpliter_heightDist = QSplitter(Qt.Vertical)
        self.operatePart_heightDist = QFrame()
        '''
        fill two parts
        '''
        # select part
        print("echo2")
        self.oper_layout_heightDist = QGridLayout()
        self.oper_tips_heightDist = QLabel("You can inquiry infomation in species")
        self.oper_speciesLabel_heightDist = QLabel("Species: ")
        self.oper_speciesCombox_heightDist = QComboBox()
        self.oper_inqHeightButton_heightDist = QPushButton("Inquiry Height")
        self.oper_inqNumberButton_heightDist = QPushButton("Inquiry Number")
        self.oper_changeViewButton_heightDist=QPushButton("Change View")
        print("echo3")

        self.oper_layout_heightDist.addWidget(self.oper_tips_heightDist, 0, 1)
        self.oper_layout_heightDist.addWidget(self.oper_speciesLabel_heightDist, 1, 0)
        self.oper_layout_heightDist.addWidget(self.oper_speciesCombox_heightDist, 1, 1)
        self.oper_layout_heightDist.addWidget(self.oper_inqHeightButton_heightDist,2,0)
        self.oper_layout_heightDist.addWidget(self.oper_inqNumberButton_heightDist,2,1)
        self.oper_layout_heightDist.addWidget(self.oper_changeViewButton_heightDist,3,0)
        self.operatePart_heightDist.setLayout(self.oper_layout_heightDist)
        self.vSpliter_heightDist.addWidget(self.operatePart_heightDist)
        print("echo4")
        # infomation part
        self.hSpliter_heightDist = QSplitter(Qt.Horizontal)
        self.infomationTablePart_heightDist = QScrollArea()
        tempLayout_table = QHBoxLayout()


        tablelabel_heightDist = ["Avgerage Height", "Location"]

        self.table_heightDist = QTableView()
        self.tableModel_heightDist = QStandardItemModel(0, 2)
        self.tableModel_heightDist.setHorizontalHeaderLabels(tablelabel_heightDist)
        self.table_heightDist.setModel(self.tableModel_heightDist)
        self.table_heightDist.setEditTriggers(QTableView.NoEditTriggers)
        print("echo5")
        tempLayout_table.addWidget(self.table_heightDist)

        self.infomationTablePart_heightDist.setWidget(self.table_heightDist)

        self.infomationTablePart_heightDist.setWidgetResizable(True)
        self.hSpliter_heightDist.addWidget(self.infomationTablePart_heightDist)
        print("echo5.1")
        self.pieChartView_heightDist = self.makePieChartView()
        self.barChartView_heightDist = self.makeBarChartView()
        print("echo 5.2")
        self.views_heightDist = QStackedWidget()
        self.views_heightDist.addWidget(self.pieChartView_heightDist)
        self.views_heightDist.addWidget(self.barChartView_heightDist)
        self.hSpliter_heightDist.addWidget(self.views_heightDist)  # 在这里加图！！！！！
        self.views_heightDist.setCurrentIndex(0)
        print("echo6")
        self.vSpliter_heightDist.addWidget(self.hSpliter_heightDist)
        self.vbox_heightDist.addWidget(self.vSpliter_heightDist)
        self.frame_heightDist.setLayout(self.vbox_heightDist)
        self.heightDistLayout = QHBoxLayout()
        print("echo7")
        self.heightDistLayout.addWidget(self.frame_heightDist)
        self.oper_inqHeightButton_heightDist.clicked.connect(self.emit_heightDist_height)
        self.oper_inqNumberButton_heightDist.clicked.connect(self.emit_heightDist_number)
        self.oper_changeViewButton_heightDist.clicked.connect(lambda :self.changeChartView(self.views_heightDist))
        self.container_heightDist.setLayout(self.heightDistLayout)
        print("echo8")
    def emit_heightDist_height(self):
        self.heightDist_heightSignal.emit(self.oper_speciesCombox_heightDist.currentText())
    def emit_heightDist_number(self):
        self.heightDist_numberSignal.emit(self.oper_speciesCombox_heightDist.currentText())


    def build_addManager(self):#整个添加界面
        self.frame_addManager=QFrame()
        self.frame_addManager.setFrameShape(QFrame.StyledPanel)
        self.vbox=QVBoxLayout()
        self.spliter_addManager=QSplitter(Qt.Vertical)
        self.operatePart=QFrame()
        self.infoPart=QFrame()
        '''
        fill two parts
        '''
        # select part
        self.oper_layout=QGridLayout()
        self.oper_IDLabel=QLabel("ID: ")
        self.oper_nameLabel=QLabel("Name: ")
        self.oper_phoneLabel=QLabel("Phone Number: ")
        self.oper_deptLabel=QLabel("Department: ")
        self.oper_IDField=QLineEdit()
        self.oper_deptField=QComboBox()
        self.oper_nameField=QLineEdit()
        self.oper_phoneField=QLineEdit()
        self.oper_addButton=QPushButton("Add")
        self.oper_delButton=QPushButton("Delete")

        self.oper_layout.addWidget(self.oper_IDLabel,0,0)
        self.oper_layout.addWidget(self.oper_IDField,0,1)
        self.oper_layout.addWidget(self.oper_nameLabel,1,0)
        self.oper_layout.addWidget(self.oper_nameField,1,1)
        self.oper_layout.addWidget(self.oper_phoneLabel,2,0)
        self.oper_layout.addWidget(self.oper_phoneField,2,1)
        self.oper_layout.addWidget(self.oper_deptLabel,3,0)
        self.oper_layout.addWidget(self.oper_deptField,3,1)
        self.oper_layout.addWidget(self.oper_delButton,4,0)
        self.oper_layout.addWidget(self.oper_addButton,4,1)
        self.operatePart.setLayout(self.oper_layout)
        self.spliter_addManager.addWidget(self.operatePart)


        #infomation part
        self.infomationPart = QScrollArea()
        tempLayout = QHBoxLayout()


        # self.table_addManager = QTableWidget(1,4)
        tablelabel_addManager = ["m_id", "name","department","phone number"]
        # self.table_addManager.setHorizontalHeaderLabels(tablelabel_addManager)
        self.table_addManager=QTableView()
        self.tableModel_addManager=QStandardItemModel(0,4)
        self.tableModel_addManager.setHorizontalHeaderLabels(tablelabel_addManager)
        self.table_addManager.setModel(self.tableModel_addManager)
        self.table_addManager.setEditTriggers(QTableView.NoEditTriggers)

        # self.table.setItem(0, 0, QTableWidgetItem("hello"))
        # self.table.setItem(0, 1, QTableWidgetItem("you"))
        # self.table.setItem(0, 2, QTableWidgetItem("should"))
        # self.table.setItem(0, 3, QTableWidgetItem("happy"))
        # self.table_addManager.setEnabled(False)
        tempLayout.addWidget(self.table_addManager)

        # self.scrollAreaContent.setLayout(self.tempLayout)

        # self.testButton.clicked.connect(self.update)
        self.infomationPart.setWidget(self.table_addManager)

        self.infomationPart.setWidgetResizable(True)

        # self.table_addManager.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        # self.spliter_addManager.addWidget(self.infoPart)
        self.spliter_addManager.addWidget(self.infomationPart)
        self.vbox.addWidget(self.spliter_addManager)
        self.frame_addManager.setLayout(self.vbox)
        self.managerLayout=QHBoxLayout()
        self.managerLayout.addWidget(self.frame_addManager)

        self.container_addManager.setLayout(self.managerLayout)
        self.oper_addButton.clicked.connect(self.emit_addManager_add)
        self.oper_delButton.clicked.connect(self.emit_addManager_del)
    def emit_addManager_add(self):
        self.addManager_addSignal.emit(self.oper_IDField.text(),self.oper_deptField.currentText(),self.oper_phoneField.text(),self.oper_nameField.text())
    def emit_addManager_del(self):
        self.addManager_delSignal.emit(self.oper_IDField.text())

    def build_addRegion(self):
        self.frame_addRegion = QFrame()
        self.frame_addRegion.setFrameShape(QFrame.StyledPanel)
        self.vbox_addRegion = QVBoxLayout()
        self.spliter_addRegion = QSplitter(Qt.Vertical)
        self.operatePart_addRegion = QFrame()
        self.infoPart_addRegion = QFrame()
        '''
        fill two parts
        '''
        # select part
        self.oper_layout_addRegion = QGridLayout()
        self.oper_IDLabel_addRegion = QLabel("Region ID: ")
        self.oper_locationLabel_addRegion = QLabel("Location: ")
        self.oper_areaLabel_addRegion = QLabel("Area: ")
        # self.oper_managerLabel_addRegion = QLabel("Manager: ")
        self.oper_IDField_addRegion = QLineEdit()
        self.oper_locationField_addRegion = QLineEdit()
        self.oper_areaField_addRegion = QLineEdit()
        # self.oper_managerField_addRegion = QLineEdit()
        self.oper_addButton_addRegion = QPushButton("Add")
        self.oper_delButton_addRegion = QPushButton("Delete")

        self.oper_layout_addRegion.addWidget(self.oper_IDLabel_addRegion, 0, 0)
        self.oper_layout_addRegion.addWidget(self.oper_IDField_addRegion, 0, 1)
        self.oper_layout_addRegion.addWidget(self.oper_locationLabel_addRegion, 1, 0)
        self.oper_layout_addRegion.addWidget(self.oper_locationField_addRegion, 1, 1)
        self.oper_layout_addRegion.addWidget(self.oper_areaLabel_addRegion, 2, 0)
        self.oper_layout_addRegion.addWidget(self.oper_areaField_addRegion, 2, 1)
        # self.oper_layout_addRegion.addWidget(self.oper_managerLabel_addRegion, 3, 0)
        # self.oper_layout_addRegion.addWidget(self.oper_managerField_addRegion, 3, 1)
        self.oper_layout_addRegion.addWidget(self.oper_delButton_addRegion, 3, 0)
        self.oper_layout_addRegion.addWidget(self.oper_addButton_addRegion, 3, 1)
        self.operatePart_addRegion.setLayout(self.oper_layout_addRegion)
        self.spliter_addRegion.addWidget(self.operatePart_addRegion)

        # infomation part
        self.infomationPart_addRegion = QScrollArea()
        tempLayout = QHBoxLayout()

        # self.table_addManager = QTableWidget(1,4)
        tablelabel_addRegion = ["Area ID", "Location", "Area", "Manager ID"]
        # self.table_addManager.setHorizontalHeaderLabels(tablelabel_addManager)
        self.table_addRegion = QTableView()
        self.tableModel_addRegion = QStandardItemModel(0, 4)
        self.tableModel_addRegion.setHorizontalHeaderLabels(tablelabel_addRegion)
        self.table_addRegion.setModel(self.tableModel_addRegion)
        self.table_addRegion.setEditTriggers(QTableView.NoEditTriggers)

        # self.table.setItem(0, 0, QTableWidgetItem("hello"))
        # self.table.setItem(0, 1, QTableWidgetItem("you"))
        # self.table.setItem(0, 2, QTableWidgetItem("should"))
        # self.table.setItem(0, 3, QTableWidgetItem("happy"))
        # self.table_addManager.setEnabled(False)
        tempLayout.addWidget(self.table_addRegion)

        # self.scrollAreaContent.setLayout(self.tempLayout)

        # self.testButton.clicked.connect(self.update)
        self.infomationPart_addRegion.setWidget(self.table_addRegion)

        self.infomationPart_addRegion.setWidgetResizable(True)

        # self.table_addManager.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        # self.spliter_addManager.addWidget(self.infoPart)
        self.spliter_addRegion.addWidget(self.infomationPart_addRegion)
        self.vbox_addRegion.addWidget(self.spliter_addRegion)
        self.frame_addRegion.setLayout(self.vbox_addRegion)
        self.regionLayout = QHBoxLayout()
        self.regionLayout.addWidget(self.frame_addRegion)
        self.oper_addButton_addRegion.clicked.connect(self.emit_addRegion_add)
        self.oper_delButton_addRegion.clicked.connect(self.emit_addRegion_del)
        self.container_addRegion.setLayout(self.regionLayout)
    def emit_addRegion_add(self):
        self.addRegion_addSignal.emit(self.oper_IDField_addRegion.text(),self.oper_locationField_addRegion.text(),self.oper_areaField_addRegion.text())
    def emit_addRegion_del(self):
        self.addRegion_delSignal.emit(self.oper_IDField_addRegion.text())

    def build_arrangeWork(self):

        print("in build arrange work")
        self.frame_arrangeWork = QFrame()
        self.frame_arrangeWork.setFrameShape(QFrame.StyledPanel)
        self.vbox_arrangeWork = QVBoxLayout()
        self.spliter_arrangeWork = QSplitter(Qt.Vertical)
        self.operatePart_arrangeWork = QFrame()
        self.infoPart_arrangeWork = QFrame()
        '''
        fill two parts
        '''
        # select part
        print("echo1")

        self.oper_layout_arrangeWork = QGridLayout()
        self.oper_regionLabel_arrangeWork = QLabel("Region: ")
        self.oper_regionField_arrangeWork = QComboBox()
        self.oper_newManagerLabel_arrangeWork = QLabel("New Manager ID: ")
        self.oper_newManagerField_arrangeWork = QComboBox()
        self.oper_revokeButton_arrangeWork=QPushButton("Revoke")
        self.oper_originalManagerLabel_arrangeWork=QLabel("Original Manager ID: ")
        self.oper_originalManagerField_arrangeWork=QComboBox()
        self.oper_assignButton_arrangeWork = QPushButton("Assign")
        self.oper_substituteButton_arrangeWork=QPushButton("Substitute")
        self.oper_layout_arrangeWork.addWidget(self.oper_regionLabel_arrangeWork, 0, 0)
        self.oper_layout_arrangeWork.addWidget(self.oper_regionField_arrangeWork, 0, 1)
        self.oper_layout_arrangeWork.addWidget(self.oper_originalManagerLabel_arrangeWork, 1, 0)
        self.oper_layout_arrangeWork.addWidget(self.oper_originalManagerField_arrangeWork, 1, 1)

        self.oper_layout_arrangeWork.addWidget(self.oper_newManagerLabel_arrangeWork, 2, 0)
        self.oper_layout_arrangeWork.addWidget(self.oper_newManagerField_arrangeWork, 2, 1)
        self.oper_layout_arrangeWork.addWidget(self.oper_originalManagerLabel_arrangeWork, 3, 0)
        self.oper_layout_arrangeWork.addWidget(self.oper_originalManagerField_arrangeWork, 3, 1)
        print("echo5")
        self.oper_layout_arrangeWork.addWidget(self.oper_revokeButton_arrangeWork,4,0)
        self.oper_layout_arrangeWork.addWidget(self.oper_assignButton_arrangeWork, 4, 1)
        self.oper_layout_arrangeWork.addWidget(self.oper_substituteButton_arrangeWork,4,2)
        self.operatePart_arrangeWork.setLayout(self.oper_layout_arrangeWork)
        self.spliter_arrangeWork.addWidget(self.operatePart_arrangeWork)
        # infomation part
        print("echo6")
        self.infomationPart_arrangeWork = QScrollArea()
        tempLayout = QHBoxLayout()
        # self.table_addManager = QTableWidget(1,4)
        tablelabel_arrangeWork = ["Area ID", "Location", "Area", "Manager ID"]
        # self.table_addManager.setHorizontalHeaderLabels(tablelabel_addManager)
        self.table_arrangeWork = QTableView()
        self.tableModel_arrangeWork = QStandardItemModel(0, 4)
        self.tableModel_arrangeWork.setHorizontalHeaderLabels(tablelabel_arrangeWork)
        self.table_arrangeWork.setModel(self.tableModel_arrangeWork)
        self.table_arrangeWork.setEditTriggers(QTableView.NoEditTriggers)
        tempLayout.addWidget(self.table_arrangeWork)

        self.infomationPart_arrangeWork.setWidget(self.table_arrangeWork)

        self.infomationPart_arrangeWork.setWidgetResizable(True)
        print("echo7")
        self.spliter_arrangeWork.addWidget(self.infomationPart_arrangeWork)
        self.vbox_arrangeWork.addWidget(self.spliter_arrangeWork)
        self.frame_arrangeWork.setLayout(self.vbox_arrangeWork)
        self.arrangeLayout = QHBoxLayout()
        self.arrangeLayout.addWidget(self.frame_arrangeWork)
        print("echo8")
        self.oper_revokeButton_arrangeWork.clicked.connect(self.emit_revokeWork)
        print("echo8.1")
        self.oper_assignButton_arrangeWork.clicked.connect(self.emit_assignWork)
        print("echo 8.2")
        self.oper_substituteButton_arrangeWork.clicked.connect(self.emit_substituteWork)
        print("echo8.3")
        self.oper_revokeButton_arrangeWork.clicked.connect(self.emit_revokeWork)
        print("echo9")
        self.container_arrangeWork.setLayout(self.arrangeLayout)
        print("echo10")
    def emit_substituteWork(self):
        self.substituteWorkSignal.emit(self.oper_regionField_arrangeWork.currentText(),self.oper_originalManagerField_arrangeWork.currentText(),self.oper_newManagerField_arrangeWork.currentText())
    def emit_assignWork(self):
        self.assignWorkSignal.emit(self.oper_regionField_arrangeWork.currentText(),self.oper_newManagerField_arrangeWork.currentText())
    def emit_revokeWork(self):
        self.revokeWorkSignal.emit(self.oper_regionField_arrangeWork.currentText(),self.oper_originalManagerField_arrangeWork.currentText())
    def build_newRoot(self):
        print("echo1")
        self.frame_newRoot = QFrame()
        self.frame_newRoot.setFrameShape(QFrame.StyledPanel)
        self.vbox_newRoot = QVBoxLayout()
        self.spliter_newRoot = QSplitter(Qt.Vertical)
        self.operatePart_newRoot = QFrame()
        self.infoPart_newRoot = QFrame()
        '''
        fill two parts
        '''
        # select part
        print("echo2")
        self.oper_layout_newRoot = QGridLayout()
        self.oper_IDLabel_newRoot = QLabel("Plant ID: ")
        self.oper_locationLabel_newRoot = QLabel("Location: ")
        self.oper_speciesLabel_newRoot = QLabel("Species: ")
        self.oper_heightLabel_newRoot = QLabel("Height: ")
        self.oper_IDField_newRoot = QLineEdit()
        self.oper_locationField_newRoot = QComboBox()
        self.oper_speciesField_newRoot = QComboBox()
        self.oper_heightField_newRoot = QLineEdit()
        self.oper_addButton_newRoot = QPushButton("Add")
        self.oper_delButton_newRoot = QPushButton("Delete")
        print("echo3")
        self.oper_layout_newRoot.addWidget(self.oper_IDLabel_newRoot, 0, 0)
        self.oper_layout_newRoot.addWidget(self.oper_IDField_newRoot, 0, 1)
        self.oper_layout_newRoot.addWidget(self.oper_locationLabel_newRoot, 1, 0)
        self.oper_layout_newRoot.addWidget(self.oper_locationField_newRoot, 1, 1)
        self.oper_layout_newRoot.addWidget(self.oper_speciesLabel_newRoot, 2, 0)
        self.oper_layout_newRoot.addWidget(self.oper_speciesField_newRoot, 2, 1)
        self.oper_layout_newRoot.addWidget(self.oper_heightLabel_newRoot, 3, 0)
        self.oper_layout_newRoot.addWidget(self.oper_heightField_newRoot, 3, 1)
        self.oper_layout_newRoot.addWidget(self.oper_delButton_newRoot, 4, 0)
        self.oper_layout_newRoot.addWidget(self.oper_addButton_newRoot, 4, 1)
        self.operatePart_newRoot.setLayout(self.oper_layout_newRoot)
        self.spliter_newRoot.addWidget(self.operatePart_newRoot)
        print("echo4")
        # infomation part
        self.infomationPart_newRoot = QScrollArea()
        tempLayout = QHBoxLayout()

        # self.table_addManager = QTableWidget(1,4)
        tablelabel_newRoot = ["Plant ID", "Species Name", "Area ID", "Height"]
        # self.table_addManager.setHorizontalHeaderLabels(tablelabel_addManager)
        self.table_newRoot = QTableView()
        self.tableModel_newRoot = QStandardItemModel(0, 4)
        self.tableModel_newRoot.setHorizontalHeaderLabels(tablelabel_newRoot)
        self.table_newRoot.setModel(self.tableModel_newRoot)
        self.table_newRoot.setEditTriggers(QTableView.NoEditTriggers)
        print("echo5")
        tempLayout.addWidget(self.table_newRoot)

        self.infomationPart_newRoot.setWidget(self.table_newRoot)

        self.infomationPart_newRoot.setWidgetResizable(True)
        print("echo6")
        self.spliter_newRoot.addWidget(self.infomationPart_newRoot)
        self.vbox_newRoot.addWidget(self.spliter_newRoot)
        self.frame_newRoot.setLayout(self.vbox_newRoot)
        self.newRootLayout = QHBoxLayout()
        print("echo7")
        self.newRootLayout.addWidget(self.frame_newRoot)
        self.oper_addButton_newRoot.clicked.connect(self.emit_newRoot_add)
        self.oper_delButton_newRoot.clicked.connect(self.emit_newRoot_del)
        self.container_newRoot.setLayout(self.newRootLayout)
        print("echo8")
    def emit_newRoot_add(self):
        self.newRoot_addSignal.emit(self.oper_IDField_newRoot.text(),self.oper_locationField_newRoot.currentText(),self.oper_speciesField_newRoot.currentText(),self.oper_heightField_newRoot.text())
    def emit_newRoot_del(self):
        self.newRoot_delSignal.emit(self.oper_IDField_newRoot.text(),self.oper_speciesField_newRoot.currentText())

    def build_newSpecies(self):
        print("echo1")
        self.frame_newSpecies = QFrame()
        self.frame_newSpecies.setFrameShape(QFrame.StyledPanel)
        self.vbox_newSpecies = QVBoxLayout()
        self.spliter_newSpecies = QSplitter(Qt.Vertical)
        self.operatePart_newSpecies = QFrame()
        self.infoPart_newSpecies = QFrame()
        '''
        fill two parts
        '''
        # select part
        print("echo2")
        self.oper_layout_newSpecies = QGridLayout()
        self.oper_tips_newSpecies=QLabel("Entering the basic information of the new species, BE CAREFUL WHEN ENTERING!!!")
        self.oper_familyLabel_newSpecies = QLabel("Family: ")
        self.oper_genusLabel_newSpecies = QLabel("Genus: ")
        self.oper_speciesLabel_newSpecies = QLabel("Species: ")
        self.oper_descriptionLabel_newSpecies = QLabel("Description: ")
        self.oper_familyField_newSpecies = QLineEdit()
        self.oper_genusField_newSpecies = QLineEdit()
        self.oper_speciesField_newSpecies = QLineEdit()
        self.oper_descriptionField_newSpecies = QTextEdit()
        self.oper_addButton_newSpecies = QPushButton("Add")
        print("echo3")
        self.oper_layout_newSpecies.addWidget(self.oper_tips_newSpecies,0,1,1,1)
        self.oper_layout_newSpecies.addWidget(self.oper_familyLabel_newSpecies,1,0)
        self.oper_layout_newSpecies.addWidget(self.oper_familyField_newSpecies,1,1)
        self.oper_layout_newSpecies.addWidget(self.oper_genusLabel_newSpecies,2,0)
        self.oper_layout_newSpecies.addWidget(self.oper_genusField_newSpecies,2,1)
        self.oper_layout_newSpecies.addWidget(self.oper_speciesLabel_newSpecies,3,0)
        self.oper_layout_newSpecies.addWidget(self.oper_speciesField_newSpecies,3,1)
        self.oper_layout_newSpecies.addWidget(self.oper_descriptionLabel_newSpecies,4,0)
        self.oper_layout_newSpecies.addWidget(self.oper_descriptionField_newSpecies,4,1,3,5)
        self.oper_layout_newSpecies.addWidget(self.oper_addButton_newSpecies,5,0)
        self.operatePart_newSpecies.setLayout(self.oper_layout_newSpecies)
        self.spliter_newSpecies.addWidget(self.operatePart_newSpecies)
        print("echo4")
        # infomation part
        self.infomationPart_newSpecies = QScrollArea()
        tempLayout = QHBoxLayout()

        # self.table_addManager = QTableWidget(1,4)
        tablelabel_newSpecies = ["Species Name", "Genus Name", "Family Name", "Description"]
        # self.table_addManager.setHorizontalHeaderLabels(tablelabel_addManager)
        self.table_newSpecies = QTableView()
        self.tableModel_newSpecies = QStandardItemModel(0, 4)
        self.tableModel_newSpecies.setHorizontalHeaderLabels(tablelabel_newSpecies)
        self.table_newSpecies.setModel(self.tableModel_newSpecies)
        self.table_newSpecies.setEditTriggers(QTableView.NoEditTriggers)
        print("echo5")
        tempLayout.addWidget(self.table_newSpecies)

        self.infomationPart_newSpecies.setWidget(self.table_newSpecies)

        self.infomationPart_newSpecies.setWidgetResizable(True)
        print("echo6")
        self.spliter_newSpecies.addWidget(self.infomationPart_newSpecies)
        self.vbox_newSpecies.addWidget(self.spliter_newSpecies)
        self.frame_newSpecies.setLayout(self.vbox_newSpecies)
        self.newSpeciesLayout = QHBoxLayout()
        print("echo7")
        self.newSpeciesLayout.addWidget(self.frame_newSpecies)
        self.oper_addButton_newSpecies.clicked.connect(self.emit_newSpecies_add)
        # self.oper_delButton_newRoot.clicked.connect(self.emit_newRoot_del)
        self.container_newSpecies.setLayout(self.newSpeciesLayout)
        print("echo8")
    def emit_newSpecies_add(self):
        self.newSpecies_addSignal.emit(self.oper_familyField_newSpecies.text(),self.oper_genusField_newSpecies.text(),self.oper_speciesField_newSpecies.text(),self.oper_descriptionField_newSpecies.toPlainText())


    def makePieChartView(self):
        print("echo a1")
        series = QPieSeries()
        chart = QChart()
        # 创建ChartView，它是显示图表的控件
        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        return chartview
    def makeBarChartView(self):
        series = QBarSeries()
        # series.append(set)
        chart = QChart()
        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        return chartview
    def changeChartView(self,targetChartViews):
        print("change views")
        cur=targetChartViews.currentIndex()
        targetChartViews.setCurrentIndex((cur+1)%2)
    def updateTableView(self, sqlRes,targetTableModel):
        # print("in updated tablemodel")
        numColumn = len(sqlRes.desp)
        numRow = len(sqlRes.data)
        # print("in updated tablemodel1")
        targetTableModel.setHorizontalHeaderLabels(sqlRes.desp)
        # print("in updated tablemodel2")
        targetTableModel.setColumnCount(numColumn)
        # print("in updated tablemodel3")
        targetTableModel.setRowCount(numRow)
        for i in range(int(numRow)):
            for j in range(int(numColumn)):
                targetTableModel.setItem(i, j, QStandardItem(str(sqlRes.data[i][j])))
                # print("in updated tablemodel4")
    def updateCombox(self,comboxList,targetCombox):
        targetCombox.clear()
        targetCombox.addItems(comboxList)
    def updatePieView(self, sqlRes, targetPieView):  # 真的是chartView组件
        print("in updated pieview")
        series = QPieSeries()
        for elem in sqlRes.data:
            sls = QPieSlice(str(elem[1]), float(elem[0]))
            sls.setLabelVisible()
            series.append(sls)
        chart = QChart()
        # QLegend类是显示图表的图例，先隐藏掉
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        # 设置动画效果
        chart.setAnimationOptions(QChart.SeriesAnimations)
        # 设置标题
        # chart.setTitle("饼图示例")
        chart.legend().setVisible(True)
        # 对齐方式
        chart.legend().setAlignment(Qt.AlignBottom)
        targetPieView.setChart(chart)
    def updateBarView(self,sqlRes,targetBarView,type):
        set = QBarSet(type)

        for elem in sqlRes.data:
            set.append(elem[0])
        # 若显示各部分所占百分比，用QPercentBarSeries
        series = QBarSeries()
        series.append(set)

        chart = QChart()
        chart.addSeries(series)
        # chart.setTitle("一周数据展示")
        chart.setAnimationOptions(QChart.SeriesAnimations)
        # chart.setTheme(QChart.ChartThemeDark)
        # 横轴数据

        categories = []
        for elem in sqlRes.data:
            categories.append(elem[1])
        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
        targetBarView.setChart(chart)
    def updateTextContent(self,content,target):
        target.setText(content)
        print("Changed Text")
    def initFunctionTree(self):
        self.functionTree=QTreeWidget()
        self.functionTree.setColumnCount(1)
        self.functionTree.setHeaderLabels(['Function'])


        inquiryFunc=QTreeWidgetItem(self.functionTree)
        inquiryFunc.setText(0,"Inquiry")
        # 添加根目录
        statisticsFunc = QTreeWidgetItem(self.functionTree)
        # 设置key
        statisticsFunc.setText(0,"Statistics")
        # root.setIcon(0, QIcon('new.png'))

        # 添加子目录的两种方式，第一种
        inq_count = QTreeWidgetItem(statisticsFunc)
        inq_count.setText(0, 'Number Distribution')
        # child1.setCheckState(0, Qt.Unchecked)  # 设置选中状态
        # child1.setBackground(0, QColor(205, 201, 201))
        # 第二种
        inq_height = QTreeWidgetItem()
        inq_height.setText(0, 'Height Distribution')
        statisticsFunc.addChild(inq_height)

        settingFunc=QTreeWidgetItem(self.functionTree)
        settingFunc.setText(0,"Settings and Management")

        set_addManager=QTreeWidgetItem(settingFunc)
        set_addManager.setText(0,"Add Manager")
        set_addRegion=QTreeWidgetItem(settingFunc)
        set_addRegion.setText(0,"Add Region")
        set_arrangePerson=QTreeWidgetItem(settingFunc)
        set_arrangePerson.setText(0,"Arrange Work")

        plantFunc=QTreeWidgetItem(self.functionTree)
        plantFunc.setText(0,"Plant Management")

        plant_newRoot=QTreeWidgetItem(plantFunc)
        plant_newRoot.setText(0,"New Root")
        plant_newSpecies=QTreeWidgetItem(plantFunc)
        plant_newSpecies.setText(0,"New Species")


        # # 添加2层子节点
        # child1_1 = QTreeWidgetItem(child1)
        # child1_1.setText(0, '子节点1的子节点')

        # child1_1.setIcon(0, QIcon('open.png'))

        # 添加点击事件
        self.functionTree.clicked.connect(self.selectFunction)
    def selectFunction(self):
        curElem=self.sender().currentItem().text(0)
        print(curElem)
        if curElem in self.funcTable.keys():
            self.butler.setCurrentIndex(self.funcTable[curElem])
    def test(self):
        print("test for main window")

    def showSQLErrorInfo(self,warning):
        reply = QMessageBox.information(self,"Warning",warning,QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)

class Views():
    def __init__(self):
        self.loginWindow = LoginWindow()


