# python3.6.5
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests
from ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/1274-2","119070","5183ccbb187e48bab5cea7d8c977b13c" )
#r.addBodyPara("imgUrl", "http://pic.4j4j.cn/upload/pic/20130528/a9117a5351.jpg")
#r.addBodyPara("base64", "")
r.addFilePara("imgFile", "C:/Users/高泽静/PycharmProjects/test/bg_img/imooc1.png")
res = r.post()
#print(res.text)
#取json里的值
text = res.json()['showapi_res_body']['texts']
print(text) # 返回信息
