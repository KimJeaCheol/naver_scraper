import scrapy
from naver_scraper.items import finance
from naver_scraper.items import stock

class NaverFinanceSpider(scrapy.Spider):
    name = 'finance'
    allowed_domains = ['finance.naver.com']
    start_urls = ['https://finance.naver.com/']

    def parse(self, response):
        # 거래상위 TOP 종목
        top_items = response.css('#_topItems1 tr')
        for value in top_items:
            item = stock()
            item['volatility'] = value.css('tr::attr(class)').get()
            item['category'] = '거래상위'
            item['name'] = value.css('th a::text').get()
            item['current_price'] = value.css('td:nth-of-type(1)::text').get().strip()
            change = value.css('td:nth-of-type(2)::text').get()
            change_value = change.strip() if change is not None else None
            item['change_value'] = change_value
            item['rate'] = value.css('td:nth-of-type(3) em::text').get().strip()
            yield item

        # 상승 TOP 종목
        top_risers = response.css('#_topItems2 tr')
        for value in top_risers:
            item = stock()
            item['volatility'] = value.css('tr::attr(class)').get()
            item['category'] = '상승'
            item['name'] = value.css('th a::text').get()
            item['current_price'] = value.css('td:nth-of-type(1)::text').get().strip()
            change = value.css('td:nth-of-type(2)::text').get()
            change_value = change.strip() if change is not None else None
            item['change_value'] = change_value
            item['rate'] = value.css('td:nth-of-type(3) em::text').get().strip()
            yield item

        # 하락 TOP 종목
        top_fallers = response.css('#_topItems3 tr')
        for value in top_fallers:
            item = stock()
            item['volatility'] = value.css('tr::attr(class)').get()
            item['category'] = '하락'
            item['name'] = value.css('th a::text').get()
            item['current_price'] = value.css('td:nth-of-type(1)::text').get().strip()
            change = value.css('td:nth-of-type(2)::text').get()
            change_value = change.strip() if change is not None else None
            item['change_value'] = change_value
            item['rate'] = value.css('td:nth-of-type(3) em::text').get().strip()
            yield item

        # 시가총액 상위 TOP 종목
        top_market_caps = response.css('#_topItems4 tr')
        for value in top_market_caps:
            item = stock()
            item['volatility'] = value.css('tr::attr(class)').get()
            item['category'] = '시가총액 상위'
            item['name'] = value.css('th a::text').get()
            item['current_price'] = value.css('td:nth-of-type(1)::text').get().strip()
            change = value.css('td:nth-of-type(2)::text').get()
            change_value = change.strip() if change is not None else None
            item['change_value'] = change_value
            item['rate'] = value.css('td:nth-of-type(3) em::text').get().strip()
            yield item

        sections = response.css('div.article2 div.section1, div.article2 div.section2')
        # 각 section에 대해 반복합니다.
        for section in sections:
            # section 내부에 있는 div.group{i} table.tbl_home을 찾습니다.
            groups = section.css('div[class^="group"] table.tbl_home')
            # 캡션과 헤더를 추출합니다.
            # 각 group에 대해 반복합니다.
            for group in groups:
                caption = group.css('caption::text').get().strip()
                headers = group.css('thead th::text').getall()
                print(headers)
                # 테이블의 각 행에서 데이터를 추출합니다.
                rows = group.css('tbody tr')
                print(rows)
                for row in rows:
                    item = finance()
                    # 각 행의 데이터를 추출합니다.
                    item['caption'] = caption
                    item['volatility'] = row.css('::attr(class)').get().strip().split()[0]
                    item['currency'] = row.css('th a::text').get().strip()
                    item['current_rate'] = row.css('td:nth-child(2)::text').get().strip()
                    change_element = row.css('td:nth-child(3)::text').get()
                    # "전일대비" 데이터가 존재하는 경우에만 strip() 함수를 호출합니다.
                    change_vlaue = change_element.strip() if change_element else None
                    item['change_value'] = change_vlaue
                    # 추출한 데이터를 yield하여 반환합니다.
                    yield item