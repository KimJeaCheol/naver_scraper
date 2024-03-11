import scrapy


class NaverFinanceSpider(scrapy.Spider):
    name = 'naver2'
    allowed_domains = ['finance.naver.com']
    start_urls = ['https://finance.naver.com/']

    def parse(self, response):
        # 거래상위 TOP 종목
        top_items = response.css('#_topItems1 tr')
        for item in top_items:
            volatility = item.css('tr::attr(class)').get()                                                      
            name = item.css('th a::text').get()
            current_price = item.css('td:nth-of-type(1)::text').get()
            change = item.css('td:nth-of-type(2)::text').get()
            change_value = change.strip() if change is not None else None
            rate = item.css('td:nth-of-type(3) em::text').get()
            print({
                'volatility': volatility.strip(),                
                'category': '거래상위',
                'name': name.strip(),
                'current_price': current_price.strip(),
                'change': change_value,
                'rate': rate.strip(),
            })

        # 상승 TOP 종목
        top_risers = response.css('#_topItems2 tr')
        for item in top_risers:
            volatility = item.css('tr::attr(class)').get()                                          
            name = item.css('th a::text').get()
            current_price = item.css('td:nth-of-type(1)::text').get()
            change = item.css('td:nth-of-type(2)::text').get()
            change_value = change.strip() if change is not None else None
            rate = item.css('td:nth-of-type(3) em::text').get()
            print({
                'volatility': volatility.strip(),                
                'category': '상승',
                'name': name.strip(),
                'current_price': current_price.strip(),
                'change': change_value,
                'rate': rate.strip(),
            })

        # 하락 TOP 종목
        top_fallers = response.css('#_topItems3 tr')
        for item in top_fallers:
            volatility = item.css('tr::attr(class)').get()                              
            name = item.css('th a::text').get()
            current_price = item.css('td:nth-of-type(1)::text').get()
            change = item.css('td:nth-of-type(2)::text').get()
            change_value = change.strip() if change is not None else None            
            rate = item.css('td:nth-of-type(3) em::text').get()
            print({
                'volatility': volatility.strip(),                                       
                'category': '하락',
                'name': name.strip(),
                'current_price': current_price.strip(),
                'change': change_value,
                'rate': rate.strip(),
            })

        # 시가총액 상위 TOP 종목
        top_market_caps = response.css('#_topItems4 tr')
        for item in top_market_caps:
            volatility = item.css('tr::attr(class)').get()                  
            name = item.css('th a::text').get()
            current_price = item.css('td:nth-of-type(1)::text').get()
            change = item.css('td:nth-of-type(2)::text').get()
            change_value = change.strip() if change is not None else None                 
            rate = item.css('td:nth-of-type(3) em::text').get()
            print({
                'volatility': volatility.strip(),                       
                'category': '시가총액 상위',
                'name': name.strip(),
                'current_price': current_price.strip(),
                'change': change_value,
                'rate': rate.strip(),
            })
