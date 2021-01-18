#导包 unittest ApiArticle
import unittest
from day02_hmtt.api.api_article import ApiArticle
from parameterized import parameterized
from day02_hmtt.tools.read_json import ReadJson


def get_data_add():
    data = ReadJson("article_post.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("data"),
                 data.get("expect_result"),
                 data.get("status_code")))
    return arrs

def get_data_cancel():
    data = ReadJson("article_delete.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("status_code")))
    return arrs
#新建测试类  继承
class TestArticle(unittest.TestCase):
    #新建测试收藏文章方法
    @parameterized.expand(get_data_add())
    def test01_post_article(self,url,headers,data,expect_result,status_code):
        #临时数据
        # url="http:///ttapi.research.itcast.cn/app/v1_0/article/collections"
        # headers={"Content-Type":"application/x-www-form-urlencoded",
        #         "Authorization":"Bearer token信息"}
        # data={"target":"1"}
        #调用收藏文章方法
        r=ApiArticle().api_post_article(url,headers,data)
        #调试 查看响应数据结果
        print("收藏响应数据为：",r.json())
        #断言状态码
        # self.assertEqual(201,r.status_code)
        self.assertEqual(status_code, r.status_code)
        #断言响应信息
        # self.assertEqual("OK)",r.json()["message"])
        self.assertEqual(expect_result, r.json()["message"])


    #新建测试取消收藏文章方法
    @parameterized.expand(get_data_cancel())
    def test02_delete_article(self,url,headers,status_code):
        #临时数据
        # url="http:///ttapi.research.itcast.cn/app/v1_0/article/collections/1"
        # headers={"Content-Type":"application/x-www-form-urlencoded",
        #          "Authorization":"Bearer token信息"}
        #调用取消收藏文章方法
        r=ApiArticle().api_delete_article(url,headers)
        #调试 获取响应状态码
        print("取消收藏响应状态码为：",r.status_code)
        #断言状态码
        # self.assertEqual(204,r.status_code)
        self.assertEqual(status_code, r.status_code)

if __name__ == '__main__':
    unittest.main()