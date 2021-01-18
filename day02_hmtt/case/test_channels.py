#导包 unittest  ApiChannels
import unittest
from day02_hmtt.api.api_channels import ApiChannels
from parameterized import parameterized
from day02_hmtt.tools.read_json import ReadJson

def get_data():
    data = ReadJson("channels.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("expect_result"),
                 data.get("status_code")))
    return arrs

#新建测试类 继承
class TestChannels(unittest.TestCase):
    #新建测试方法
    @parameterized.expand(get_data())
    def test_channels(self,url,headers,expect_result,status_code):
        #临时数据
        # url="http:///ttapi.research.itcast.cn/app/v1_0/user/channels"
        # #注意：token信息和Bearer之间有一个空格
        # headers={"Content-Type":"application/json",
        #          "Authorization":"Bearer token信息"}
        #调用获取用户频道 列表的方法
        r=ApiChannels().api_get_channels(url,headers)

        #调试信息，打印响应结果
        print(r.json())
        #断言 状态码
        # self.assertEqual(200, r.status_code)
        self.assertEqual(status_code,r.status_code)

        #断言 响应信息
        # self.assertEqual("OK", r.json()['message'])
        self.assertEqual(expect_result,r.json()['message'])

if __name__ == '__main__':
    unittest.main()