#导包 json
import json

# #打开json文件并获取文件流
# with open("../data/login.json","r",encoding="utf-8")as f:
#     #调用load方法加文件流
#     data=json.load(f)
#     print("获取的数据为：",data)

#使用函数进行封装
# def read_json():
#     with open("../data/login.json","r",encoding="utf-8")as f:
#         #调用load方法加文件流
#         return json.load(f)

#使用参数替换静态文件名（以类的方法）
class ReadJson(object):
    def __init__(self,filename):
        self.filepath="../data/"+filename

    def read_json(self):
        with open(self.filepath,"r",encoding="utf-8")as f:
            #调用load方法加文件流
            return json.load(f)

'''
    问题：
        1、未经封装无法在别的模块中使用
        2、数据存储文件有好几个，如果把导入文件名写死，在读取别的文件时无法使用
        3、预期格式为列表嵌套元组[(url,mobile,code)],但是目前返回的是字典
        4、多个参数预期格式为列表嵌套元组[(url,mobile,code)，(url,mobile,code)，……],但是目前返回的是字典
    解决：
        1、进行封装
        2、使用参数替换静态写死的文件名
        3、读取字典中的内容，并添加到新的列表中
        4、利用字典中values（）方法读取所有的值
'''

if __name__=='__main__':
    # print(ReadJson("login.json").read_json())
    datas=ReadJson("login_more.json").read_json()
    arrs=[]
    #使用遍历获取所有的value
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("mobile"),
                     data.get("code"),
                     data.get("expect_result"),
                     data.get("status_code")))
    print(arrs)