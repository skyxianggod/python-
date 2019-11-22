#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests,re
class Qsbk(object):
    '''抓取页面'''
    def __get_html(self,url):
        html=requests.get(url).content.decode()
        return html
    # '''匹配输出当前页面的段子'''
    def print_qsbk(self,url):
        ret=self.__get_html(url)
        Items=re.findall('<div class="content">.*?<span>(.*?)</span>.*?</div>',ret,re.S)
        #输出每页的段子#
        items=[]
        for item in Items:
            item=item.replace('\n','').replace('<br/>','')
            items.append(item)
        print("当前抓取的段子")
        for i,item in enumerate(items):
            print(i+1,item,"\n")

    def start_print(self):
        b=1
        while True:
            a=input('c/q:').strip()
            if a=='c':
                url='https://www.qiushibaike.com/8hr/page/'+str(b)
                b+=1
                self.print_qsbk(url)
            else:
                break
hot_Qsbk=Qsbk()
hot_Qsbk.start_print()
