# -*- coding: utf-8 -*-
import codecs
import pprint
from bs4 import BeautifulSoup

_filename = r"E:\Private\develop\CrawlingStudy\temp\kis.html"

# codecs.open이 아닌 일반 open으로 처리할 경우 UnicodeDecodeError가 발생한다.
with codecs.open(_filename, 'r', 'utf-8') as f:
    html = f.read()

_soup = BeautifulSoup(html, 'html.parser')

# 등급이 평가된 기관의 기관명만 리스트에 담는다.
org_list = []
a_tag_list = _soup.select('#hot_disclosure01 tbody tr td a')
for tag in a_tag_list:
    if(tag.text.strip()): # 빈 문자열을 != ''로 판단할 필요없다.
        org_list.append(tag.text.strip())

print(org_list)
"""
# 등급이 평가된 기관의 기관명을 포함한 모든 정보를 리스트에 담는다.
# 공백이 포함되어 있다.
temp_data = []
td_tag_list = _soup.select('#hot_disclosure01 tbody tr td')
for tag in td_tag_list:
    temp_data.append(tag.text.strip())


grade_list = []
for orgname in org_list:
    for data in temp_data:
        if orgname == data:
            idx = temp_data.index(data)
            org_grade_dict = {}
            org_grade_dict['ORG_NAME'] = temp_data[idx]
            org_grade_dict['DIV'] = temp_data[idx+1]
            org_grade_dict['COUNT'] = temp_data[idx+2]
            org_grade_dict['AMOUNT'] = temp_data[idx+3]
            org_grade_dict['MAT_DATE'] = temp_data[idx+4]
            org_grade_dict['VAL_DIV'] = temp_data[idx+5]
            org_grade_dict['PRE_GRADE'] = temp_data[idx+6]
            org_grade_dict['PRE_OUTLOOK'] = temp_data[idx+6]
            org_grade_dict['NOW_GRADE'] = temp_data[idx+7]
            org_grade_dict['NOW_OUTLOOK'] = temp_data[idx+7]
            org_grade_dict['VAL_DATE'] = temp_data[idx+8]
            grade_list.append(org_grade_dict)
            break

#pprint.pprint(grade_list)
for org_grade in grade_list:
    print(org_grade)
"""