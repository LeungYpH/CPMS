import pymysql

class SQLResult():
    def __init__(self,cursor):
        self.data=cursor.fetchall()
        self.desp=self.getTitle(cursor.description)

    def getTitle(self,desp):
        title=[]
        for elem in desp:
            title.append(elem[0])
            # print(elem[0])
        return title
class SQLOperator():
    # mysql_conn = pymysql.connect(host='localhost', port=3306, user='root', password='Alexriddle0112', db='treemanage')
    def __init__(self,user,pwd):
        self.mysql_conn = pymysql.connect(host='localhost', port=3306, user=user, password=pwd,
                                     db='cpms')
        self.title = []
    def select(self,sqlCommand):
        try:
            with self.mysql_conn.cursor() as cursor:
                # print("echo1")

                cursor.execute(sqlCommand)
                self.result = SQLResult(cursor)
                # self.description=self.getTitle(cursor.description)
                self.showResult()
        except Exception as e:
            print("error")
            self.result.data = None

    def update(self,sqlCommand):
        try:
            with self.mysql_conn.cursor() as cursor:
                cursor.execute(sqlCommand)
                self.mysql_conn.commit()

        except Exception as e:
            self.mysql_conn.rollback()
            print("error")
    def insert(self,sqlCommand):
        try:
            with self.mysql_conn.cursor() as cursor:
                cursor.execute(sqlCommand)
                self.mysql_conn.commit()
        except Exception as e:
            self.mysql_conn.rollback()
            print("error")
    def deleted(self,sqlCommand):
        try:
            with self.mysql_conn.cursor() as cursor:
                # print("echo1")
                cursor.execute(sqlCommand)
                self.mysql_conn.commit()
        except Exception as e:
            self.mysql_conn.rollback()
            print("error")
    def call(self,sqlCommand):
        try:
            with self.mysql_conn.cursor() as cursor:
                cursor.execute(sqlCommand)
                self.mysql_conn.commit()
        except Exception as e:
            print("error")
            self.mysql_conn.rollback()
    def showResult(self):
        if self.result.data is None:
            return
        print(self.result.desp)
        for res in self.result.data:
            for elem in res:
                print(elem,end='\t')
            print()
    def getComboxList(self,sqlCommand):
        targetList=["ALL"]
        try:
            with self.mysql_conn.cursor() as cursor:
                cursor.execute(sqlCommand)
                data=cursor.fetchall()
                for elem in data:
                    targetList.append(elem[0])
        except Exception as e:
            print("error")
        return targetList
    def getComboxList_noneAll(self,sqlCommand):
        targetList=[]
        try:
            with self.mysql_conn.cursor() as cursor:
                cursor.execute(sqlCommand)
                data=cursor.fetchall()
                for elem in data:
                    targetList.append(elem[0])
        except Exception as e:
            print("error")
        return targetList
    def select_para(self,cmd,paras):
        try:
            with self.mysql_conn.cursor() as cursor:
                # print("echo1")

                cursor.execute(cmd,paras)
                self.result = SQLResult(cursor)
                # self.description=self.getTitle(cursor.description)
                self.showResult()
        except Exception as e:
            print("error")
            self.result.data = None
    def insert_para(self,sqlCommand,paras):
        try:
            with self.mysql_conn.cursor() as cursor:
                cursor.execute(sqlCommand,paras)
                self.mysql_conn.commit()
        except Exception as e:
            self.mysql_conn.rollback()
            print("error")
    def delete_para(self,sqlCommand,paras):
        try:
            with self.mysql_conn.cursor() as cursor:
                # print("echo1")
                cursor.execute(sqlCommand,paras)
                self.mysql_conn.commit()
        except Exception as e:
            self.mysql_conn.rollback()
            print("error")
    def update_para(self,sqlCommand,paras):
        try:
            with self.mysql_conn.cursor() as cursor:
                cursor.execute(sqlCommand,paras)
                self.mysql_conn.commit()
        except Exception as e:
            self.mysql_conn.rollback()
            print("error")
    def call_para(self,sqlCommand,paras):
        try:
            with self.mysql_conn.cursor() as cursor:
                cursor.execute(sqlCommand)
                self.mysql_conn.commit()
        except Exception as e:
            print("error")
            self.mysql_conn.rollback()
    def getSingleValue(self,sqlCommand):
        try:
            with self.mysql_conn.cursor() as cursor:
                cursor.execute(sqlCommand)
                data=cursor.fetchall()
                return data[0][0]
        except Exception as e:
            print("error")
            # self.mysql_conn.rollback()

class SQLCounter(SQLOperator):
    def __init__(self,user,pwd):
        super(SQLCounter, self).__init__(user,pwd)


if __name__=='__main__':
    sqlTest=SQLOperator('root','Alexriddle0112')
    # cmd="select * from manager"
    # cmd2="insert into arrange values(%s,%s)"
    # para=("Comp. Bio.")
    # sqlTest.select_para(cmd,para)
    # sqlTest.insert_para(cmd2,('20003','A00001'))
    print(sqlTest.getSingleValue("select desp from species where species_name='Rosa ssp.'"))
    # try:
    #     connection = pymysql.connect(
    #         host="localhost",
    #         port=3306,
    #         user="root",
    #         password="Alexriddle0112",
    #         database="cpms"
    #     )  # 创建数据库连接
    #     cursor = connection.cursor()  # 声明数据游标
    #
    #     sql = "select * from %s where dept_name='Comp. Bio.'"  # 被调用 SQL 语句
    #     data_tuple = ('manager' )  # 传入的参数元组
    #
    #     cursor.execute(sql,data_tuple)  # 执行 SQL 语句
    #     res=cursor.fetchall()
    #     for elem in res:
    #         print(elem)
    #
    # except Exception as error:
    #     connection.rollback()  # 执行失败，数据回滚
    #     print(f"参数化查询执行异常：{error}")
    # .format(table='living',label='species_name',something='Osmanthus sp.')
    # print(cmd)
    # cmd2="insert into manager values('12321','Bio. Qiangji','13698918273','Wang Zikun')"
    # cmd3="select * from manager"
    # sqlTest2=SQLOperator('root','Alexriddle0112')
    # sqlTest.insert(cmd2)
    # sqlTest.select(cmd3)
    # sqlTest.showResult()


