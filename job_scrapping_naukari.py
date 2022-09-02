# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# import random
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager



# class ScrapNaukriJobs:
#     BASE_URL = 'https://www.naukri.com/'
#     FILE_NAME = 'scrap_naukri_jobs.csv'
#     CTC_FILTER_QUERY_PARAMS = '&ctcFilter=101&ctcFilter=15to25&ctcFilter=25to50&ctcFilter=50to75&ctcFilter=75to100'
#     CITY_FILTER_PARAMS = '&cityTypeGid=6&cityTypeGid=17&cityTypeGid=73&cityTypeGid=97&cityTypeGid=134&cityTypeGid=139&cityTypeGid=183&cityTypeGid=220&cityTypeGid=232&cityTypeGid=9508&cityTypeGid=9509'

#     def __init__(self,language):
#         options = webdriver.ChromeOptions()
#         options.add_argument('--ignore-certificate-errors')
#         options.add_argument('--incognito')
#         options.add_argument('--headless')
#         self.driver = webdriver.Chrome(ChromeDriverManager().install())
#         self.language = language.lower()
#         self.job_detail_links = []

#     def get_job_detail_links(self):
#         for page in range(1,3):
#             query_param = f'{self.language}-jobs'
#             URL = f"{self.BASE_URL}{query_param}?k={self.language}{self.CTC_FILTER_QUERY_PARAMS}{self.CITY_FILTER_PARAMS}" if page == 1 else f"{self.BASE_URL}{query_param}-{str(page)}?k={self.language}{self.CTC_FILTER_QUERY_PARAMS}{self.CITY_FILTER_PARAMS}"            
#             self.driver.get(URL)            
#             time.sleep(5) 
#             soup=BeautifulSoup(self.driver.page_source, 'lxml')

#             for outer_artical in soup.findAll(attrs={'class':"jobTuple bgWhite br4 mb-8"}):                
#                 for inner_links in outer_artical.find(attrs={'class':"jobTupleHeader"}).findAll(attrs={'class':"title fw500 ellipsis"}):
#                     self.job_detail_links.append(inner_links.get('href'))

#     def scrap_details(self):
#         self.get_job_detail_links()
#         time.sleep(2)
#         designation_list,company_name_list,experience_list,salary_list = [],[],[],[]        
#         location_list,job_description_list,role_list,industry_type_list = [],[],[],[]        
#         functional_area_list,employment_type_list,role_category_list,education_list = [],[],[],[]       
#         key_skill_list,about_company_list,address_list,post_by_list = [],[],[],[]       
#         post_date_list,website_list,url_list = [],[],[]


#         for link in range(len(self.job_detail_links)):
#             print(link,'...')
#             time.sleep(10)
#             self.driver.get(self.job_detail_links[link])    
#             soup=BeautifulSoup(self.driver.page_source, 'lxml')

#             if soup.find(attrs={'class':"salary"})==None or soup.find(attrs={'class':'loc'})=="Remote": 
#                 continue
#             else:

#                 company_name_list.append("NA" if soup.find(attrs={'class':"jd-header-comp-name"}) == None else soup.find(attrs={'class':"jd-header-comp-name"}).text)
#                 print(company_name_list)              
#                 experience_list.append("NA" if soup.find(attrs={'class':"exp"}) == None else soup.find(attrs={'class':"exp"}).text)
#                 print(experience_list)
#                 salary_list.append("NA" if soup.find(attrs={'class':"salary"})== None else soup.find(attrs={'class':"salary"}).text)
#                 print(salary_list)

#                 s=("NA" if soup.find(attrs={'class':'loc'}) == None else soup.find(attrs={'class':'loc'}).find('a').text)
#                 if s!='Remote' or s is not 'Remote':
#                     location_list.append(s)
#                 # if s== ("Mumbai"  or "Pune" or "Hyderabad" or "Bangalore" or "Gurgaon" or "Noida" or "Delhi" or "Kolkata" or "Chennai" or "Ahmedabad") and s!="Remote":
#                     # location_list.append(s)
#                 # else:
#                     # print("9999999")

#                 designation_list.append("NA" if soup.find(attrs={'class':"jd-header-title"}) == None else soup.find(attrs={'class':"jd-header-title"}).text)
#                 print(designation_list)
#                 job_description_list.append("NA" if soup.find(attrs={'class':"job-desc"})==None else soup.find(attrs={'class':"job-desc"}).text)
#                 print(job_description_list)
#                 post_date_list.append(["NA"] if soup.find(attrs={'class':"jd-stats"}) == None else [i for i in soup.find(attrs={'class':"jd-stats"})][0].text.split(':')[1])
#                 print(post_date_list)
#                 website_list.append("NA" if soup.find(attrs={'class':"jd-header-comp-name"}) == None else soup.find(attrs={'class':"jd-header-comp-name"}).contents[0]['href'])
#                 print(website_list)
#                 url_list.append("NA" if soup.find(attrs={'class':"jd-header-comp-name"}) == None else soup.find(attrs={'class':"jd-header-comp-name"}).contents[0]['href'])
#                 print(url_list)      
                         

#                 details=[]
#                 for i in soup.find(attrs={'class':"other-details"}).findAll(attrs={'class':"details"}):
#                     details.append(i.text)

#                 role_list.append(details[0])
#                 print(role_list)
#                 industry_type_list.append(details[1])
#                 print(industry_type_list)
#                 functional_area_list.append(details[2])
#                 print(functional_area_list)
#                 employment_type_list.append(details[3])
#                 print(employment_type_list)
#                 role_category_list.append(details[4])
#                 print(role_category_list)

#                 qual=[]
#                 for i in soup.find(attrs={'class':"education"}).findAll(attrs={'class':'details'}):
#                     qual.append(i.text)
#                 education_list.append(qual)
#                 print(education_list)

#                 sk=[]
#                 for i in soup.find(attrs={'class':"key-skill"}).findAll('a'):
#                     sk.append(i.text)
#                 key_skill_list.append(",".join(sk))  
#                 print(key_skill_list)              

#                 if soup.find(attrs={'class':"name-designation"})==None:
#                     post_by_list.append("NA")
#                     print(post_by_list)
#                 else:
#                     post_by_list.append(soup.find(attrs={'class':"name-designation"}).text)
#                     print(post_by_list)

#                 if soup.find(attrs={'class':"about-company"})==None:                    
#                     about_company_list.append("NA") 
#                     print(about_company_list)                   
#                 else:                    
#                     address_list.append("NA" if soup.find(attrs={'class':"about-company"}).find(attrs={'class':"comp-info-detail"}) == None else soup.find(attrs={'class':"about-company"}).find(attrs={'class':"comp-info-detail"}).text)
#                     print(address_list)
#                     about_company_list.append(soup.find(attrs={'class':"about-company"}).find(attrs={'class':"detail dang-inner-html"}).text)

                

#         # if "Mumbai"  or "Pune" or "Hyderabad" or "Bangalore" or "Gurgaon" or "Noida" or "Delhi" or "Kolkata" or "Chennai" or "Ahmedabad" in location_list:
#             # if location_list !="Remote":
#         df=pd.DataFrame()
#         df['Designation'] = designation_list
#         df['Company Name'] = company_name_list
#         df['Salary']=salary_list
#         df['Experience']=experience_list
#         df['Location']=location_list
#         df['Role']=role_list
#         df['Skills']=key_skill_list
#         df['Qualification']=education_list
#         df['Industry Type']=industry_type_list
#         df['Functional Area']=functional_area_list
#         df['Employment Type']=employment_type_list
#         df['Role Category']=role_category_list
#         df['Address'] = address_list
#         df['Post By'] = post_by_list
#         df['Post Date'] = post_date_list
#         df['Website'] = website_list
#         df['Url'] = url_list
#         df['Job Description']=job_description_list
#         df['About Company']=about_company_list
#         print(len(df),"????????????????????????????????????????????????????????????????????????????????????????????????????????????????")

#                 # if df['location']=='Mumbai':
#         df.to_csv(self.FILE_NAME,index=False)
#         # else:
#         # print("no data")
#         self.driver.close()
        

# print("Program star time...",time.time())
# scrap_naukri = ScrapNaukriJobs("PYTHON")
# scrap_naukri.scrap_details()
# # scrap_naukri.get_job_detail_links()
# print("Execution completed...",time.time())


# ====================================================================================

# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# import random
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager



# class ScrapNaukriJobs:
#     BASE_URL = 'https://www.naukri.com/'
#     FILE_NAME = 'scrap_naukri_jobs.csv'
#     CTC_FILTER_QUERY_PARAMS = '&ctcFilter=101&ctcFilter=15to25&ctcFilter=25to50&ctcFilter=50to75&ctcFilter=75to100'
#     CITY_FILTER_PARAMS = '&cityTypeGid=6&cityTypeGid=17&cityTypeGid=73&cityTypeGid=97&cityTypeGid=134&cityTypeGid=139&cityTypeGid=183&cityTypeGid=220&cityTypeGid=232&cityTypeGid=9508&cityTypeGid=9509'

#     def __init__(self,language):
#         options = webdriver.ChromeOptions()
#         options.add_argument('--ignore-certificate-errors')
#         options.add_argument('--incognito')
#         options.add_argument('--headless')
#         self.driver = webdriver.Chrome(ChromeDriverManager().install())
#         self.language = language.lower()
#         self.job_detail_links = []

#     def get_job_detail_links(self):
#         for page in range(1,2):
#             query_param = f'{self.language}-jobs'
#             URL = f"{self.BASE_URL}{query_param}?k={self.language}{self.CTC_FILTER_QUERY_PARAMS}{self.CITY_FILTER_PARAMS}" if page == 1 else f"{self.BASE_URL}{query_param}-{str(page)}?k={self.language}{self.CTC_FILTER_QUERY_PARAMS}{self.CITY_FILTER_PARAMS}"            
#             self.driver.get(URL)            
#             time.sleep(5) 
#             soup=BeautifulSoup(self.driver.page_source, 'lxml')

#             for outer_artical in soup.findAll(attrs={'class':"jobTuple bgWhite br4 mb-8"}):                
#                 for inner_links in outer_artical.find(attrs={'class':"jobTupleHeader"}).findAll(attrs={'class':"title fw500 ellipsis"}):
#                     self.job_detail_links.append(inner_links.get('href'))

#     def scrap_details(self):
#         self.get_job_detail_links()
#         time.sleep(2)
#         designation_list,company_name_list,experience_list,salary_list = [],[],[],[]        
#         location_list,job_description_list,role_list,industry_type_list = [],[],[],[]        
#         functional_area_list,employment_type_list,role_category_list,education_list = [],[],[],[]       
#         key_skill_list,about_company_list,address_list,post_by_list = [],[],[],[]       
#         post_date_list,website_list,url_list = [],[],[]
#         list1,list2=[],[]

#         for link in range(len(self.job_detail_links)):
#             print(link,'...')
#             time.sleep(10)
#             self.driver.get(self.job_detail_links[link])    
#             soup=BeautifulSoup(self.driver.page_source, 'lxml')

#             time.sleep(2)
#             if soup.find(attrs={'class':"salary"})==None: 
#                 continue
#             else:

#                 company_name = ("NA" if soup.find(attrs={'class':"jd-header-comp-name"}) == None else soup.find(attrs={'class':"jd-header-comp-name"}).text)
#                 list1.append(company_name)
#                 print(company_name)              
#                 experience = ("NA" if soup.find(attrs={'class':"exp"}) == None else soup.find(attrs={'class':"exp"}).text)
#                 list1.append(experience)
#                 print(experience)
#                 salary = ("NA" if soup.find(attrs={'class':"salary"})== None else soup.find(attrs={'class':"salary"}).text)
#                 list1.append(salary)
#                 print(salary)

#                 s=("NA" if soup.find(attrs={'class':'loc'}) == None else soup.find(attrs={'class':'loc'}).find('a').text)
#                     # location_list.append(s)
#                 location = s
#                 print(location)
#                 # if s== ("Mumbai"  or "Pune" or "Hyderabad" or "Bangalore" or "Gurgaon" or "Noida" or "Delhi" or "Kolkata" or "Chennai" or "Ahmedabad") and s!="Remote":
#                     # location_list.append(s)
#                 # else:
#                     # print("9999999")

#                 designation = ("NA" if soup.find(attrs={'class':"jd-header-title"}) == None else soup.find(attrs={'class':"jd-header-title"}).text)
#                 print(designation)
#                 job_description = ("NA" if soup.find(attrs={'class':"job-desc"})==None else soup.find(attrs={'class':"job-desc"}).text)
#                 print(job_description)
#                 post_date = (["NA"] if soup.find(attrs={'class':"jd-stats"}) == None else [i for i in soup.find(attrs={'class':"jd-stats"})][0].text.split(':')[1])
#                 print(post_date)
#                 website = ("NA" if soup.find(attrs={'class':"jd-header-comp-name"}) == None else soup.find(attrs={'class':"jd-header-comp-name"}).contents[0]['href'])
#                 print(website)
#                 url = ("NA" if soup.find(attrs={'class':"jd-header-comp-name"}) == None else soup.find(attrs={'class':"jd-header-comp-name"}).contents[0]['href'])
#                 print(url)      
                         

#                 details=[]
#                 for i in soup.find(attrs={'class':"other-details"}).findAll(attrs={'class':"details"}):
#                     details.append(i.text)

#                 role = (details[0])
#                 print(role)
#                 industry_type = (details[1])
#                 print(industry_type)
#                 functional_area = (details[2])
#                 print(functional_area)
#                 employment_type = (details[3])
#                 print(employment_type)
#                 role_category = (details[4])
#                 print(role_category)

#                 qual=[]
#                 for i in soup.find(attrs={'class':"education"}).findAll(attrs={'class':'details'}):
#                     qual.append(i.text)
#                 education = (qual)
#                 print(education)

#                 sk=[]
#                 for i in soup.find(attrs={'class':"key-skill"}).findAll('a'):
#                     sk.append(i.text)
#                 # key_skill_list.append(",".join(sk))  
#                 # print(key_skill_list)
#                 print(sk)              

#                 if soup.find(attrs={'class':"name-designation"})==None:
#                     post_by = ("NA")
#                     print(post_by)
#                 else:
#                     post_by = (soup.find(attrs={'class':"name-designation"}).text)
#                     print(post_by)

#                 if soup.find(attrs={'class':"about-company"})==None:                    
#                     about_company = ("NA") 
#                     print(about_company)                   
#                 else:                    
#                     address = ("NA" if soup.find(attrs={'class':"about-company"}).find(attrs={'class':"comp-info-detail"}) == None else soup.find(attrs={'class':"about-company"}).find(attrs={'class':"comp-info-detail"}).text)
#                     print(address)
#                     about_company = (soup.find(attrs={'class':"about-company"}).find(attrs={'class':"detail dang-inner-html"}).text)
#                     print(about_company)

#                 # list1 = []
#                 # list1.append(company_name,experience,salary,location,designation,job_description,post_date,website,url,role,industry_type,functional_area,employment_type,role_category,education,sk,post_by,about_company)
#             print("list1==========>>>>>",list1)
#             # print(list1,"<============list1")
#         list2.append(list1)
#         print("list2======>>>>>",list2)
        
#         df=pd.DataFrame()
#         df['Designation'] = designation_list
#         df['Company Name'] = company_name_list
#         df['Salary']=salary_list
#         df['Experience']=experience_list
#         df['Location']=location_list
#         df['Role']=role_list
#         df['Skills']=key_skill_list
#         df['Qualification']=education_list
#         df['Industry Type']=industry_type_list
#         df['Functional Area']=functional_area_list
#         df['Employment Type']=employment_type_list
#         df['Role Category']=role_category_list
#         df['Address'] = address_list
#         df['Post By'] = post_by_list
#         df['Post Date'] = post_date_list
#         df['Website'] = website_list
#         df['Url'] = url_list
#         df['Job Description']=job_description_list
#         df['About Company']=about_company_list
#         print(len(df),"????????????????????????????????????????????????????????????????????????????????????????????????????????????????")

#         df.to_csv(self.FILE_NAME,index=False)
#         self.driver.close()
        

# print("Program star time...",time.time())
# scrap_naukri = ScrapNaukriJobs("PYTHON")
# scrap_naukri.scrap_details()
# # scrap_naukri.get_job_detail_links()
# print("Execution completed...",time.time())

# ====================================================================


from bs4 import BeautifulSoup
import pandas as pd
import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



class ScrapNaukriJobs:
    BASE_URL = 'https://www.naukri.com/'
    FILE_NAME = 'scrap_naukri_jobs_php.csv'
    CTC_FILTER_QUERY_PARAMS = '&ctcFilter=101&ctcFilter=15to25&ctcFilter=25to50&ctcFilter=50to75&ctcFilter=75to100'
    CITY_FILTER_PARAMS = '&cityTypeGid=6&cityTypeGid=17&cityTypeGid=51&cityTypeGid=73&cityTypeGid=97&cityTypeGid=134&cityTypeGid=139&cityTypeGid=183&cityTypeGid=220&cityTypeGid=232&cityTypeGid=9508&cityTypeGid=9509'
    INDUSTRY_FILTER_PARAMS = '&industryTypeIdGid=103&industryTypeIdGid=107&industryTypeIdGid=108&industryTypeIdGid=110&industryTypeIdGid=111&industryTypeIdGid=112&industryTypeIdGid=113&industryTypeIdGid=119&industryTypeIdGid=127&industryTypeIdGid=131&industryTypeIdGid=132&industryTypeIdGid=133&industryTypeIdGid=137&industryTypeIdGid=149&industryTypeIdGid=155&industryTypeIdGid=156&industryTypeIdGid=164&industryTypeIdGid=167&industryTypeIdGid=172&industryTypeIdGid=175'

    def __init__(self,language):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.language = language.lower()
        self.job_detail_links = []

    def get_job_detail_links(self):
        for page in range(1,25):
            query_param = f'{self.language}-jobs'
            time.sleep(5)
            if self.CITY_FILTER_PARAMS !=('&cityTypeGid=4' or '&cityTypeGid=72' or '&cityTypeGid=135' or '&cityTypeGid=184' or '&cityTypeGid=187' or '&cityTypeGid=213' or '&cityTypeGid=229' or '&cityTypeGid=260' or '&cityTypeGid=325' or '&cityTypeGid=350' or '&cityTypeGid=507' or '&cityTypeGid=542' or '&cityTypeGid=9513' or '&cityTypeGid=101' ):
                URL = f"{self.BASE_URL}{query_param}?k={self.language}{self.CITY_FILTER_PARAMS}{self.CTC_FILTER_QUERY_PARAMS}{self.INDUSTRY_FILTER_PARAMS}" if page == 1 else f"{self.BASE_URL}{query_param}-{str(page)}?k={self.language}{self.CITY_FILTER_PARAMS}{self.CTC_FILTER_QUERY_PARAMS}{self.INDUSTRY_FILTER_PARAMS}"            
                self.driver.get(URL)            
                time.sleep(5) 
            else:
                continue
            soup=BeautifulSoup(self.driver.page_source, 'lxml')

            for outer_artical in soup.findAll(attrs={'class':"jobTuple bgWhite br4 mb-8"}):                
                for inner_links in outer_artical.find(attrs={'class':"jobTupleHeader"}).findAll(attrs={'class':"title fw500 ellipsis"}):
                    self.job_detail_links.append(inner_links.get('href'))

    def scrap_details(self):
        self.get_job_detail_links()
        time.sleep(2)
        designation_list,company_name_list,experience_list,salary_list = [],[],[],[]        
        location_list,job_description_list,role_list,industry_type_list = [],[],[],[]        
        functional_area_list,employment_type_list,role_category_list,education_list = [],[],[],[]       
        key_skill_list,about_company_list,address_list,post_by_list = [],[],[],[]       
        post_date_list,website_list,url_list = [],[],[]


        for link in range(len(self.job_detail_links)):
            print(link,'...')
            time.sleep(5)
            self.driver.get(self.job_detail_links[link])    
            soup=BeautifulSoup(self.driver.page_source, 'lxml')

            if soup.find(attrs={'class':"salary"})==None or soup.find(attrs={'class':'loc'})=="Remote": 
                continue
            else:

                company_name_list.append("NA" if soup.find(attrs={'class':"jd-header-comp-name"}) == None else soup.find(attrs={'class':"jd-header-comp-name"}).text)
                print(company_name_list)              
                experience_list.append("NA" if soup.find(attrs={'class':"exp"}) == None else soup.find(attrs={'class':"exp"}).text)
                print(experience_list)
                salary_list.append("NA" if soup.find(attrs={'class':"salary"})== None else soup.find(attrs={'class':"salary"}).text)
                print(salary_list)

                loca = []
                location=("NA" if soup.find(attrs={'class':'loc'}) == None else soup.find(attrs={'class':'loc'}).findAll('a'))
                for i in location:
                    try:
                        loca.append(i.text)
                    except AttributeError:
                        loca.append(i)
                    except:
                        loca.append(i)
                    
                # key_skill_list.append(",".join(sk))  
                # print(key_skill_list)
                location_list.append(",".join(loca))
                print(location_list)

                # if s== ("Mumbai"  or "Pune" or "Hyderabad" or "Bangalore" or "Gurgaon" or "Noida" or "Delhi" or "Kolkata" or "Chennai" or "Ahmedabad") and s!="Remote":
                    # location_list.append(s)
                # else:
                    # print("9999999")

                designation_list.append("NA" if soup.find(attrs={'class':"jd-header-title"}) == None else soup.find(attrs={'class':"jd-header-title"}).text)
                print(designation_list)
                job_description_list.append("NA" if soup.find(attrs={'class':"job-desc"})==None else soup.find(attrs={'class':"job-desc"}).text)
                print(job_description_list)
                post_date_list.append(["NA"] if soup.find(attrs={'class':"jd-stats"}) == None else [i for i in soup.find(attrs={'class':"jd-stats"})][0].text.split(':')[1])
                print(post_date_list)

                try:
                    website_list.append("NA" if soup.find(attrs={'class':"jd-header-comp-name"}).contents[0]['href'] == None else soup.find(attrs={'class':"jd-header-comp-name"}).contents[0]['href'])
                    print(website_list)
                except KeyError or ValueError:
                    website_list.append("NA")
                    print(website_list)
                except:
                    website_list.append("NA")

                try:
                    url_list.append("NA" if soup.find(attrs={'class':"jd-header-comp-name"}).contents[0]['href'] == None else soup.find(attrs={'class':"jd-header-comp-name"}).contents[0]['href'])
                    print(url_list)
                except KeyError or ValueError:
                    website_list.append("NA")
                    print(website_list)
                except:
                    website_list.append("NA")    
                         

                details=[]
                for i in soup.find(attrs={'class':"other-details"}).findAll(attrs={'class':"details"}):
                    details.append(i.text)

                role_list.append(details[0].replace('Role',''))
                print(role_list)
                industry_type_list.append(details[1].replace('Industry Type',''))
                print(industry_type_list)
                functional_area_list.append(details[2].replace('Functional Area',''))
                print(functional_area_list)
                employment_type_list.append(details[3].replace('Employment Type',''))
                print(employment_type_list)
                role_category_list.append(details[4].replace('Role Category',''))
                print(role_category_list)

                qual=[]
                for i in soup.find(attrs={'class':"education"}).findAll(attrs={'class':'details'}):
                    qual.append(i.text)
                education_list.append(qual)
                print(education_list)

                sk=[]
                for i in soup.find(attrs={'class':"key-skill"}).findAll('a'):
                    sk.append(i.text)
                key_skill_list.append(",".join(sk))  
                print(key_skill_list)              

                if soup.find(attrs={'class':"name-designation"})==None:
                    post_by_list.append("NA")
                    print(post_by_list)
                else:
                    post_by_list.append(soup.find(attrs={'class':"name-designation"}).text)
                    print(post_by_list)

                if soup.find(attrs={'class':"about-company"})==None:                    
                    about_company_list.append("NA") 
                    print(about_company_list)                   
                else:                    
                    address_list.append("NA" if soup.find(attrs={'class':"about-company"}).find(attrs={'class':"comp-info-detail"}) == None else soup.find(attrs={'class':"about-company"}).find(attrs={'class':"comp-info-detail"}).text)
                    print(address_list)
                    about_company_list.append(soup.find(attrs={'class':"about-company"}).find(attrs={'class':"detail dang-inner-html"}).text)

                

        # if "Mumbai"  or "Pune" or "Hyderabad" or "Bangalore" or "Gurgaon" or "Noida" or "Delhi" or "Kolkata" or "Chennai" or "Ahmedabad" in location_list:
            # if location_list !="Remote":
        df=pd.DataFrame()
        df['Designation'] = designation_list
        df['Company Name'] = company_name_list
        df['Salary']=salary_list
        df['Experience']=experience_list
        df['Location']=location_list
        df['Role']=role_list
        df['Skills']=key_skill_list
        df['Qualification']=education_list
        df['Industry Type']=industry_type_list
        df['Functional Area']=functional_area_list
        df['Employment Type']=employment_type_list
        df['Role Category']=role_category_list
        df['Address'] = address_list
        df['Post By'] = post_by_list
        df['Post Date'] = post_date_list
        df['Website'] = pd.Series(website_list)
        df['Url'] = pd.Series(url_list)
        df['Job Description']=job_description_list
        df['About Company']=about_company_list
        print(len(df),"????????????????????????????????????????????????????????????????????????????????????????????????????????????????")

                # if df['location']=='Mumbai':
        df.to_csv(self.FILE_NAME,index=False)
        # else:
        # print("no data")
        self.driver.close()
        

print("Program star time...",time.time())
scrap_naukri = ScrapNaukriJobs("php")
scrap_naukri.scrap_details()
# scrap_naukri.get_job_detail_links()
print("Execution completed...",time.time())
