from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup
import re
import urllib
import os
import sys

try:
    fp = open(os.path.join(sys.path[0], 'user.txt'), 'r')
    user = fp.read()
finally:
    fp.close()

try:
    fp = open(os.path.join(sys.path[0], 'password.txt'), 'r')
    userpass = fp.read()
finally:
    fp.close()


workorders = []
tracking = []
assignments = []
contact = []
company = []

browser = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
browser.get ('https://www.workmarket.com/login')
time.sleep(3)
loginUser = browser.find_element_by_css_selector('#login-email')
loginUser.send_keys(user)
password = browser.find_element_by_css_selector('#login-password')
password.send_keys(userpass)
button = browser.find_element_by_css_selector('#login_page_button > span')
button.click()
time.sleep(3)
browser.get('https://www.workmarket.com/assignments#status/active/managings')
#time.sleep(1)
#browser.find_element_by_css_selector("select#assignment_list_size > option[value='50']").click()
time.sleep(3)
soup = BeautifulSoup(browser.page_source,features="html5lib")



for link in soup.find_all('a', href=re.compile("/assignments/details/")):
    print ('https://www.workmarket.com{}'.format(link['href']))
    assignments.append('https://www.workmarket.com{}'.format(link['href']))

for i in range(len(assignments)):
    browser.get(assignments[i])
    time.sleep(3)
    soup = BeautifulSoup(browser.page_source,'html.parser')

    temp = soup.select('#pane-buyer-custom-fields > div:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(2) > textarea')
    m = re.search('value="(.+?)"', str(temp))
    if m:
        workorders.append(m.group(1))
    else:
        workorders.append("")
    print(workorders[i])
    #print (temp)

    temp = soup.select('#pane-buyer-custom-fields > div:nth-child(2) > table > tbody > tr:nth-child(10) > td:nth-child(2) > textarea')
    m = re.search('value="(.+?)"', str(temp))
    if m:
        tracking.append(m.group(1))
    else:
        tracking.append("")
    print(tracking[i])
    #print (temp)

    contactdetails = soup.select('#outer-container > div > div.row_details_assignment > div.sidebar.worker-map > div:nth-child(4) > div > p:nth-child(3) > strong')
    contactdetails += soup.select('#outer-container > div > div.row_details_assignment > div.sidebar.worker-map > div:nth-child(4) > div > p:nth-child(4)')
    contact.append(contactdetails)
    #print(contact[i])
    
    temp = soup.select('#outer-container > div > div.row_details_assignment > div.sidebar.worker-map > div.well-b2.intro-summary > div.well-content > dl:nth-child(2) > dd > strong')
    m = re.search('<strong>(.+?)</strong>', str(temp))
    if m:
        company.append(m.group(1))
    else:
        company.append("")
    print(company[i],"\n")
    #print (temp)


    