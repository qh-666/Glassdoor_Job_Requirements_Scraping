import pandas as pd
from selenium import webdriver
import re
from selenium.webdriver.support.ui import WebDriverWait

from glassdoor import URL_all
from URL import Item

skills = ["excel", "python", "r", "c","matlab","Linux","sas","java",
          "machine learning","Business Intelligence Tools","Big Data","DBMS","Hive", "HDFS", "Git", "Jenkins",
          "sql", "spss", "tableau", "power bi", "hadoop","dundasBI", "tableau", "powerbi","Excel", "SAS","Qlik"
          "Data Management", "Data Analysis", "Stewardship", "Data warehouse", "relational databases", "data ingestion","ETL",
          "PHP","Javascript","query structure","AI","Airflow","Luigi","Datastage","STEM","MySQL","Excel","AWS","KDD",
            "ESP", "AutoSys", "Netezza","data models", "data dictionarie",
          "spark", "communication", "presentation", "problem solving","Google Analytics","Google API","GIS",
          "project management", "consulting", "leadership","programming","Cognos", "Cubes", "Slate",
          "technical writing", "academic writing","professional writing","Azure","SSRS","Adobe",
          "computer science", "engineering", "information systems","statistics", "mathematics","finance", "economics",
          "phd", "master", "bachelor"]

#use excel to generate this list
re_skills=[r'\bexcel\b',r'\bpython\b',r'\br\b',r'\bc\b',r'\bmatlab\b',r'\blinux\b',
r'\bsas\b',
r'\bjava\b',
r'\bmachine learning\b',
r'\bbusiness intelligence tools\b',
r'\bbig data\b',
r'\bdbms\b',
r'\bhive\b',
r'\bhdfs\b',
r'\bgit\b',
r'\bjenkins\b',
r'\bsql\b',
r'\bspss\b',
r'\btableau\b',
r'\bpower bi\b',
r'\bhadoop\b',
r'\bdundasbi\b',
r'\btableau\b',
r'\bpowerbi\b',
r'\bexcel\b',
r'\bsas\b',
r'\bqlikdata management\b',
r'\bdata analysis\b',
r'\bstewardship\b',
r'\bdata warehouse\b',
r'\brelational databases\b',
r'\bdata ingestion\b',
r'\betl\b',
r'\bphp\b',
r'\bjavascript\b',
r'\bquery structure\b',
r'\bai\b',
r'\bairflow\b',
r'\bluigi\b',
r'\bdatastage\b',
r'\bstem\b',
r'\bmysql\b',
r'\bexcel\b',
r'\baws\b',
r'\bkdd\b',
r'\besp\b',
r'\bautosys\b',
r'\bnetezza\b',
r'\bdata models\b',
r'\bdata dictionarie\b',
r'\bspark\b',
r'\bcommunication\b',
r'\bpresentation\b',
r'\bproblem solving\b',
r'\bgoogle analytics\b',
r'\bgoogle api\b',
r'\bgis\b',
r'\bproject management\b',
r'\bconsulting\b',
r'\bleadership\b',
r'\bprogramming\b',
r'\bcognos\b',
r'\bcubes\b',
r'\bslate\b',
r'\btechnical writing\b',r'\bacademic writing\b',r'\bprofessional writing\b',r'\bazure\b',r'\bssrs\b',
r'\badobe\b',r'\bcomputer science\b',r'\bengineering\b',r'\binformation systems\b',
r'\bstatistics\b',r'\bmathematics\b',r'\bfinance\b',r'\beconomics\b',r'\bphd\b',r'\bmaster\b',r'\bbachelor\b']

i=0
browser = webdriver.Chrome(executable_path='/Users/hq/Downloads/chromedriver 2')
browser.set_page_load_timeout(180)
####
# item=Item()
# item.url='https://www.glassdoor.ca/job-listing/business-systems-data-analyst-imaginit-JV_IC2281069_KO0,29_KE30,38.htm?jl=3487425532&ctt=1583998135288'
# URL_all=[item]
####
for item in URL_all:
    i=i+1
    url=item.url
    browser.get(url)
    element = WebDriverWait(browser, 1000)
    a = browser.find_elements_by_id("JobDescriptionContainer")
    print("---", i, "----")
    for b in a:
        c = b.get_attribute("innerHTML")
        c=c.lower()
        for re_skill in re_skills:
            re_skill=re_skill.lower()
            x = re.search(re_skill, c)
            if x!=None:
                item.skills.append(re_skill[2:-2])
    print(item.skills)

table = pd.DataFrame()
for item in URL_all:
    table = table.append({
        'job_title': item.job_title,
        'company': item.company,
        'location': item.location,
        'skills': item.skills,
        'link': item.url}, ignore_index=True)
table = table.drop_duplicates(['link'], keep='first')
table.to_csv('data1.csv')
