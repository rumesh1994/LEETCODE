
# coding: utf-8

# California’s Prop65 website has a list of all chemicals deemed harmful. Write a script to extract 
# 1) the chemical name 2) the date(s) the chemical was listed 3) where it is typically used (e.g., acetochlor is used as a herbicide)

# Approach for this task is as follows:
# 1.p65list091319 contains Chemical Name, CAS number, Type of Toxicity, Listing Mechanism, Date Listed, NSRL or MADL (µg/day)a
# 2.OEHHA-chemicals_2019-12-08T03-34-34 contains Chemical Name , CAS Number, Use(s) and other columns
# 3.Merge both the csv based on Chemical Name 
# 4.Verify the details for one chemical by web scraping too.

import pandas as pd
import numpy as np
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

# STEP 1: Read the p65list091319 file, define the column headers
data = pd.read_csv('p65list091319.csv',encoding='unicode_escape', header=None)
# print(data.shape)
df = data.loc[12:,0:5]
df.columns = ['Title', 'Type of Toxicity', 'Listing Mechanism', 'CAS Number', 'Date Listed', 'NSRL or MADL (µg/day)a']
# print(df.head(), df.shape)

# The number of null rows in respective columns
[(i,df[i].isnull().sum().sum()) for i in df.columns]

# The number of unique values in respective columns
[(i,len(set(df[i]))) for i in df.columns]

# STEP 2: Reads the OEHHA-chemicals_2019-12-08T03-34-34 csv having chemical name, Uses too
df2 = pd.read_csv('OEHHA-chemicals_2019-12-08T03-34-34.csv', usecols=['Title','CAS Number', 'Use(s)'])
# print(df2.shape)

# Remove null values in the title columns
df = df.dropna(axis=0, subset=['Title'])
# Copy df with selected columns below into df_new
df_new = df[['Title', 'Date Listed', 'Type of Toxicity', 'Listing Mechanism']].copy()

# print(len(set(df['Title']).union(set(df2['Title']))))

# STEP 3: Merging 2 csvs to get the required results on the 'title' field
# Copy df2 to df_use
df_use = df2.copy()
# Merge df_new and df_use onto df_use with outer join on the common field 'Title'. Call it d3.
d3 = df_use.merge(df_new, how='outer', on='Title')
# Export d3 to csv format with the name final.csv
d3.to_csv("final.csv",index=False)

# STEP 4: Web scarpping to get information for acrylamide or benzene to verify the use details. Inspect the page
# to understand the structure of the html page.
# Tried with BeautifulSoup module, it tried blocking (Not a robot) by showing 'Request unsuccessful. Incapsula incident ID'.
page = requests.get("https://www.p65warnings.ca.gov/fact-sheets/benzene")
print(page) 
page.content

# Output : <Response [200]>
# Request unsuccessful. Incapsula incident ID: xx..... </iframe></body></html>
# Refer : https://support.incapsula.com/hc/en-us/articles/209074918-Common-Incapsula-Errors-and-Their-Solutions-
# https://stackoverflow.com/questions/36971604/getting-wrong-page-source-when-calling-url-from-python

# Hence tried doing the same with another module webdriver
driver = webdriver.Chrome("chromedriver.exe")
# Url for benzene
driver.get("https://www.p65warnings.ca.gov/fact-sheets/benzene")
# Inspect the page and find the class of the content that is required
elements = driver.find_elements_by_xpath(".//li[@role='presentation']")
x = driver.find_elements_by_xpath(".//div[@class='ds-1col node node-fact-sheet view-mode-full clearfix']")
for element in x:
    a = element.find_elements_by_xpath(".//ul[@class='list-understated']")
print([i.text for i in a])
# Output: ['Related Chemical(s)\nBenzene', 'Related Product or Place\nPetroleum Products\nService Stations\nVehicle-Repair Facilities\nPassenger and Off-Highway Motor Vehicles\nRecreational Vessels\nDiesel Engine Exhaust']
# To verify look at row 97/98 in final.csv

# References:
# https://brainsdrains.com/web-scraping-with-python-and-selenium-beginners-guide/
# https://www.programcreek.com/python/example/89106/selenium.webdriver.remote.webelement.WebElement
# https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486

