# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import pandas as pd

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
# options.add_argument('--headless')
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://linkedin.com/uas/login")
# time.sleep(5)
# soup=BeautifulSoup(driver.page_source, 'lxml')

# username = driver.find_element(By.ID,"username")
# # Enter Your Email Address
# username.send_keys("sonali.1994mychoice@gmail.com")
# pword = driver.find_element(By.ID,"password")
# # Enter Your Password
# pword.send_keys("bhAbAni9006")		
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# time.sleep(3)


# area_of_search = "python"
# URL = "https://www.linkedin.com/search/results/all/?keywords="+area_of_search
# driver.get(URL)

# links = []
# designation_l,company_l,location_l,post_date_l=[],[],[],[]
# job_type_l,employees_l,description_l=[],[],[]
# s=driver.find_elements(By.XPATH,'//*[@id="main"]/div/div/div[1]/div[2]/a')
# for i in s:
#     links.append(i)
#     time.sleep(3)
#     i.click()


#     time.sleep(10)

#     hi =driver.find_elements(By.XPATH,'//*[@id="main"]/div/section[1]/div/ul/li')
#     for item in hi:
#         time.sleep(5)
#         item.click()
#     # print(len(hi))
#         list1 =[]
#         list2=[]
        

#         designation = driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/a/h2').text
#         # designation_partial = driver.find_element(By.CLASS_NAME,'//*[@class="t-24 t-bold jobs-unified-top-card__job-title"]').text
#         # designation = soup.find(attrs={'class':"t-24 t-bold jobs-unified-top-card__job-title"}).text
#         designation_l.append(designation)      
#         print("designation_partial========>>>>",designation)

        
#         company=driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/span/span').text
#         company_l.append(company)
#         print('company====>>>>',company)

#         location=driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/span/span[2]').text
#         location_l.append(location)
#         print('location======>>>',location)

#         post_date = driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/span[2]/span').text
#         post_date_l.append(post_date)
#         print('post_date========>>>>',post_date)

#         # hello = driver.find_elements(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/ul/li')
#         # print(len(hello))
#         # for item in len(hello):
#         #     # if item == 1:
#         #     job_type = item.find_element(By.TAG_NAME,'span').text
#         #     print(job_type)
            
#         #     if item == 2:
#         #         employee = item.find_element(By.TAG_NAME,'span').text

#         # job_type = driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/ul/li/span').text 
#         time.sleep(3)
#         job_type = driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/ul/li[1]/span').text
#                                                 # //*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/ul/li[1]/span
#                                                 # //*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/ul/li[1]/span
#         # job_type = driver.find_elements((By.CLASS_NAME,'jobs-unified-top-card__job-insight')[0]).text
#         job_type_l.append(job_type)
#         print('job_type=====>>>',job_type)

#         employees = driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div[2]/ul/li[2]/span').text
#         employees_l.append(employees)
#         print("employees======>>>",employees)
#         time.sleep(3)
#         description = driver.find_element(By.XPATH,'//*[@id="job-details"]/span').text
#         description_l.append(description)
#         print("description======>>>",description)
#         print("list1=====>>>>>",list1)

# FILE_NAME = 'scrap_linkedin.csv'
# df=pd.DataFrame()
# df['Designation'] = designation_l
# df['Company Name'] = company_l
# df['Location']=location_l
# df['Post Date'] = post_date_l
# df['Job Type'] = pd.Series(job_type_l)
# df['Employees'] = pd.Series(employees_l)
# df['Job Description']=description_l
        
# print(len(df),"???????????????????????????")
# df.to_csv(FILE_NAME,index=False)
#             # post_by = driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[2]').text
#                                                 # //*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/a/span
#                                                 # //*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[2]
#                                                 # //*[@id="main"]/div/section[2]/div/div[2]/div[1]/div[1]/div[2]
#             # print("post_by =======>>>",post_by)

#         # url =driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/span/span/a').get_attribute('href')
#         # print('url====>>>>',url)

#         # industry = driver.find_element(By.XPATH,'//*[@id="ember330"]/section/div[1]/div[2]').text
#         # industry = driver.find_element(By.,'//*[@id="ember329"]/section/section/div/div[2]').text
#             # industry = driver.find_element(By.CLASS_NAME,'//*[@class="t-14 mt5"]').text


#             # print("industry==========>>>>>>>>",industry)


# # #  f"{self.BASE_URL}{query_param}-{str(page)}?k={self.language}{self.CTC_FILTER_QUERY_PARAMS}{self.CITY_FILTER_PARAMS}

# # # https://www.linkedin.com/jobs/search/?currentJobId=3187310056&geoId=103644278&keywords=python&location=United%20States&refresh=true
# # # https://www.linkedin.com/jobs/search/?currentJobId=3233290445&geoId=102713980&keywords=python&location=India&refresh=true


# # # https://www.linkedin.com/feed/?trk=guest_homepage-basic_nav-header-signin
# # # https://www.linkedin.com/search/results/all/?keywords=python&origin=HISTORY&sid=%3BY9
# # # https://www.linkedin.com/jobs/search/?currentJobId=3237785651&keywords=python
# driver.close()

# # # ================================================================



from selenium import webdriver
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://linkedin.com/uas/login")
time.sleep(5)
soup=BeautifulSoup(driver.page_source, 'lxml')

username = driver.find_element(By.ID,"username")
# Enter Your Email Address
username.send_keys("please write your username of linkedin")
pword = driver.find_element(By.ID,"password")
# Enter Your Password
pword.send_keys("please write your password of linkedin")		
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3)

start=0
area_of_search = "python"
while(start<100):
    time.sleep(3)
    URL = "https://www.linkedin.com/search/results/all/?keywords="+area_of_search+"&start="+str(start)
    # URL = "https://www.linkedin.com/jobs/search/?keywords="+area_of_search+"&start="+str(start)
    driver.get(URL)
    time.sleep(5)

    links = []
    designation_l,company_l,location_l,post_date_l=[],[],[],[]
    job_type_l,employees_l,description_l=[],[],[]
    s=driver.find_elements(By.XPATH,'//*[@id="main"]/div/div/div[1]/div[2]/a')
    for i in s:
        links.append(i)
        time.sleep(3)
        i.click()


        time.sleep(10)

        hi =driver.find_elements(By.XPATH,'//*[@id="main"]/div/section[1]/div/ul/li')
        for item in hi:
            time.sleep(5)
            item.click()
    # print(len(hi))
        # list1 =[]
        # list2=[]
        

            designation = driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/a/h2').text
        
            designation_l.append(designation)      
            print("designation_partial========>>>>",designation)

        
            company=driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/span/span').text
            company_l.append(company)
            print('company====>>>>',company)

            location=driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/span/span[2]').text
            location_l.append(location)
            print('location======>>>',location)

            post_date = driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/span[2]/span').text
            post_date_l.append(post_date)
            print('post_date========>>>>',post_date)


            time.sleep(3)
            job_type = driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/ul/li[1]/span').text
                                                
            job_type_l.append(job_type)
            print('job_type=====>>>',job_type)

            employees = driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div[2]/ul/li[2]/span').text
            employees_l.append(employees)
            print("employees======>>>",employees)
            time.sleep(3)
            description = driver.find_element(By.XPATH,'//*[@id="job-details"]/span').text
            description_l.append(description)
            print("description======>>>",description)
            # print("list1=====>>>>>",list1)
            time.sleep(2)
    start = int(start)+25    

FILE_NAME = 'scrap_linkedin.csv'
df=pd.DataFrame()
df['Designation'] = designation_l
df['Company Name'] = company_l
df['Location']=location_l
df['Post Date'] = post_date_l
df['Job Type'] = pd.Series(job_type_l)
df['Employees'] = pd.Series(employees_l)
df['Job Description']=description_l
        
print(len(df),"???????????????????????????")
df.to_csv(FILE_NAME,index=False)
           
driver.close()

# # ================================================================



