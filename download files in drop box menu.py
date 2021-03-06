# -*- utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome('your chromedriver path')

url = r"http://ftc.go.kr/info/dataopen/openCommList.jsp"

def download_file () :
    driver.get(url) # get url from webpage
    driver_province = driver.find_elements_by_xpath("//select[@id='area1']/option[@value]") # find the lists of province
    count_province = 1 # number the province
    while True:
        count_city = 1 # number the city
        try :
            driver_province[count_province].click() # pick a province in the list
            driver_city = driver.find_elements_by_xpath("//select[@id='area2']/option[@value]") # find the lists of cities
            while True :
                try :
                    driver.implicitly_wait(1)
                    driver_city[count_city].click()
                    driver.find_element_by_xpath("//a[@href='javascript:fct_down();']").click()
                    print(driver_city[count_city].text + ' downloaded well ' + str(count_province) + ' ' + str(count_city))
                except :
                    break
                count_city += 1
        except :
            driver_province = driver.find_elements_by_xpath("//select[@id='area1']/option[@value]")  # find the lists of province
            count_province += 1

download_file()
