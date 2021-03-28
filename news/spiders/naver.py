import scrapy
from news.items import NewsItem
from time import sleep

class NaverSpider(scrapy.Spider):
    name = 'naver'
    allowed_domains = ['finance.naver.com']
        
    def __init__(self):
        self.start_urls = []
        for i in range(1, 5):
            self.start_urls.append('https://finance.naver.com/item/news_news.nhn?code=005930&page={}&sm=title_entity_id.basic&clusterId='.format(i))

    def parse(self, response):
        sleep(1)
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
