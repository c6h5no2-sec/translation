# -*- coding: utf-8 -*-
import win32clipboard as w
import win32con
import xlrd
import time
import keyboard


class listen(object):
    #获取剪切板内容
    def getText(self):
        w.OpenClipboard()
        t =w.GetClipboardData(win32con.CF_TEXT)
        w.CloseClipboard()
        try:
            copy=t.decode('UTF-8')
            #print(type(copy))
        except:
            copy=t.decode('gbk')
            #print(type(copy))
        return copy

    #写入剪切板内容
    def setText(self,aString):
        #aString = "1234"
        w.OpenClipboard()
        w.EmptyClipboard()
        #w.SetClipboardData(win32con.CF_TEXT, aString)
        w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
        w.CloseClipboard()
        time.sleep(1)


    '''
    def f(self):
       a=self.gettext()
       print(a)
       try:
           #此模块用于监听后需要干啥
           result = "asdfasdf"
           result=bytes(result,encoding="gbk")#剪切板复制的要是个字节流
       except:
           result="error"
           print("error")
           result=bytes(result,encoding="utf-8")
       self.settext(result)
       self.clean()
    '''

      #定时清除剪切板内容，增加安全性
    def  clean(self):
        time.sleep(10)
        self.setText('请输入内容')
        #监听
"""
#主函数
if __name__ == "__main__":
        author = "Powered by C6H5NO2"
        author = bytes(author,encoding="gbk")
        lis = listen()
        
        lis.settext(author)
        keyboard.add_hotkey('ctrl+space',lis.f)
        keyboard.wait()
"""