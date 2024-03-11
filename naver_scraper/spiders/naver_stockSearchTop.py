import scrapy
from naver_scraper.items import stockSearchTop

class NaverFinanceStockSearchTop(scrapy.Spider):
    name = 'stocksearchtop'
    allowed_domains = ['finance.naver.com']
    start_urls = ['https://finance.naver.com/sise/lastsearch2.naver']

    def parse(self, response):
        # article2 밑에 있는 section1과 section2를 구분합니다.
        content_area = response.css('#contentarea')
        rows = content_area.css('div.box_type_l')
        test = rows.css('table')
        print(test)
        
        # 각 section에 대해 반복합니다.
        for row in rows[1:]:  # 첫 번째 행은 테이블의 헤더이므로 건너뜁니다
            item = stockSearchTop()
            # 각 행의 데이터를 추출합니다.
            item['rank_num'] = row.css('td:nth-child(1)::text').get()
            item['stock_name'] = row.css('td:nth-child(2) a::text').get()
            item['search_rate'] = row.css('td:nth-child(3)::text').get()
            item['current_price'] = row.css('td:nth-child(4)::text').get()
            item['change_value'] = row.css('td:nth-child(5)::text').get()
            item['change_percent'] = row.css('td:nth-child(6)::text').get()
            item['volume'] = row.css('td:nth-child(7)::text').get()
            item['opening_price'] = row.css('td:nth-child(8)::text').get()
            item['high_price'] = row.css('td:nth-child(9)::text').get()
            item['low_price'] = row.css('td:nth-child(10)::text').get()
            item['per'] = row.css('td:nth-child(11)::text').get()
            item['roe'] = row.css('td:nth-child(12)::text').get()
            yield item # 추출한 데이터를 yield하여 반환합니다.