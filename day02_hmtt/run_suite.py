'''
    目标：
        1、搜索组装测试他套件
        2、运行测试套件并生成测试报告
'''
#导包 unittest HTMLTestRunner time
import sys
import os
import unittest
import time
parent_dir=os.path.join(os.path.dirname(os.getcwd()))
sys.path.append(parent_dir)

from day02_hmtt.tools.HTMLTestRunner import HTMLTestRunner
# from HTMLTestRunner import  HTMLTestRunner

if __name__ == '__main__':


    #第一步：组装测试套件
    suite=unittest.defaultTestLoader.discover("./case",pattern="test*.py")
    #第二步：指定报告存放路径及文件名称
    file_path="./report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))
    #第三步：运行测试套件并生成测试报告
    with open(file_path,"wb")as f:
        HTMLTestRunner(stream=f).run(suite)