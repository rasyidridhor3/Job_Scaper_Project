import requests
from bs4 import BeautifulSoup
import csv
url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title)

job_cards = soup.find_all("div", class_="card-content")
print(len(job_cards))
with open ("jobs.csv", mode="w",newline="", encoding="utf-8") as file :
    writer = csv.writer(file)
    writer.writerow(["title","company", "location", "link"])

    for job in job_cards:

     title = job.find("h2").text.strip()   
     company = job.find("h3").text.strip()
     location = job.find("p").text.strip()
     
     link = job.find("a")("href")
     
     writer.writerow([title,company,location,link])
print("Data berhasil disimpan ke jobs.csv")

