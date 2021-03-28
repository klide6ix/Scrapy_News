import scrapy
from news.items import NewsItem

class NaverSpider(scrapy.Spider):
    name = 'naver'
    allowed_domains = ['finance.naver.com']
    start_urls = [
        'https://finance.naver.com/item/news_news.nhn?code=036570&page=1&sm=title_entity_id.basic&clusterId=',
        'https://finance.naver.com/item/news_news.nhn?code=036570&page=2&sm=title_entity_id.basic&clusterId=',
        'https://finance.naver.com/item/news_news.nhn?code=036570&page=3&sm=title_entity_id.basic&clusterId=',
        'https://finance.naver.com/item/news_news.nhn?code=036570&page=4&sm=title_entity_id.basic&clusterId=',
        'https://finance.naver.com/item/news_news.nhn?code=036570&page=5&sm=title_entity_id.basic&clusterId=',
        'https://finance.naver.com/item/news_news.nhn?code=036570&page=6&sm=title_entity_id.basic&clusterId=',
        'https://finance.naver.com/item/news_news.nhn?code=036570&page=7&sm=title_entity_id.basic&clusterId=',
        'https://finance.naver.com/item/news_news.nhn?code=036570&page=8&sm=title_entity_id.basic&clusterId=',
        'https://finance.naver.com/item/news_news.nhn?code=036570&page=9&sm=title_entity_id.basic&clusterId=',
        'https://finance.naver.com/item/news_news.nhn?code=036570&page=10&sm=title_entity_id.basic&clusterId=',
        'https://finance.naver.com/item/news_news.nhn?code=036570&page=11&sm=title_entity_id.basic&clusterId=',
        'https://finance.naver.com/item/news_news.nhn?code=036570&page=12&sm=title_entity_id.basic&clusterId=',
        'https://finance.naver.com/item/news_news.nhn?code=036570&page=13&sm=title_entity_id.basic&clusterId=',
        'https://finance.naver.com/item/news_news.nhn?code=036570&page=14&sm=title_entity_id.basic&clusterId=',
        'https://finance.naver.com/item/news_news.nhn?code=036570&page=15&sm=title_entity_id.basic&clusterId='
    ]

    def parse(self, response):
        result = response.css('tbody *::text').getall()

        prefix = ('\n', '\t')        
        for line in result[:]:
            if line.startswith(prefix):
                result.remove(line)

        print(result)
        
        # index : 0  - article
        # index : 1  - press
        # index : 2  - date
        index = 0
        while index < len(result):
            if result[index] == "연관기사 목록":
                index += 1
                continue

            if result[index] == "관련뉴스 ":
                index += 3
                continue

            item = NewsItem()
            item['article'] = result[index]
            item['press'] = result[index + 1]
            item['date'] = result[index + 2]

            index += 3

            yield item
