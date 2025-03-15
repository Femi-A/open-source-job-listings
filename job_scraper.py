import requests
from bs4 import BeautifulSoup

# URL of job postings (Modify as needed)
URL = "https://angel.co/jobs"

# Fetch the page content
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Extract job listings (Modify selectors based on site structure)
jobs = []
for job in soup.find_all("div", class_="job_listing"):
    title = job.find("h2").text.strip()
    company = job.find("h3").text.strip()
    location = job.find("span", class_="location").text.strip()
    link = job.find("a")["href"]

    jobs.append({
        "Company": company,
        "Title": title,
        "Location": location,
        "Link": f"https://angel.co{link}"
    })

# Convert to markdown format
markdown_content = "### Wellfound Job Listings\n\n"
for job in jobs:
    markdown_content += f"- **[{job['Company']}]** - {job['Title']} ({job['Location']})\n"
    markdown_content += f"  - Apply: [{job['Link']}]({job['Link']})\n\n"

# Save to markdown file inside the repo
file_path = "Internships/Remote_Internships.md"
with open(file_path, "w", encoding="utf-8") as file:
    file.write(markdown_content)

print("Job listings updated successfully!")
