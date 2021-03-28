import scrapy

# https://finance.naver.com/item/news_news.nhn?code=036570&page=1&sm=title_entity_id.basic&clusterId=
# https://finance.naver.com/item/news_news.nhn?code=036570&page=2&sm=title_entity_id.basic&clusterId=
# https://finance.naver.com/item/news_news.nhn?code=036570&page=3&sm=title_entity_id.basic&clusterId=
# https://finance.naver.com/item/news_news.nhn?code=036570&page=4&sm=title_entity_id.basic&clusterId=
# page=x -> 각 뉴스 페이지

class NaverSpider(scrapy.Spider):
    name = 'naver'
    allowed_domains = ['finance.naver.com']
    start_urls = ['https://finance.naver.com/item/news_news.nhn?code=036570&page=1&sm=title_entity_id.basic&clusterId=']

    def parse(self, response):        
        response.css('*::text').getall()
        # pass
