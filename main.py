import webbrowser
import requests
import bs4
import time
import config, constants
from selenium import webdriver

ZIP_RECRUITER_US_AWS_URL = "https://www.ziprecruiter.com/jobs-search?search=aws&location=Remote+%28USA%29&company=&days=1&refine_by_salary=&refine_by_employment=employment_type%3Aall&page=1&impression_superset_id=CFRAY%3A830dcbe04ad85407-IAD"


#webbrowser.open('https://www.ziprecruiter.com/jobs-search?search=aws&location=Remote+%28USA%29&company=&days=1&refine_by_salary=&refine_by_employment=employment_type%3Aall&page=1&impression_superset_id=CFRAY%3A830dcbe04ad85407-IAD')

#TODO: Auto apply 1 click (simple) //no responses
"""
#TEST CODE
res = requests.get(ZIP_RECRUITER_US_AWS_URL)
print(len(res))

ZipSoup = bs4.BeautifulSoup(res.text, 'html.parser')

OneClickApply = ZipSoup.select('#zds-2')
print(len(OneClickApply))
"""


browser = webdriver.Firefox()
browser.get(ZIP_RECRUITER_US_AWS_URL)



try:
    time.sleep(5.0)
    linkElem = browser.find_element_by_link_text('Sign in here')
    print('Found <%s> element with that class name!' % (linkElem.tag_name))

except:
    print("hello")

input() #to prevent window from closing

#Manual Captcha 






#TODO: Schedule task every evening


#TODO: Request manual entry for unrecognized questions
	#PTODO: Save manual entries

#PTODO: ChatGPT integration to answer questions

#PTODO: Identify Best matches for US

#PTODO: Text Copy Buttons
