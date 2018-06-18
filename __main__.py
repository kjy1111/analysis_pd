import collect
from config import CONFIG
import analyze
import visualize

if __name__ == '__main__':

    # 데이터 수집(collectino)

    collect.crawling_tourspot_visitor(district=CONFIG['district'], **CONFIG['common'])

    for country in CONFIG['countries']:
        collect.crawling_foreign_visitor(country, **CONFIG['common'])

    # 데이터 분석(analyze)