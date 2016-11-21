import urllib2
import urllib
import re
from lxml import etree
from threading import Thread
#coding=utf-8


def baocun(img,imgq):
    q=str(img)
    urllib.urlretrieve(img,'meinv/%s.jpg' %q[-15:-7] )
    print 'save a photo'




def getimg(address):

    tou="http://desk.zol.com.cn"
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    requestt=urllib2.Request(address)
    responsee=urllib2.urlopen(requestt,timeout=20).read()

    ipattern=re.compile('id="1920x1080.*?href="(.+?\.html)"',re.S)
    try:
        foimg=re.search(ipattern,responsee).group(1)

        furl=tou+foimg

        frequest=urllib2.Request(furl)
        fresponse=urllib2.urlopen(frequest,timeout=20).read()
        fpatternn=re.compile('<img src="(.*?)"',re.S)
        imgq=re.findall(fpatternn,fresponse)
        for img in imgq:
            #print img
            t=Thread(target=baocun,args=(img,imgq))
            t.start()



    except:
        print 'failed'





def listimg(iurl):
    #print iurl
    #tupian_url=urllib2.urlopen(image_url,timeout=60).read()
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    list_request=urllib2.Request(iurl)
    list_response=urllib2.urlopen(list_request,timeout=30).read()

    page=etree.HTML(list_response.lower())

    hreaf=page.xpath("//div[@class=' wrapper photo-set mt15']/div[@class='photo-set-list']/div/div/ul/li/a/@href")
    tou="http://desk.zol.com.cn"
    #print hreaf
    for item in hreaf:

        address=tou+item
        #print address
        try:
            getimg(address)
        except:
            pass



def imgurl(url):


    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }

    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request,timeout=30).read()

    pattern=re.compile('<li class="photo-list-padding.*?href="(.+?\.html)"',re.S)
    items=re.findall(pattern,response)
    tou="http://desk.zol.com.cn"

    for item in items:
        iurl=tou+item
        try:
            listimg(iurl)
        except:
            pass


def main():
    i=1
    star_url='http://desk.zol.com.cn/meinv/'
    html=".html"
    while i<65:
        print'------------------------------------'
        print'the %s'%i
        print'------------------------------------'
        qurl=star_url+str(i)+html
        imgurl(qurl)
        i+=1
if __name__=='__main__':
    main()


