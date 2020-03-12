# Glassdoor Job Requirements Skills Scraping
Scrape the job title, location, company and required skills in glassdoor

#
### This repository is part of a course project, not for commercial purposes
![](<csv_screenshot.png>)
#
### Location
"Toronto", "Vancouver","Ottawa","Hamilton","Montreal","Victoria","Winnipeg","Edmonton"
          "Quebec City","Regina","Scarborough","London,ON","Windsor","Vaughan","Richmond Hill"
          
### Job_title
"data analyst","data scientist","data manager"

### Skills
"excel", "python", "r", "c","java"..........."SSRS","Adobe","computer science", "statistics", "mathematics"

Location and Job title can be changed in **glassdoor.py**, skills can be changed in **glassdoor_detail.py**

# Run
**Run** glassdoor_detail.py

**glassdoor.py** will scrape all the combinations of job titles and locations, and render number of pages, and scrape each job's link

**glassdoor_detail.py** will scrape all the job links and get all required skills
