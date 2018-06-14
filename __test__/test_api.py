import analysis_pd.collect.api as pdapi

# test for pd_gen_url
url = pdapi.pd_gen_url(
    'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
    YM='{0:04d}{1:02d}'.format(2017, 1),
    SIDO='서울특별시',
    GUNGU='',
    RES_NM='',
    numOfRows=10,
    _type='json',
    pageNo=1)

print(url)


# test for pd_fetch_foreign_visitor
item = pdapi.pd_fetch_foreign_visitor(112, 2012, 7)
print(item)


# test for pd_fetch_tourspot_visitor
for year in range(2017, 2017 + 1):
    for month in range(1, 13):
        for item in pdapi.pd_fetch_tourspot_visitor(
                district1='서울특별시',
                year=year,
                month=month):
            print(item)