from View import *



class InquiryController():
    def numberDist_species(self,region,mainWindow,sqler):
        try:
            cmd="select count(ID) as 'number of plant',species_name from living natural join region where location=%s group by species_name"
            if region=="ALL":
                cmd="select count(ID) as 'number of plant',species_name from living natural join region group by species_name"
                sqler.select(cmd)
            else:
                sqler.select_para(cmd,(region))
            mainWindow.test()
            mainWindow.updateTableView(sqler.result,mainWindow.tableModel_numberDist)
            mainWindow.updatePieView(sqler.result,mainWindow.pieChartView_numberDist)
            mainWindow.updateBarView(sqler.result,mainWindow.barChartView_numberDist,"number of plant")
        # self.view.mainWindow.table_numberDist, self.view.mainWindow.pieChartView_numberDist, self.view.mainWindow.barChartView_numberDist
        except:
            pass
    def numberDist_family(self,region,mainWindow,sqler):
        try:
            cmd="select count(ID) as 'number of plant',family_name from living natural join species natural join genus natural join region where location=%s group by family_name"
            if region == "ALL":
                cmd = "select count(ID) as 'number of plant',family_name from living natural join species natural join genus natural join region group by family_name"
                sqler.select(cmd)
            else:
                sqler.select_para(cmd,(region))
            mainWindow.updateTableView(sqler.result,mainWindow.tableModel_numberDist)
            mainWindow.updatePieView(sqler.result,mainWindow.pieChartView_numberDist)
            mainWindow.updateBarView(sqler.result,mainWindow.barChartView_numberDist,"number of plant")
        except:
            pass
    def numberDist_genus(self,region,mainWindow,sqler):
        try:
            cmd="select count(ID) as 'number of plant',genus_name from living natural join species  natural join region where location=%s group by genus_name"
            if region == "ALL":
                cmd = "select count(ID) as 'number of plant',genus_name from living natural join species  natural join region group by genus_name"
                sqler.select(cmd)
            else:
                sqler.select_para(cmd,(region))
            mainWindow.updateTableView(sqler.result,mainWindow.tableModel_numberDist)
            mainWindow.updatePieView(sqler.result,mainWindow.pieChartView_numberDist)
            mainWindow.updateBarView(sqler.result,mainWindow.barChartView_numberDist,"number of plant")
        except:
            pass
    def heightDist_height(self,species,mainWindow,sqler):
        try:
            cmd="select avg(height) as 'Average Height',location from living natural join region where species_name=%s group by location"
            if species=="ALL":
                cmd="select avg(height) as 'Average Height',location from living natural join region group by location"
                sqler.select(cmd)
            else:
                sqler.select_para(cmd,(species))
            mainWindow.updateTableView(sqler.result, mainWindow.tableModel_heightDist)
            mainWindow.updatePieView(sqler.result, mainWindow.pieChartView_heightDist)
            mainWindow.updateBarView(sqler.result, mainWindow.barChartView_heightDist, "Average Height")
        except:
            pass
    def heightDist_number(self,species,mainWindow,sqler):
        try:
            cmd="select count(ID) as 'Number of Plant',location from living natural join region where species_name=%s group by location"
            if species=="ALL":
                cmd="select count(ID) as 'Number of Plant',location from living natural join region group by location"
                sqler.select(cmd)
            else:
                sqler.select_para(cmd,(species))
            mainWindow.updateTableView(sqler.result, mainWindow.tableModel_heightDist)
            mainWindow.updatePieView(sqler.result, mainWindow.pieChartView_heightDist)
            mainWindow.updateBarView(sqler.result, mainWindow.barChartView_heightDist, "Average Height")
        except:
            pass




class Controller():

    def __init__(self):
        self.view=Views()
        # self.settingCtrl=SettingController()
        # self.plantCtrl=PlantController()
        self.inquiryCtrl=InquiryController()
        self.view.loginWindow.loadInfoSig.connect(self.connectSQL)
    def connectSQL(self,user,pwd):
        try:
            self.sqler=SQLOperator(user,pwd)
            print('okok')
            self.runMain()
        except:
            self.view.loginWindow.showLoginError()
    def runLogin(self):
        self.view.loginWindow.show()
    def runMain(self):
        self.view.mainWindow=MainWindow()
        print("main_initok")
        self.view.mainWindow.addManager_addSignal.connect(self.addManager_add)
        self.view.mainWindow.addManager_delSignal.connect(self.addManager_del)
        self.view.mainWindow.addRegion_addSignal.connect(self.addRegion_add)
        self.view.mainWindow.addRegion_delSignal.connect(self.addRegion_del)
        self.view.mainWindow.assignWorkSignal.connect(self.assignWork)
        self.view.mainWindow.substituteWorkSignal.connect(self.substituteWork)
        self.view.mainWindow.revokeWorkSignal.connect(self.revokeWork)
        self.view.mainWindow.newRoot_addSignal.connect(self.newRoot_add)
        self.view.mainWindow.newRoot_delSignal.connect(self.newRoot_del)
        self.view.mainWindow.newSpecies_addSignal.connect(self.newSpecies_add)
        self.view.mainWindow.numberDist_speciesSignal.connect(self.numberDist_species)
        self.view.mainWindow.numberDist_genusSignal.connect(self.numberDist_genus)
        self.view.mainWindow.numberDist_familySignal.connect(self.numberDist_family)
        self.view.mainWindow.heightDist_heightSignal.connect(self.heightDist_height)
        self.view.mainWindow.heightDist_numberSignal.connect(self.heightDist_number)

        self.view.mainWindow.inq_familySignal.connect(self.freshGenusCombox)
        self.view.mainWindow.inq_genusSignal.connect(self.freshSpeciesCombox)
        self.view.mainWindow.inq_speciesSignal.connect(self.displayDescription)
        print("2022.6.8")

        self.updateRegionCombox(self.view.mainWindow.oper_regionCombox_numberDist)
        self.updateSpeciesCombox(self.view.mainWindow.oper_speciesCombox_heightDist)
        self.updateRegionCombox_notAll(self.view.mainWindow.oper_locationField_newRoot)
        self.updateSpeciesCombox_notAll(self.view.mainWindow.oper_speciesField_newRoot)
        self.updateRegionCombox_notAll(self.view.mainWindow.oper_regionField_arrangeWork)
        self.updateDepartmentCombox_notAll(self.view.mainWindow.oper_deptField)
        print("2022.6.6")
        self.updateMangerCombox_notAll(self.view.mainWindow.oper_originalManagerField_arrangeWork)
        print("2022.6.6")
        self.updateFamilyCombox(self.view.mainWindow.familyCombox_inq)
        self.updateMangerCombox_notAll(self.view.mainWindow.oper_newManagerField_arrangeWork)
    def updateGenusCombox_condition(self,target,familyName):
        self.view.mainWindow.updateCombox(self.sqler.getComboxList_noneAll("select distinct genus_name from genus where family_name='{fm}'".format(fm=familyName)), target)
    def updateFamilyCombox(self,target):
        self.view.mainWindow.updateCombox(self.sqler.getComboxList_noneAll("select distinct family_name from familia"),target)

    def updateSpeciesCombox_condition(self, target,genusName):
        self.view.mainWindow.updateCombox(self.sqler.getComboxList_noneAll("select distinct species_name from species where genus_name='{gn}'".format(gn=genusName)), target)

    def updateSpeciesCombox(self,target):
        self.view.mainWindow.updateCombox(self.sqler.getComboxList("select distinct species_name from species"),target)
    def updateRegionCombox(self,target):
        self.view.mainWindow.updateCombox(self.sqler.getComboxList("select distinct location from region"),target)
    def updateRegionCombox_notAll(self,target):
        self.view.mainWindow.updateCombox(self.sqler.getComboxList_noneAll("select distinct location from region"),target)
    def updateSpeciesCombox_notAll(self,target):
        self.view.mainWindow.updateCombox(self.sqler.getComboxList_noneAll("select distinct species_name from species"),target)
    def updateDepartmentCombox_notAll(self,target):
        self.view.mainWindow.updateCombox(self.sqler.getComboxList_noneAll("select distinct dept_name from department"),
                                          target)
    def updateMangerCombox_notAll(self,target):
        self.view.mainWindow.updateCombox(self.sqler.getComboxList_noneAll("select distinct m_id from manager"),
                                          target)
    def numberDist_species(self,region):
        print("generalCtrl's seaech")
        self.inquiryCtrl.numberDist_species(region,self.view.mainWindow,self.sqler)

    def numberDist_family(self,region):
        self.inquiryCtrl.numberDist_family(region,self.view.mainWindow,self.sqler)
    def numberDist_genus(self,region):
        self.inquiryCtrl.numberDist_genus(region,self.view.mainWindow,self.sqler)
    def heightDist_height(self,species):
        self.inquiryCtrl.heightDist_height(species,self.view.mainWindow,self.sqler)
    def heightDist_number(self,species):
        self.inquiryCtrl.heightDist_number(species, self.view.mainWindow, self.sqler)

    def addManager_add(self,m_id,dept_name,phone,name):
        try:
            print("echo5")
            self.sqler.insert_para("insert into manager values(%s,%s,%s,%s)",(m_id,dept_name,phone,name))
            print("echo6")
            self.sqler.select("select * from manager")
            print("echo7")
            self.view.mainWindow.updateTableView(self.sqler.result,self.view.mainWindow.tableModel_addManager)
            print("echo8")
            self.updateMangerCombox_notAll(self.view.mainWindow.oper_originalManagerField_arrangeWork)
            self.updateMangerCombox_notAll(self.view.mainWindow.oper_newManagerField_arrangeWork)
        except:
            self.view.mainWindow.showSQLErrorInfo("Fail to add manager, please check your SQL command")
            pass
    def addManager_del(self,m_id):
        try:
            self.sqler.delete_para("delete from manager where m_id=%s",(m_id))
            self.sqler.select("select * from manager")
            self.view.mainWindow.updateTableView(self.sqler.result,self.view.mainWindow.tableModel_addManager)
            self.updateMangerCombox_notAll(self.view.mainWindow.oper_originalManagerField_arrangeWork)
            self.updateMangerCombox_notAll(self.view.mainWindow.oper_newManagerField_arrangeWork)
        except:
            self.view.mainWindow.showSQLErrorInfo("Fail to delete, ID or name not found")

            pass
    def addRegion_add(self,a_id,location,area):
        try:
            self.sqler.insert_para("insert into region values(%s,%s,%s)",(a_id,location,float(area)))
            self.sqler.select("select area_id,location,area from region")
            self.view.mainWindow.updateTableView(self.sqler.result, self.view.mainWindow.tableModel_addRegion)
            # self.view.updateRegionCombox()
            self.updateRegionCombox(self.view.mainWindow.oper_regionCombox_numberDist)
            # self.updateSpeciesCombox(self.view.mainWindow.oper_speciesCombox_heightDist)
            self.updateRegionCombox_notAll(self.view.mainWindow.oper_locationField_newRoot)
            # self.updateSpeciesCombox_notAll(self.view.mainWindow.oper_speciesField_newRoot)
            self.updateRegionCombox_notAll(self.view.mainWindow.oper_regionField_arrangeWork)
        except:
            self.view.mainWindow.showSQLErrorInfo("Fail to add region, please check your SQL command")
            pass
    def addRegion_del(self,a_id):
        try:
            self.sqler.delete_para("delete from region where area_id=%s",(a_id))
            self.sqler.select("select area_id,location,area from region ")
            self.view.mainWindow.updateTableView(self.sqler.result, self.view.mainWindow.tableModel_addRegion)
            # self.view.updateRegionCombox_numberDist()
            self.updateRegionCombox(self.view.mainWindow.oper_regionCombox_numberDist)
            # self.updateSpeciesCombox(self.view.mainWindow.oper_speciesCombox_heightDist)
            self.updateRegionCombox_notAll(self.view.mainWindow.oper_locationField_newRoot)
            # self.updateSpeciesCombox_notAll(self.view.mainWindow.oper_speciesField_newRoot)
            self.updateRegionCombox_notAll(self.view.mainWindow.oper_regionField_arrangeWork)
        except:
            self.view.mainWindow.showSQLErrorInfo("Fail to delete region, ID not found")
            pass
    def substituteWork(self,region,orinalID,newID):
        try:
            cmd="update arrange set m_id=%s where m_id=%s and  area_id= (select area_id from region where location=%s)"
            print(cmd)
            self.sqler.update_para(cmd,(newID,orinalID,region))
            self.sqler.select("select area_id, location, manager_name, m_id from region natural join arrange natural join manager")
            self.view.mainWindow.updateTableView(self.sqler.result, self.view.mainWindow.tableModel_arrangeWork)
        except:
            self.view.mainWindow.showSQLErrorInfo("Could not found correlated IDs")
            pass
    def assignWork(self,region,newID):
        try:
            cmd="insert into arrange values (%s,(select area_id from region where location=%s))"

            self.sqler.insert_para(cmd,(newID,region))
            self.sqler.select("select area_id, location, manager_name, m_id from region natural join arrange natural join manager")
            self.view.mainWindow.updateTableView(self.sqler.result, self.view.mainWindow.tableModel_arrangeWork)
        except:
            self.view.mainWindow.showSQLErrorInfo("Could not found correlated IDs")
            pass
    def revokeWork(self,region,orignalID):
        try:
            cmd="delete from arrange where m_id=%s and area_id=(select area_id from region where location=%s)"
            print(cmd)
            self.sqler.delete_para(cmd,(orignalID,region))
            self.sqler.select("select area_id, location, manager_name, m_id from region natural join arrange natural join manager")
            self.view.mainWindow.updateTableView(self.sqler.result, self.view.mainWindow.tableModel_arrangeWork)
        except:
            self.view.mainWindow.showSQLErrorInfo("Could not found correlated IDs")
            pass
    def newRoot_add(self,plantID,location,species,height):
        try:
            cmd="insert into living values (%s,%s,(select area_id from region where location=%s),%s)"
            print(cmd)
            self.sqler.insert_para(cmd,(plantID,species,location,float(height)))
            self.sqler.select("select ID,location,area_id,species_name,height from living natural join region")
            self.view.mainWindow.updateTableView(self.sqler.result, self.view.mainWindow.tableModel_newRoot)
        except:
            self.view.mainWindow.showSQLErrorInfo("Fail to add new root, make sure your ID is distinct")
            pass
    def newRoot_del(self,plantID,species):
        try:
            cmd="delete from living where ID=%s and species_name=%s "
            self.sqler.delete_para(cmd,(plantID,species))
            self.sqler.select("select ID,location,area_id,species_name,height from living natural join region")
            self.view.mainWindow.updateTableView(self.sqler.result, self.view.mainWindow.tableModel_newRoot)
        except:
            self.view.mainWindow.showSQLErrorInfo("Fail to delete root, make sure you get the correct ID and species")
            pass
    def newSpecies_add(self,familyName,genusName,speciesName,description):
        try:
            cmd="call add_new_species('{testFamily}','{testGenus}','{testSpecies}','{description}')".format(testFamily=familyName,testGenus=genusName,testSpecies=speciesName,description=description)
            self.sqler.call(cmd)
            self.sqler.select("select family_name as Family,genus_name as Genus,species_name as Species ,desp as description from species natural join genus natural join familia",)
            self.view.mainWindow.updateTableView(self.sqler.result,self.view.mainWindow.tableModel_newSpecies)
            # self.updateRegionCombox(self.view.mainWindow.oper_regionCombox_numberDist)
            self.updateSpeciesCombox(self.view.mainWindow.oper_speciesCombox_heightDist)
            # self.updateRegionCombox_notAll(self.view.mainWindow.oper_locationField_newRoot)
            self.updateSpeciesCombox_notAll(self.view.mainWindow.oper_speciesField_newRoot)
            # self.updateRegionCombox_notAll(self.view.mainWindow.oper_regionField_arrangeWork)
        except:
            self.view.mainWindow.showSQLErrorInfo("Fail to add species")
            pass
    def freshGenusCombox(self,familyName):
        self.updateGenusCombox_condition(self.view.mainWindow.genusCombox_inq,familyName)
    def freshSpeciesCombox(self,genusName):
        self.updateSpeciesCombox_condition(self.view.mainWindow.speciesCombox_inq,genusName)
    def displayDescription(self,speciesName):
        self.view.mainWindow.updateTextContent(self.sqler.getSingleValue("select desp from species where species_name='{sn}'".format(sn=speciesName)),self.view.mainWindow.despInfo_inq)
