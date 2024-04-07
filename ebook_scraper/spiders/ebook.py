import scrapy
from ebook_scraper.items import EbookItem
from scrapy.loader import ItemLoader



class EbookSpider(scrapy.Spider):
    name = "ebook"

    start_urls = ['https://books.toscrape.com/catalogue/category/books/travel_2/']
    # cols = ["Title", "Price"]

    # def __init__(self):
    #     super().__init__()
    #     self.page_count = 1
    #     self.total_pages = 4
    
    # def start_requests(self):
    #     base_url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5"

    #     while self.page_count <= self.total_pages:
    #         yield scrapy.Request(
    #             f"{base_url}/page-{self.page_count}.html"
    #         )
    #         self.page_count +=1


    def parse(self, response):
        # self.page_count +=1
        # print(response.css("h3 a::text").get())

        #select table data

        table = response.css("table")
        product_details = {}

        for row in table.css("tr"):
            heading = row.css("th::text").get()
            data = row.css("td::text").get()

            product_details[heading] = data

        yield product_details

        #following links
        # ebooks = response.css("article.product_pod")

        # for ebook in ebooks:
        #     # loader = ItemLoader(item=EbookItem(), selector=ebook)
        #     # loader.add_css('title', "h3 a::attr(title)")
        #     # # loader.add_value('price', ebook.css("p.price_color::text").get())
        #     # loader.add_css('price', "p.price_color::text")
        #     url = ebook.css("h3 a").attrib['href']

        #     yield scrapy.Request(
        #         url=self.start_urls[0] + url,
        #         callback= self.parse_details
        #     )

    # following links
    # def parse_details(self, response):
    #     main = response.css("div.product_main")
    #     loader = ItemLoader(item= EbookItem(), selector=main)
    #     loader.add_css("title", "h1::text")
    #     loader.add_css("price", "p.price_color::text")
    #     quantity_p = main.css("p.availability")
    #     loader.add_value("quantity", quantity_p.re(r'\(.+ available\)')[0])
    #     yield loader.load_item()

            
            
            # yield loader.load_item()
        
        # print("[PAGE COUNT ]: ", self.page_count)
        
        # next_btn = response.css("li.next a")

        # if next_btn:
        #     next_page = f"{self.start_urls[0]}/{next_btn.attrib['href']}"
        #     yield scrapy.Request(url=next_page)
