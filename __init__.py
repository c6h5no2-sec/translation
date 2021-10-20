import keyboard
import translation
import listenKeyboard
import re



if __name__ == "__main__":
        author = "press 'ctrl+space' will translate word or you can press'ctrl+alt' to translate a sentence\r\nPowered by C6H5NO2"
        #author = bytes(author,encoding="gbk")

        #创建对象
        lis = listenKeyboard.listen()
        tran = translation.translate()

        lis.setText(author)
        #建议帮助文档以及作者信息
        """
        def toEnglish():
        #中翻英
               text = lis.getText()
               result = tran.transToEnglish(text)
               print(text)
               a=lis.setText(result)
               print(a)
        
        def toChinese():
        #英翻中
               text = lis.getText()
               result = tran.transToChinese(text)
               #print(result)
               a=lis.setText(result)
               print(a)

        keyboard.add_hotkey('ctrl+space',toEnglish)
        keyboard.add_hotkey('ctrl+alt',toChinese)
        keyboard.wait()
        """
        def trans():
               text = lis.getText()
               #print(text)
               se=re.compile(r"[a-zA-Z]")
               se=se.findall(text)
               sea=''.join(se)
               #如果是单词
               if len(sea)!=0:
                      word_search= tran.transToChinese(sea)
                      #提取单词
                   
               #如果是中文
               else :
                      #print("中文")
                      word_search= tran.transToEnglish(text)
                      
               a = lis.setText(word_search)
               #lis.clean()
               return a
        def transSentence():
               #翻译句子
               text = lis.getText()
               text = tran.transToSentence(text)
               a = lis.setText(text)
               #lis.clean()
               return a


        keyboard.add_hotkey('ctrl+space',trans)
        keyboard.add_hotkey('ctrL+alt',transSentence)
        keyboard.wait('esc')