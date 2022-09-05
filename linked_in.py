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
username.send_keys("please enter your username here")
pword = driver.find_element(By.ID,"password")
# Enter Your Password
pword.send_keys("please enter your password here")		
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3)


links = []
designation_l,company_l,location_l,post_date_l=[],[],[],[]
job_type_l,employees_l,description_l,seperator_l=[],[],[],[]
url_l,post_by_l,post_designation_l=[],[],[]

area_of_search = "python"
location = "India"
for start in range(1,51):
    time.sleep(3)
    # URL = "https://www.linkedin.com/search/results/all/?keywords="+area_of_search+"&start="+str(start)
    URL = "https://www.linkedin.com/jobs/search/?keywords="+area_of_search+"&location="+location+"&start="+str(start)
    # time.sleep(5)
    driver.get(URL)
    
    # s=driver.find_elements(By.XPATH,'//*[@id="main"]/div/div/div[1]/div[2]/a')
    # for i in s:
    #     links.append(i)
    #     time.sleep(3)
    #     i.click()





    time.sleep(5)
    # target = driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div')
    # time.sleep(1)
    # driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', target)
    # driver.implicitly_wait(1)
    # time.sleep(1)   


    









    # hi =driver.find_elements(By.XPATH,'//*[@id="main"]/div/section[1]/div/ul/li')
    # for item in hi:
    #     time.sleep(5)
    #     item.click()
    # # print(len(hi))
    #     # list1 =[]
    #     # list2=[]
        
    print("start=======>>>>>>",start)
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
    print("description======>>>",start,description)

    time.sleep(2)

    url =driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/span/span/a').get_attribute('href')
    url_l.append(url)
    print('url====>>>>',url)

    try:
        post_by = driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/a').text
        post_by_l.append(post_by)
        print("post_by=========>>>>>>>",post_by)
    except:
        post_by_l.append("NA")
        print("NA")

    try:
        post_designation = driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div')
        post_designation_l.append(post_designation)
        print("post_designation============>>>>>>>",post_designation)
        # linked-area flex-1
    except:
        post_designation_l.append("NA")
        print("NA")
    time.sleep(10)

    

    # time.sleep(5)
    # industry = driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[6]') 
    # industry = driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[6]')
    # industry.screenshot('indus.png')
    # industry1 = driver.find_element(By.XPATH,'//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[6]').text

    # print(industry1)
    
    
    seperator = "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print(seperator)
    # break
        

FILE_NAME = 'scrap_linkedin.csv'
df=pd.DataFrame()
df['Designation'] = designation_l
df['Company Name'] = company_l
df['Location']=location_l
df['Post Date'] = post_date_l
df['Job Type'] = pd.Series(job_type_l)
df['Employees'] = pd.Series(employees_l)
df['Job Description'] = description_l
df['URL'] = url_l
df['Post By'] = post_by_l
df['Post Designation'] = post_designation_l
        
print(len(df),"???????????????????????????")
df.to_csv(FILE_NAME,index=False)
           
driver.close()

# # ================================================================

