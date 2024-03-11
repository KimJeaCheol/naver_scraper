import scrapy

class ExchangeRateSpider(scrapy.Spider):
    name = 'finance1'
    allowed_domains = ['finance.naver.com']
    start_urls = ['https://finance.naver.com/']

    def parse(self, response):
        # article2 밑에 있는 section1과 section2를 구분합니다.
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
                # 테이블의 각 행에서 데이터를 추출합니다.
                rows = group.css('tbody tr')
                for row in rows:
                    # 각 행의 데이터를 추출합니다.
                    currency = row.css('th a::text').get().strip()
                    current_rate = row.css('td:nth-child(2)::text').get().strip()
                    change_element = row.css('td:nth-child(3)::text').get()

                    # "전일대비" 데이터가 존재하는 경우에만 strip() 함수를 호출합니다.
                    change = change_element.strip() if change_element else None
                    volatility = row.css('::attr(class)').get().strip().split()[0]

                    # 추출한 데이터를 yield하여 반환합니다.
                    yield{
                        'volatility': volatility,
                        'currency': currency,
                        'current_rate': current_rate,
                        'change_value': change,
                        'caption': caption
                    }