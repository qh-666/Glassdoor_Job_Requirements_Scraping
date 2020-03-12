from selenium import webdriver
from URL import Item

locations=["Vancouver","Ottawa","Hamilton","Montreal","Victoria","Winnipeg","Edmonton"
          "Quebec City","Regina","Scarborough","London,ON","Windsor","Vaughan","Richmond Hill"]
job_title=["data analyst","data scientist","data manager"]

# create a new Firefox session
browser = webdriver.Chrome(executable_path = '/Users/hq/Downloads/chromedriver 2')
browser.set_page_load_timeout(180)

URL_all=[]#all url for every job
URL_allpages=[] #all url for all page
URL_start=[]#store urls for every combination of location & job title
pages=[]

#create all urls for URL_start
start_url="https://www.glassdoor.ca/Job/toronto-data-analyst-jobs-SRCH_IL.0,7_IC2281069_KO8,20.htm"
URL_start.append(start_url)
browser.get(start_url)
page_num = browser.find_element_by_xpath("//input[@id='TotalPages']").get_property("value")
pages.append(page_num)
for job in job_title:
    try:
        change_job_name = browser.find_element_by_xpath("//input[@id='sc.keyword']")
        change_job_name.clear()
        change_job_name.send_keys(job)
    except:
        print("did not get job")
    for location in locations:
        print("Combination for",job,"and",location)
        try:
            change_location = browser.find_element_by_xpath("//input[@id='sc.location']")
            change_location.clear()
            change_location.send_keys(location)
            browser.find_element_by_xpath("//button[@id='HeroSearchButton']").click()
        except:
            print("did not get url from",location)
        browser.refresh()
        current_url = browser.current_url
        print(current_url)
        URL_start.append(current_url)
        # get number of page
        try:
            page_num = browser.find_element_by_xpath("//input[@id='TotalPages']").get_property("value")
            pages.append(page_num)
        except:
            print("did not get number of page")
print("----all combinations are finished-----")
print("----URL list len is",len(URL_start),"-----")
print(pages)
print(URL_start)

#extend url with pages
i=0
for i in range(len(pages)):
    page=pages[i]
    url=URL_start[i]
    for j in range(int(page)+1):
        if j==0:
            continue
        if j == 1:
            url_temp = url;
        else:
            url_temp = url[:-4] + "_IP" + str(j) + ".htm"
        URL_allpages.append(url_temp)
print("-----total",len(URL_allpages),"pages----")

for url in URL_allpages:
    browser.get(url)
    a = browser.find_elements_by_xpath("//td[@class='job_title']/a")#both jobtitle and joblink
    b = browser.find_elements_by_xpath("//td[@class='company']/span")#company name
    c = browser.find_elements_by_xpath("//td[@class='location']/span")#location
    for i in range(len(a)):
        #print(i)
        item=Item();#new object
        item.url = a[i].get_attribute("href")
        item.job_title=a[i].get_attribute("innerHTML")
        item.location=c[i].get_attribute("innerHTML")
        item.company=b[i].get_attribute("innerHTML")
        URL_all.append(item)

print("----All jobs:",len(URL_all),"----")
# for item in URL_all:
#     print(item.url)
#     print(item.company)
#     print(item.location)
#     print(item.job_title)