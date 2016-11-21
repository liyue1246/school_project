# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
import re
def getImg(picurl): 
    pic = opener.open(picurl).read()
    with open('yzm.jpg','wb') as emptyPic:
        emptyPic.write(pic)

def verifyImg(picpath):    
    pass


def login(coo):
    loginUrl = 'http://ssfw.scuec.edu.cn/ssfw/j_spring_ids_security_check'
    data = {'j_username':'201321093058', 'j_password':'160024', 'validateCode':coo}
#encode the postData
    postData = urllib.urlencode(data)
 
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    header = {'User-Agent':user_agent,'Referer':'http://ssfw.scuec.edu.cn/ssfw/login.jsp'}
#generate a Request with url,postData headers and cookie
    request = urllib2.Request(loginUrl, postData, headers = header)
#post data
    content = opener.open(request)
#get html file
    mainUrl = 'http://ssfw.scuec.edu.cn/ssfw/index.do'
    mainContent = opener.open(mainUrl).read().decode('utf-8')
    print' -----------------mainContent------------------' 
    resulturl='http://ssfw.scuec.edu.cn/ssfw/zhcx/cjxx.do'
    resultcontent= opener.open(resulturl).read().decode('utf-8')
    patte=re.compile('(.*?)<div class="ks-tabs-panel',re.S)
    it=re.search(patte,resultcontent)
    print it
    #print resultcontent
    #pattern=re.compile('class="t_con.*?<td align="center.*?valign="middle">.*?</td>.*?</td>.*?</td>.*?>(.*?)</td>',re.S)
    #prtternn=re.compile('class="t_con.*?<td align="center.*?valign="middle">.*?</td>.*?</td>.*?</td>.*?>.*?</td>.*?</td>.*?</td>.*?</td>.*?>(.*?)</td>',re.S)
    #items=re.findall(pattern,resultcontent)
    #itemss=re.findall(prtternn,resultcontent)
       
       
   
    
    #s= itemss    
    #q= items
    #w=0
   
    #print len(q)
    #print len(s)
    #while w<len(q):
        #print q[w]
        #print s[w]
        
        #w+=1
       
if __name__ == '__main__':
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    picurl = 'http://ssfw.scuec.edu.cn/ssfw/jwcaptcha.do'          
    getImg(picurl)       
    #verifyImg(picpath) 
    verifycode = raw_input('Plz input teh randomcode:')
    print verifycode    
    login(verifycode)