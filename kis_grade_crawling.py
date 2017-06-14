# -*- coding: utf-8 -*-
"""
신평사의 신용등급 crawling
"""

# 상태비교를 할 때는 객체로 즉, 참조로 비교하자.
# 값은 대체할 수 있지만 상태는 대체할 수 없다.


import codecs
from bs4 import BeautifulSoup

def get_html_by_file(filename):
    """
    다운받은 html파일을 로드하여 html추출
    테스트용
    """
    # codecs.open이 아닌 일반 open으로 처리할 경우 UnicodeDecodeError가 발생한다.
    with codecs.open(filename, 'r', 'utf-8') as filep:
        html = filep.read()
    return html
    # return을 함수로 하면 지연평가를 할 수 있다.
    # 그리고 다양한 활동을 할 수 있다.




def get_org_list(html, tag_set):
    """
    bs4를 이용하여 html 파일에서 기관리스트 추출
    """
    soup = BeautifulSoup(html, 'html.parser')
    # 등급이 평가된 기관의 기관명만 리스트에 담는다.
    org_list = []
    a_tag_list = soup.select(tag_set)
    for tag in a_tag_list:
        if tag.text.strip(): # 빈 문자열을 != ''로 판단할 필요없다.
            org_list.append(tag.text.strip())

    return org_list

# 등급이 평가된 기관의 기관명을 포함한 모든 정보를 리스트에 담는다.
# 공백이 포함되어 있다.
def getcrawling_data(html, tag_set):
    """
    해당 tag_set의 모든 데이터 crawling
    """
    soup = BeautifulSoup(html, 'html.parser')

    result = []
    td_tag_list = soup.select(tag_set)
    for tag in td_tag_list:
        result.append(tag.text.strip())

    return result


def get_grade_list(web_page, list_tag, data_tag, make_grade_list):
    """
    crawling data에서 등급 정보 dict 생성
    """
    org_list = get_org_list(get_html_by_file(web_page), list_tag)
    crawling_data = getcrawling_data(get_html_by_file(web_page), data_tag)

    return make_grade_list(org_list, crawling_data)

def make_issuer_grade(org_list, crawling_data):
    """
    발행사 신용등급 리스트를 만든다.
    """
    grade_list = []
    for orgname in org_list:
        for data in crawling_data:
            if orgname == data:
                idx = crawling_data.index(data)
                org_grade_dict = {}
                org_grade_dict['ORG_NAME'] = crawling_data[idx]
                org_grade_dict['FIDATE'] = crawling_data[idx+1]
                org_grade_dict['VALDIV'] = crawling_data[idx+2]
                org_grade_dict['PRE_GRADE'] = crawling_data[idx+3]
                org_grade_dict['PRE_OUTLOOK'] = crawling_data[idx+4]
                org_grade_dict['NOW_GRADE'] = crawling_data[idx+5]
                org_grade_dict['NOW_OUTLOOK'] = crawling_data[idx+6]
                org_grade_dict['CURRENCY'] = crawling_data[idx+7]
                org_grade_dict['VAL_DATE'] = crawling_data[idx+8]
                grade_list.append(org_grade_dict)
                break

    return grade_list

def make_bond_grade(org_list, crawling_data):
    """
    발행사 신용등급 리스트를 만든다.
    """
    grade_list = []
    for orgname in org_list:
        for data in crawling_data:
            if orgname == data:
                idx = crawling_data.index(data)
                org_grade_dict = {}
                org_grade_dict['COMPANY_NAME'] = crawling_data[idx]
                org_grade_dict['DIV'] = crawling_data[idx+1]
                org_grade_dict['COUNT'] = crawling_data[idx+2]
                org_grade_dict['ISSUE_AMOUNT'] = crawling_data[idx+3]
                org_grade_dict['MAT_DATE'] = crawling_data[idx+4]
                org_grade_dict['VAL_DIV'] = crawling_data[idx+5]
                org_grade_dict['PRE_GRADE'] = crawling_data[idx+6]
                org_grade_dict['PRE_OUTLOOK'] = crawling_data[idx+6]
                org_grade_dict['NOW_GRADE'] = crawling_data[idx+7]
                org_grade_dict['NOW_OUTLOOK'] = crawling_data[idx+7]
                org_grade_dict['VAL_DATE'] = crawling_data[idx+8]
                grade_list.append(org_grade_dict)
                break

    return grade_list

def make_abs_grade(org_list, crawling_data):
    """
    발행사 신용등급 리스트를 만든다.
    """
    grade_list = []
    for orgname in org_list:
        for data in crawling_data:
            if orgname == data:
                idx = crawling_data.index(data)
                org_grade_dict = {}
                org_grade_dict['COMPANY_NAME'] = crawling_data[idx]
                org_grade_dict['DIV'] = crawling_data[idx+1]
                org_grade_dict['COUNT'] = crawling_data[idx+2]
                org_grade_dict['ISSUE_AMOUNT'] = crawling_data[idx+3]
                org_grade_dict['MAT_DATE'] = crawling_data[idx+4]
                org_grade_dict['VAL_DIV'] = crawling_data[idx+5]
                org_grade_dict['PRE_GRADE'] = crawling_data[idx+6]
                org_grade_dict['NOW_GRADE'] = crawling_data[idx+7]
                org_grade_dict['VAL_DATE'] = crawling_data[idx+8]
                grade_list.append(org_grade_dict)
                break

    return grade_list


def print_kis_issuer_grade_list():
    """
    KIS 발행사 신용등급 출력
    테스트용
    """
    kis_web_page = r"E:\Private\develop\CrawlingStudy\temp\kis.html"
    issuer_tag_for_list = '#hot_disclosure03 tbody tr td a'
    issuer_tag_for_data = '#hot_disclosure03 tbody tr td'

    for org_grade in get_grade_list(kis_web_page,
                                    issuer_tag_for_list,
                                    issuer_tag_for_data,
                                    make_issuer_grade):
        print(org_grade)

def print_kis_bond_grade_list():
    """
    KIS 채권 신용등급 출력
    테스트용
    """
    kis_web_page = r"E:\Private\develop\CrawlingStudy\temp\kis.html"
    issuer_tag_for_list = '#hot_disclosure01 tbody tr td a'
    issuer_tag_for_data = '#hot_disclosure01 tbody tr td'

    for org_grade in get_grade_list(kis_web_page,
                                    issuer_tag_for_list,
                                    issuer_tag_for_data,
                                    make_bond_grade):
        print(org_grade)

def print_kis_ifrs_grade_list():
    """
    KIS 채권 신용등급 출력
    테스트용
    """
    kis_web_page = r"E:\Private\develop\CrawlingStudy\temp\kis.html"
    issuer_tag_for_list = '#hot_disclosure04 tbody tr td a'
    issuer_tag_for_data = '#hot_disclosure04 tbody tr td'

    for org_grade in get_grade_list(kis_web_page,
                                    issuer_tag_for_list,
                                    issuer_tag_for_data,
                                    make_issuer_grade):
        print(org_grade)

def print_kis_abs_grade_list():
    """
    KIS 채권 신용등급 출력
    테스트용
    """
    kis_web_page = r"E:\Private\develop\CrawlingStudy\temp\kis.html"
    issuer_tag_for_list = '#hot_disclosure05 tbody tr td a'
    issuer_tag_for_data = '#hot_disclosure05 tbody tr td'

    for org_grade in get_grade_list(kis_web_page,
                                    issuer_tag_for_list,
                                    issuer_tag_for_data,
                                    make_abs_grade):
        print(org_grade)



if __name__ == '__main__':
    print_kis_abs_grade_list()
