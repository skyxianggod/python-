#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
Movie_list=[]
url=Url='https://movie.douban.com/top250'
def get_html(url):
    html=requests.get(url).content.decode()
    # print(html)
    return html


def html_decode(html):
    group=BeautifulSoup(html)
    movie_list=group.find('ol',attrs={'class':'grid_view'})
    print(movie_list,"---")
    movie_list_tiltle=movie_list.find_all('li')
    # movie_list_title=movie_list.findall('li')
    # print(movie_list_tiltle)
    for li in movie_list_tiltle:
        movie_name=li.find('span',attrs={'class':'title'}).getText()
        Movie_list.append(movie_name)

        # print(movie_name)
    # print(Movie_list)
    next_page=group.find('span',attrs={'class':'next'}).find('a')
    print(next_page['href'])
    if next_page:
        return Movie_list,Url+next_page['href']
    return Movie_list,None
while True:
    try :
        if url:
            ret=get_html(url)
            result=html_decode(ret)
            url=result[1]
            continue
    except TypeError as e:
        print(e)
        fp=open("./movie.txt",'w+',encoding='utf-8')
        for i in  result[0]:
            fp.write(i+'\n')
        fp.close()
        break

