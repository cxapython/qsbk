# -*- coding: utf-8 -*-
import scrapy
import datetime
from qiushibaike.items import QiushibaikeItem, QItemLoader


class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = (f'https://www.qiushibaike.com/8hr/page/{i}/' for i in range(11))

    def parse(self, response):
        content_left_node = response.xpath("//div[@id='content-left']")  # 确定发布区的节点区域
        div_node_list = content_left_node.xpath("./div")
        crawl_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for div_node in div_node_list:
            item = QiushibaikeItem()
            l = QItemLoader(item, selector=div_node)
            l.add_xpath('name',
                        ".//div[@class='author clearfix']/a[contains(@onclick,'web-list-author-text')]/h2/text()",
                        )
            l.add_xpath('info', ".//div[@class='content']/span[1]//text()")
            l.add_value('crawl_date', crawl_date)
            data = l.load_item()
            print(data)
            yield data
            # content = content_node.xpath('string(.)')
            # name = title_node.extract_first()
            # info = content.extract_first()
            # crawl_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # item['name'] = name.strip() if name else name
            # item['info'] = info.strip() if info else info
            # item['crawl_date'] = crawl_date
            # yield item
