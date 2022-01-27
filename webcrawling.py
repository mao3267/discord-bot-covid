from bs4 import BeautifulSoup
import requests


   
url = "https://covid-19.nchc.org.tw/"

html = requests.get(url,verify=False)

soup = BeautifulSoup(html.text,"html.parser")
covid = soup.select("div.col-lg-3.col-sm-6.col-6.text-center.my-5 p.text-muted span.country_confirmed_percent")
total_covid = soup.select("div.col-lg-3.col-sm-6.col-6.text-center.my-5 h1.country_recovered.mb-1.text-info")
print(covid[1].text)


print("總新增病例"+total_covid[0].text)