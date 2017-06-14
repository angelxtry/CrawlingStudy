# -*- coding: utf-8 -*-
import codecs
import os
import pprint
from bs4 import BeautifulSoup

filename = r"E:\Private\develop\CrawlingStudy\temp\kis.html"

print(os.getcwd())

org_list = []
temp_data = []
with codecs.open(filename, 'r', 'utf-8') as f:
    print(filename)
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

a_tag_list = soup.select('#hot_disclosure03 tbody tr td a')
for tag in a_tag_list:
    if(tag.text.strip() != ''):
        org_list.append(tag.text.strip())

for idx, tag in enumerate(org_list, 1):
    print(idx, tag)

td_tag_list = soup.select('#hot_disclosure03 tbody tr td')
for tag in td_tag_list:
    temp_data.append(tag.text.strip())

grade_list = []
for orgname in org_list:
    print(orgname)
    for data in temp_data:
        if orgname == data:
            idx = temp_data.index(data)
            org_grade_dict = {}
            org_grade_dict['ORG_NAME'] = temp_data[idx]
            org_grade_dict['FIDATE'] = temp_data[idx+1]
            org_grade_dict['VALDIV'] = temp_data[idx+2]
            org_grade_dict['PRE_GRADE'] = temp_data[idx+3]
            org_grade_dict['PRE_OUTLOOK'] = temp_data[idx+4]
            org_grade_dict['NOW_GRADE'] = temp_data[idx+5]
            org_grade_dict['NOW_OUTLOOK'] = temp_data[idx+6]
            org_grade_dict['CURRENCY'] = temp_data[idx+7]
            org_grade_dict['VAL_DATE'] = temp_data[idx+8]
            print(org_grade_dict)
            grade_list.append(org_grade_dict)
            break

#pprint.pprint(grade_list)
for org_grade in grade_list:
    print(org_grade)