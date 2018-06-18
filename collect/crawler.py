import os
import json
from .api import api

RESULT_DIRECTORY = '__results__/crawling'


def preprocess_tourspot_visitor(data):
    # addrCd 삭제
    del data['addrCd']
    del data['rnum']

    data['count_locals'] = data['csNatCnt']
    del data['csNatCnt']

    data['count_forigner'] = data['csForCnt']
    del data['csForCnt']

    data['tourist_spot'] = data['resNm']
    del data['resNm']

    data['data'] = data['ym']
    del data['ym']

    data['restrict1'] = data['sido']
    del data['sido']

    data['restrict2'] = data['gungu']
    del data['gungu']


def preprocess_foreign_visitor(data):
    # ed 삭제
    del data['ed']

    # edCd 삭제
    del data['edCd']

    # rnum 삭제
    del data['rnum']

    # 나라 코드
    data['counrty_code'] = data['natCd']
    del data['natCd']

    # 나라 이름
    data['counrty_name'] = data['natKorNm'].replace(' ', '')
    del data['natKorNm']

    # 방문자 수
    data['visit_count'] = data['num']
    del data['num']

    # 년, 월
    if 'ym' not in data:
        data['data'] = ''
    else:
        data['data'] = data['ym']
        del data['ym']


def crawling_tourspot_visitor(district, start_year, end_year, fetch=True, result_directory='', service_key=''):
    results = []

    if fetch:
        for year in range(start_year, end_year + 1):
            for month in range(1, 13):
                for item in api.pd_fetch_tourspot_visitor(district, year=year, month=month, service_key=service_key):
                    for data in item:
                        if data is None:
                            continue

                        preprocess_tourspot_visitor(data)
                        results.append(data)    # results += data

        # save data to file
        filename = '%s/%s_tourinstspot_%s_%s.json' % (result_directory, district, start_year, end_year)
        with open(filename, 'w', encoding='utf-8') as outfile:
            json_string = json.dumps(results, indent=4, sort_keys=False, ensure_ascii=False)
            outfile.write(json_string)

    # return filename


def crawling_foreign_visitor(country, start_year, end_year, fetch=True, result_directory='', service_key=''):
    results = []

    if fetch:
        for year in range(start_year, end_year+1):
            for month in range(1, 13):
                data = api.pd_fetch_foreign_visitor(country[1], year, month, service_key)
                if data is None:
                    continue

                preprocess_foreign_visitor(data)
                results.append(data)

        # save data to file
        filename = '%s/%s(%s)_foreign_visitor_%s_%s.json' % (result_directory, country[0], country[1], start_year, end_year)
        with open(filename, 'w', encoding='utf-8') as outfile:
            json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(json_string)