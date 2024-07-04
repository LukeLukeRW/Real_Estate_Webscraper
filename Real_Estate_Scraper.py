import selenium
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os
import json
import keyboard

def main(file):
    global driver
    suburb_list = initialising_variables(file)
    for y in range(len(suburb_list)):
        url = f"https://www.realestate.com.au/buy/in{suburb_list[y][0]}+vic+{suburb_list[y][1]}/list-{y}"
        driver.get(url)
        soup = BeautifulSoup(driver.page_source,'html.parser')
        
        


def initialising_variables(file):
    suburb_list = []
    with open(file,'r') as file:
        j = file.readlines()
        Suburb = [i.strip() for i in j]

    for k in Suburb:
        p = k.split(' ')
        post_code = p.pop(-1)
        p = '+'.join(p)

        suburb_list.append([p,post_code])
    return suburb_list


if __name__ == '__main__':
    driver = selenium.webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    file = "Melb_Suburb_List.csv"
    main(file)

# i = None



# soup = BeautifulSoup(driver.page.source, 'html_parser')


# split at space, remove and get the -1 last one in the list
# Then with the others .join with + '+'.join


# !!
# <a href="/property-house-vic-bendigo-144287668" class="details-link residential-card__details-link"><span class="">67 Garsed Street, Bendigo</span></a>
# https://www.realestate.com.au/property-house-vic-bendigo-144287668
# /property-house-vic-bendigo-144287668
