# pipelines.py

import pymysql
from naver_scraper.items import finance
from naver_scraper.items import stock
from naver_scraper.items import stockSearchTop


class NaverFinancePipeline:
    def __init__(self, host, port , user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(
            host=settings.get('DATABASE').get('host'),
            port=settings.get('DATABASE').get('port'),
            user=settings.get('DATABASE').get('username'),
            password=settings.get('DATABASE').get('password'),
            database=settings.get('DATABASE').get('database')
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        with self.db.cursor() as cursor:
            if isinstance(item, stock): 
                sql1 = """INSERT INTO mystock(volatility, category, name, current_price, change_value, rate) 
                        VALUES (%s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql1, (
                    item.get('volatility'),
                    item.get('category'),
                    item.get('name'),
                    item.get('current_price'),
                    item.get('change_value'),
                    item.get('rate')
                ))
            elif isinstance(item, finance):  # Check if the item is an instance of MyItem2
                sql2 = """INSERT INTO market_indicators (volatility, currency, current_rate, change_value, caption) 
                        VALUES (%s, %s, %s, %s, %s)"""
                cursor.execute(sql2, (
                    item.get('volatility'),
                    item.get('currency'),
                    item.get('current_rate'),
                    item.get('change_value'),  # 변경된 키 이름으로 수정
                    item.get('caption'), # 변경된 키 이름으로 수정
                ))
            elif isinstance(item, stockSearchTop):  # Check if the item is an instance of MyItem2
                sql2 = """INSERT INTO stock_search_top (rank_num, stock_name, search_rate, current_price, change_value, change_percent, volume, opening_price, high_price, low_price, per, roe)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql2, (
                    item.get('rank_num'),
                    item.get('stock_name'),
                    item.get('search_rate'), 
                    item.get('current_price'),
                    item.get('change_value'),
                    item.get('change_percent'),
                    item.get('volume'),
                    item.get('opening_price'),
                    item.get('high_price'),
                    item.get('low_price'),
                    item.get('per'),
                    item.get('roe'),
                ))
            self.db.commit()
        return item