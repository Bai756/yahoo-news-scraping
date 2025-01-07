import scrapy
from yahoo_news.items import YahooNewsItem


class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["www.finance.yahoo.com"]
    start_urls = ["https://finance.yahoo.com/topic/latest-news/"]

    def parse(self, response):
        for news in response.css("div.content.yf-18q3fnf"):
            item = YahooNewsItem()
            item["title"] = news.css("a::attr(aria-label)").get()
            item["url"] = news.css("a::attr(href)").get()
            item["source"] = news.css("div > div.publishing.yf-1weyqlp::text").get()
            yield item
    
            
