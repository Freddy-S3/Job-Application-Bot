import webbrowser
import requests
import bs4


#webbrowser.open('https://www.ziprecruiter.com/jobs-search?search=aws&location=Remote+%28USA%29&company=&days=1&refine_by_salary=&refine_by_employment=employment_type%3Aall&page=1&impression_superset_id=CFRAY%3A830dcbe04ad85407-IAD')

#TODO: Auto apply 1 click (simple) //no responses

res = requests.get('https://www.ziprecruiter.com/jobs-search?search=aws&location=Remote+%28USA%29&company=&days=1&refine_by_salary=&refine_by_employment=employment_type%3Aall&page=1&impression_superset_id=CFRAY%3A830dcbe04ad85407-IAD')
print(len(res))

ZipSoup = bs4.BeautifulSoup(res.text, 'html.parser')

OneClickApply = ZipSoup.select('#zds-2')
print(len(OneClickApply))

#TODO: Schedule task every evening


#TODO: Request manual entry for unrecognized questions
	#PTODO: Save manual entries

#PTODO: ChatGPT integration to answer questions

#PTODO: Identify Best matches for US

#PTODO: Text Copy Buttons
