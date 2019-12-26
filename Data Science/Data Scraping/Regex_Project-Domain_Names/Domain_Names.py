
# coding: utf-8

# The task is to extract text from the given pdf and find all the news domain names from the extracted text.
# Approach for this task is as follows:
# 1. So initially check if the pdf is machine readable. 
# 2. If not, extract the text using OCR.
# 3. Once the text is extracted, go through each file and write regex pattern that matches domain names.
# 4. After this, check if 'news' exists in the domain names (repetition of domain names is allowed).

# STEP 1: Extract text using PyPDF2 module

# importing required modules 
import PyPDF2 

# creating a pdf file object 
pdfFile = open('Domains (Name.com).pdf', 'rb') 

# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFile)  

# creating a page object 
pageObj = pdfReader.getPage(0) 

# extracting text from page 
print(pageObj.extractText()) 

# closing the pdf file object 
pdfFile.close() 


# STEP 2: Step 1 didn't extract the text and hence Extracted the text using OCR by follwing the link below.
# Each page forms one text document. Hence we obtain 19 text files.
# https://pypi.org/project/pypdfocr/ or https://www.sejda.com/ocr-pdf

# STEP 3: It's time to write the regex pattern. The re module is used for this. Glob module assits in going through
# all the text files extracted for the pdf in a folder. The csv module writes the output into an excel file.

import glob
import re
import csv

# Reads the files
mylist = ['Domains (Name.com)/' + f.split('\\')[1] for f in glob.glob("Domains (Name.com)/*.txt")]

# This finds all the domain names given in the pdf across all pages
y = []
news = []
for i in mylist:
    # There are different types of character encodings (the coded character set is mapped to bytes for manipulation)
    # such as ASCII and Unicode.
    with open(i,encoding="utf8") as f: 
        for line in f: 
            pattern = '(?:[a-zA-Z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z]'
            result = re.findall(pattern, line) 
            
            # STEP 4: Finds if it is a news related domain name or not
            if result != []:
                y.append(result)
                if len(result) == 1:
                    if result[0].split('.')[0].find('news') != -1:
                            news.append(result[0])
                else:
                    for i in result:
                        if i.split('.')[0].find('news') != -1:
                            news.append(i)
# print(news)
# ['news9diet.com', 'news9diet.com', 'news9diet.com', 'news9diet.com', 'news9diet.com', 'news9diet.com', 'news7health.com', 'f7news.com', 'tv9newstoday.com', 'Snews.tv', 'fdx8news.com', 'newsat6health.com', 'memphisaqazettenews.com', 'memphisgazettenews.net', 'memphisaazettenews.org', 'memphisaazettenews.tv']

# Outputs the related domain names to excel                            
with open('output_Domain.csv','w', newline='') as result_file:
    wr = csv.writer(result_file, dialect='excel')
    wr.writerows(y)

# References:
# https://www.regextester.com
# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory 
# https://python.developreference.com/article/10451647/Imagemagick+FailedToExecuteCommand+%60%E2%80%9Cgswin32c.exe%E2%80%9D http://docs.wand-py.org/en/latest/guide/install.html#install-imagemagick-windows
