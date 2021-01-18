#导包 requests
import requests
#新建对象类
class ApiChannels(object):

#新建获取用户频道列表的方法
    def api_get_channels(self,url,headers):
        #调用get请求方法
        return requests.get(url,headers=headers)

