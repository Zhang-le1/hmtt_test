'''
    目标：在unittest框架中使用数据库工具
'''

#导包 unittest 测试工具类
import unittest
from   day02_hmtt.tools.read_db import ReadDB
#新建测试类 继承
class TestDB(unittest.TestCase):
    #新建测试方法
    def test_db(self):
        #定义sql语句
        sql='select is_deleted from news_collection where user_id=1 and article_id=2'
        #调用 get_sql_one()
        data=ReadDB().get_sql_one(sql)
        #调试，查看响应数据
        print(data)
        #断言
        self.assertEqual(0,data[0])

if __name__ == '__main__':
    unittest.main()
