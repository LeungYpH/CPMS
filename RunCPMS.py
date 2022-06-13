"""
备忘录：
1. Controller中加入 错误提示类，里面含一个弹窗，根据提供的报错字符串生成报错窗口。
2. 添加 Reset/Clear按钮
3. 开始即更新
"""

from Controller import *
import sys

class Run():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ctrl = Controller()
    def runCPMS(self):
        self.ctrl.runLogin()
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    run=Run()
    run.runCPMS()
