from urllib.parse import urlencode
from .web_request import json_request


ACCESS_TOKEN = 'lPho2AedT94HdWcuLEqLx%2FxutLFprTW4diIv6lp%2FylcbEtT0TFuMSfWdSiWip2LcqZ3fRfZ4tTKNyZiU%2BKUfAw%3D%3D'
EndPoint = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'

def pd_gen_url(base=EndPoint, **params):
    url = '%s?serviceKey=%s&%s' % (base, ACCESS_TOKEN, urlencode(params))
    return url


def pd_fetch_tourspot_visitor(district1='', district2='', tourspot='', year=0, month=0):
    url = pd_gen_url(YM='{0:04d}{1:02d}'.format(year, month),
                     SIDO=district1,
                     GUNGU=district2,
                     RES_NM=tourspot,
                     numOfRows='10',
                     _type='json',
                     pageNo=1)

    json_result = json_request(url=url)
    print(json_result)

'''
    isnext = True

    while isnext is True:
        json_result = json_request(url=url)

        paging = None if json_result is None else json_result.get('paging')
        posts = None if json_result is None else json_result.get('data')

        url = None if paging is None else paging.get('next')
        isnext = url is not None

        yield posts
'''