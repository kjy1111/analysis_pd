import collect

if __name__ == '__main__':

    # collect

    collect.crawling_tourspot_visitor('서울특별시', 2017, 2017)



    for country in [('중국', 112), ('일본', 130), ('미국', 275)]:
        collect.crawling_foreign_visitor(country, 2017, 2017)
