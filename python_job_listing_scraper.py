import requests
from bs4 import BeautifulSoup
import csv

URL = "https://realpython.github.io/fake-jobs/"

def scrape_jobs():
    response = requests.get(URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    job_cards = soup.find_all("div", class_="card-content")

    jobs = []

    for job in job_cards:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        link = job.find("a")["href"]

        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "link": link
        })

    return jobs


def save_to_csv(jobs, filename="jobs.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["title", "company", "location", "link"]
        )
        writer.writeheader()
        writer.writerows(jobs)


if __name__ == "__main__":
    jobs = scrape_jobs()
    save_to_csv(jobs)
    print(f"Scraped {len(jobs)} jobs successfully!")
