'''
from selenium  import  webdriver
browser  =  webdriver.PhantomJS()
browser.get('https://www.baidu.com')
print(browser.current_url)

from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>Hello</p>','lxml')
print(soup.p.string)


from flask import Flask
app  =  Flask(__name__)

@app.route("/")
def hello():
    return"Hello  World !"

if  __name__ =="__main__":
    app. run()

'''

import scrapy_redis