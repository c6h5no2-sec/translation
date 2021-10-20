# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.tmt.v20180321 import tmt_client, models

class translate(object):
    '''
    def __init__(self,word):
        self.word = word
    '''

    def transToChinese(self,word):
        #查中文意思
        word = word
        url="http://dict.youdao.com/w/" + word
        res=requests.get(url,timeout=10)
        try:
            if res.status_code == requests.codes.ok:
                text=res.text
                #print("+++++++++++++++++++++++++++++++\n")
                #print(url+"爬取完毕\n")
                #print(text)
                search=re.compile(r"<li>.[^a].*?</li>")
                #匹配<li></li>下的某个字符的非a
                search=search.findall(text)
                #print(search)
                #匹配出所有
                search='\r\n'.join(search)
                #print(search)
                #匹配出来的<li></li>通过换行进行分隔
                search=search.replace("<li>","")
                search=search.replace("</li>","")
                #print(search)
                if len(search)!=0 :
                    return search
                else:
                    #print(search)
                    search = "没有找到相关意思:" + word
                    return search
            else:
                #print("+++++++++++++++++++++++++++++++")
                text=url+"爬取失败\n"
                return text
        except:
                return "出现意外错误"

    def transToEnglish(self,word):
        #中翻英
        
        word = word
        #print(type(word))
        url="http://dict.youdao.com/w/" + word
        res=requests.get(url,timeout=10)
        try:
            if res.status_code == requests.codes.ok:
                text=res.text
                #print("+++++++++++++++++++++++++++++++\n")
                #print(url+"爬取完毕\n")
                #print(text)
                soup=BeautifulSoup(text,"html.parser")
                a=soup.find_all("p",class_="wordGroup")
                #print(len(a))
                #<p>段落下属性为wordGroup

                if len(a)==0 :
                    text="没有找到相关单词" + word
                    return text
                else:
                    c=''
                    d=''
                    try:
                        for i in a:
                            b=i.find_all("span")[1].text
                            #span标签
                            a=i.find_all("span")[0].text
                            c=a+b+"  "+c
                        return c
                    except:
                        c = c.replace("\n",'')
                        #c = bytes(c,encoding="gbk")
                        if len(c) == 0:
                            c = "试试用ctrl+alt吧"
                        return c
            else:
                #print("+++++++++++++++++++++++++++++++")
                text=url+"爬取失败，请检测网络连接\n"
                return text

        except:
            text = "fail"
            return text

    def transToSentence(self,text):
        try:
            #word='english'
            cred = credential.Credential("AKIDMRO7YuAdeOq3yzTFSN8furYziFVUqW9K", "4qLbbNr3ycz6yZw42PbZJmCWalgAUXJo")
            httpProfile = HttpProfile()
            httpProfile.endpoint = "tmt.tencentcloudapi.com"
            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            client = tmt_client.TmtClient(cred, "ap-chengdu", clientProfile) 

            rep = models.LanguageDetectRequest()
            params1 = '{\"Text\":\"'+text+'\",\"ProjectId\":1188900}'


            rep.from_json_string(params1)

            #文本转换
            res=client.LanguageDetect(rep)
            #print(res.to_json_string())
            #文本识别        
            la=res.to_json_string()[10:12]
            #print(la)
            #输出语种

            if la=='zh':
                lan ='en'
            elif la== 'en':
                lan = 'zh'

            req = models.TextTranslateRequest()
            params = '{\"SourceText\":\"'+text+'\",\"Source\":\"auto\",\"Target\":\"'+lan+'\",\"ProjectId\":0}'
            req.from_json_string(params)
            resp = client.TextTranslate(req)
            #print (resp.to_json_string())
            a=resp.to_json_string()
            #print(a[15])
            leng=a.find("\",")
            result = a[16:leng]
            #print(result)
            return result
        except TencentCloudSDKException as err:
            result="翻译的句子有误，请重试"
            #print("error")
            return result
'''
使用方法
a = translate()
word="asdf"
a.transChinese(word)

a = translate()
word = "吃饭"
b = a.transToEnglish(word)
print(b)
'''
