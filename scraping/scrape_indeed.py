

import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.indeed.com/jobs?q=software+developer&l="
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

job_descriptions = []
for job in soup.find_all("div", class_="job_seen_beacon"):
    title = job.find("h2").text.strip() if job.find("h2") else "N/A"
    company = job.find("span", class_="companyName").text.strip() if job.find("span", class_="companyName") else "N/A"
    description = job.find("div", class_="job-snippet").text.strip() if job.find("div", class_="job-snippet") else "N/A"

    job_descriptions.append({"title": title, "company": company, "description": description})

# Save to JSON
with open("../data/job_descriptions/software_jobs.json", "w") as f:
    json.dump(job_descriptions, f, indent=4)

print("✅ Job descriptions saved!")
